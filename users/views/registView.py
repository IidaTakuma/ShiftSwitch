from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template.loader import get_template
from django.views.generic import CreateView, TemplateView
from users.forms import UsersRegistForm
from main.models import User


class UsersRegistView(CreateView):
    """ユーザー仮登録"""
    template_name = 'users/regist.html'
    form_class = UsersRegistForm

    def form_valid(self, form):
        """仮登録と本登録用メールの発行."""
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # アクティベーションURLの送付
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject_template = get_template('users/mail_template/regist/subject.txt')
        subject = subject_template.render(context)

        message_template = get_template('users/mail_template/regist/message.txt')
        message = message_template.render(context)

        user.email_user(subject, message)
        return redirect('users:regist_done')

class UsersRegistDone(TemplateView):
    """ユーザー仮登録したよ"""
    template_name = 'users/regist_done.html'

class UsersRegistComplete(TemplateView):
    """メール内URLアクセス後のユーザー本登録"""
    template_name = 'users/regist_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)  # デフォルトでは1日以内

    def get(self, request, **kwargs):
        """tokenが正しければ本登録."""
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest()

        # tokenが間違っている
        except BadSignature:
            return HttpResponseBadRequest()

        # tokenは問題なし
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    # 問題なければ本登録とする
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()