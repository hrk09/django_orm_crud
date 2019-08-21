from django.db import models

# Create your models here.


# django model을 상속받는다
class Article(models.Model):
    # id = models.AutoField(primary_key=True)
    # id(pk)는 기본적으로 처음 테이블이 생성될 때 자동으로 만들어짐
    # 즉, id를 따로 작성할 필요가 없음
    # 게시판이 하나씩 생길때마다 1,2,3,... 이렇게 번호 생성됨
    
    # CharField 에서는 max_length가 필수 인자(길이를 반드시 지정해야 함)
    title = models.CharField(max_length=20)  # 클래스변수(DB의 필드)
    content = models.TextField()  # 클래스 변수(DB의 필드)
    created_at = models.DateTimeField(auto_now_add=True)
    # 자동으로 지금 추가됐을 때, 해당 시간을 추가해줘