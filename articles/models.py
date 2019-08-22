from django.db import models


# 1. python manage.py makemigrations => django에게 model 작성했음을 알림
# 2. python manage.py migrate => django에게 실제 DB에 작성하라고 명령(실제 DB 반영)


# django model을 상속받는다
class Article(models.Model):
    # id = models.AutoField(primary_key=True)
    # id(pk)는 기본적으로 처음 테이블이 생성될 때 자동으로 만들어짐
    # 즉, id를 따로 작성할 필요가 없음
    # 게시판이 하나씩 생길때마다 1,2,3,... 이렇게 번호 생성됨

    # 모든 필드는 기본적으로 NOT NULL => 비어있으면 안 된다
    
    # CharField 에서는 max_length가 필수 인자(길이를 반드시 지정해야 함)
    title = models.CharField(max_length=20)  # 클래스변수(DB의 필드)
    content = models.TextField()  # 클래스 변수(DB의 필드) CharField 와 다른건 textfield는 max_length 설정할 필요없이 쓸 수 있다
    # 자동으로 지금 추가됐을 때만, 해당 시간을 추가해줘
    created_at = models.DateTimeField(auto_now_add=True)
    # 자동으로 현재 시간을 언제든지
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번 글 - {self.title} : {self.content}'