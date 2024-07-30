CRUD >>>>

c>> insert record 
R>> read record
U>> update 
D>> delete

****************************************

1 >>> virtualenv env
2 >>> env\Scripts\activate
3 >>> pip install django

4 >>> django-admin startproject message
5 >>> cd message
6 >>> python manage.py startapp messageapp
7 >>> python manage.py runserver

*****************************************
connect to database >>>> 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'message',
        'HOST':'localhost',
        'USER':'root',
        'PASSWORD':'',
        'PORT':'3306'
    }
}

command >>>
 
python manage.py makemigrations
python manage.py migrate


(ORM)>> object relational mapping ..
insert > m = Msg.object.create(fname=f_name,lname=l_name,mobile=m_num,email=e_mail)
        m.save()

