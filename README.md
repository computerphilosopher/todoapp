# Django TODO 

## 개요

![capture]([./readme_image/capture.JPG])

TODO 리스트의 조회, 수정, 삭제가 가능한 프로젝트입니다. 

데모 사이트: http://beomsupark.pythonanywhere.com/

## 빌드 방법 (리눅스 기준)

리눅스에서 서버를 직접 테스트 해 보고 싶다면 다음의 과정을 따릅니다.

### 1. 저장소 클론

git 명령어를 입력해 저장소를 클론합니다. 

```
git clone https://github.com/computerphilosopher/todoapp.git
```

### 2. virtualenv 설정

다음과 같은 환경으로 virtualenv를 설정합니다.

* python~=3.7
* django~=2.2

### 3. secrets.json 생성

manage.py가 있는 프로젝트 디렉토리에 secrets.json 파일을 생성합니다.

https://www.miniwebtool.com/django-secret-key-generator/ 에서 비밀 키를 작성해 json 파일에 다음과 같이 입력합니다.

secrets.json (... 부분에는 생성된 비밀 키를 넣으세요.)
```
{

  "SECRET_KEY": "..."
}
```

### 4. 서버 기본 설정

```
$ python3 manage.py collectstatic
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py createsuperuser

```

### 5. 구동 확인 

$ python3 manage.py runserver