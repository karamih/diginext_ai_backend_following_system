<h1> Following system </h1>

<p>for attending in diginext startup bootcamp, we should submit some tasks, one of those is implementing a following system with arbitary language and framework, so this is <b>django</b>.</p> 
<br>
<h3>Django Rest-Framework</h3>
<hr>
<p>this sample is based on DRF, used postgres as database.<br>so this is what they want to implement in this task:</p>
<p>

1- یک لیست از کاربرها همراه با دنبال‌کنندگان و دنبال‌شوندگان هر کاربر.

2- یک API برای دنبال‌کردن.

3- یک API برای لغو دنبال‌کردن.

4- یک API که تعداد دنبال‌کنندگان هر کاربر را به شکل روزانه نشان دهد.

5- یک API که دنبال کنندگان مشترک دو کاربر را نشان دهد.

</p>
<hr>
<h3>Deployed on Liara</h3>
<p>project is deployed on liara you can check it:</p>

[liara](https://suspicious-raman-jxkk6yjch.liara.run/)

* debug set into True, you can explore.
* consider for a while time will be on server so when you come to try may not be on server anymore.

<hr>

<h3>Test on Local</h3>

<p>you have to do some steps:</p>

* <h5>clone/download project

```cmd
git clone https://github.com/karamih/diginext_ai_backend_following_system.git
```

* <h5>create an environment like venv:

```cmd
python -m venv venv
```

* <h5>active environment:

```cmd
venv\Scripts\activate  
```

* <h5>install packages:

```cmd
pip install -r requirements.txt
```

* <h5>create supreuser:

```cmd
python manage.py createsuperuser 
```

* <h5>run server:

```cmd
python manage.py runserver 
```

<br>

<h4>attention before running you should config database:</h4>

* create your own database and replace your config with settings.py file:

```python
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': 'diginext',
        'USER': 'postgres',
        'PASSWORD': 'Pg123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

* migrate models:

```cmd
    python manage.py migrate 
```

<h5>now you could run in local successfully.</h5>

***

<h3>API's</h3>
<p>in the project there is postman file that contains all api's (urls and examples)<br>
test them!.</p>

```
diginext_backend.postman_collection.json
```