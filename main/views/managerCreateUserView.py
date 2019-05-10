from django.views.generic import CreateView
from users.models import User, Activate
from django.shortcuts import redirect
from main.forms import CreateUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.token_manager import create_expiration_date, create_key
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import get_template
from ShiftSwitch import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse_lazy

class CreateUserView(LoginRequiredMixin, CreateView):
    model = User
    template_name = "main/managerCreateUser.html"
    form_class = CreateUserForm
    success_url = reverse_lazy('main:createUser')

    def post(self, request, *args, **kwargs):
        _username = "ユーザ名は設定されていません"
        _password = "admin012"
        _email = request.POST['email']
        
        user = User()
        user.email = _email
        user.username = _username
        user.set_password(_password)
        user.is_active = False
        user.save()

        print(_username + "を作成しました")
        form = self.get_form()

        # activeモデルの作成と保存(userモデルとひも付く)
        # uuidを使ったランダムな文字列作成
        activate_key = create_key()
 
        # keyの有効期限
        expiration_date = create_expiration_date()

         # 1時間有効なURLの情報レコードを作成
        activate_instance = Activate(user=user, key=activate_key, expiration_date=expiration_date)
        activate_instance.save()
        # ドメイン取得
        current_site = get_current_site(self.request)
        domain = current_site.domain
 
        # メール本文のテンプレート取得
        message_template = get_template('mailtemplate/new/message.txt')
 
        # 64ベースのエンコード
        uid = force_text(urlsafe_base64_encode(force_bytes(activate_key)))
 
        context = {
            'protocol': 'https' if self.request.is_secure() else 'http',
            'domain': domain,
            'uid': uid,
            'user': user,
        }
 
        # メール送信
        subject = 'ご登録ありがとうございます'
        message = message_template.render(context)
        from_email = settings.EMAIL_HOST_USER
        to = [user.email]
        send_mail(subject, message, from_email, to)
 
        # result = super().form_valid(form)
 
        messages.success(
            self.request, '{}様宛に会員登録用のURLを記載したメールを送信しました。'.format(user.email))
 
        return redirect(to = '/')