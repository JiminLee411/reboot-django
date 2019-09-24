# REVIEW

* 가상환경 만들기

  ```bash
  $ python -m venv venv
  ```

* 가상환경 실행

  ```bash
  $ source venv/Scripts/activate
  ```

* django 설치

  ```bash
  $ git init
  $ pip install django
  ```

* git  설정

  ```bash
  $ git init
  $ touch .gitignore
  $ pip freeze > requirements.txt
  ```
  
* django 프로젝트 생성

  ```bash
  $ django-admin startproject reboot .
  ```

* 서버 실행

  ```bash
  $ python manage.py runserver
  ```

* app 생성

  ```bash
  $ python manage.py startapp articles
  ```

* app 생성 후, 설정

  * `reboot/settings`

    ```python
    INSTALLED_APPS = [
        'articles',
        ...,
    ]
    ```

  * `reboot/urls`

    ```python
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', include('articles.urls')),
    ]
    ```

  * `articels/urls`

    ```python
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', views.index),
    ]
    ```

  * `articels/views`

    ```python
    from django.shortcuts import render
    
    # Create your views here.
    def index(request):
        return render(request, 'articles/index.html')
    ```

  * `templates`



# Django

## Model 정의

* title : charfield
* content : textfield
* created_at : auto_now_add, datetimefield
* updated_at : auto_now, datetimefield



## CRUD

* C
  * `/new/` : 글 작성 form
  * `/create/` : 저장 후 index로 보내기(redirect)
* R
  * `/1/` : `detail` 함수에서 처리
* D
  * `/1/delete/` : 삭제 후 index로 보내기
* U
  * `/1/edit/` : 글 수정 form
  * `/1/update/`  : 저장 후 Read로 보내기