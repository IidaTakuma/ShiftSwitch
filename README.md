
# ShiftSwitch

#### 使用用途

アルバイトのシフト交換・管理をサポートするツールです。



#### 使用環境

Python 3.7.2

Django 2.2

pipenv



#### セットアップ

```shell
$ git clone https://github.com/IidaTakuma/ShiftSwitch.git
$ cd ShiftSwitch
$ cp .env.sample .env
# 必要な情報を.envに入力
$ pipenv install
$ pipenv install django-widgets-improved
$ pipenv run python manage.py makemigrations
$ pipenv run python manage.py migrate
```


#### 実行

```shell
$ pipenv run python manage.py runserver
```

#### ユーザー作成(管理者)

```shell
$ pipenv run python manage.py createsuperuser
```





