
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
$ pipenv install
$ pipenv install django-widgets-improved
$ pipenv shell
$ cd ShiftSwitch
$ python manage.py makemigrations
$ python manage.py migrate
```



#### 実行

```shell
$ python manage.py runserver
```

#### ユーザー作成(管理者)

```shell
$ python manage.py createsuperuser
```





