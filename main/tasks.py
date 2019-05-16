import json
import requests
import ShiftSwitch.settings as settings
from django.template.loader import get_template

def send_slack_message(message):
    requests.post(settings.SLACK_WEBHOOK_ENDPOINT,
                  data=json.dumps({
                      'text': message,  # 投稿するテキスト
                      'username': u'me',  # 投稿のユーザー名
                      'icon_emoji': u':ghost:',  # 投稿のプロフィール画像に入れる絵文字
                      'link_names': 1,  # メンションを有効にする
                  }))
