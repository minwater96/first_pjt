# Django

1. 프로젝트생성
```bash
django-admin startproject {pjt_name}
```

2. 가상환경 생성

```bash
python -m venv venv
```

3. 가상환경 활성화

```bash
source venv/bin/activate
```

4. 서버on (off: 'ctrl + c')
```bash
python manage.py runserver
```

5. 앱생성
```bash
django-admin startapp {app_name}
```

6. 앱등록 ('settings.py')
```python
INSTALLED_APPS = [
    ...
    '{app_name}'
]
```

