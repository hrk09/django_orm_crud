# Django ORM



## Create

#### 기초설정

- Shell

  ```bash
  $ python manage.py shell
  ```

  

- import model

  ```python
  from articles.models import Article
  ```



#### 데이터를 저장하는 3가지 방법

1. 첫 번째 방식

   - ORM 쓰는 이유? 

     - DB를 조작하는 것을 객체지향 프로그래밍(클래스) 처럼 하기 위해서

     ```python
     article = Article()
     article # <Article: Article object (None)>
     article.title = 'First article'
     article.content = 'Hello  article?'
     
     article.title  # 'First article'
     article.content  # 'Hello  article?'
     article.save()
     article  # <Article: Article object (1)>
     ```

2. 두 번째 방식

   - 함수에서 keyword 인자 넘기기 방식과 동일

     ```python
     article = Article(title='Second article', content='hihi')
     article.save()
     article
     <Article: Article object (2)>
     ```

3. 세 번째 방식

   - `create()`를 사용하면 쿼리셋 객체를 생성하고 저장하는 로직이 한번의 스텝 

     ```python
     Article.objects.create(title='Third', content='Django! good')
     <Article: Article object (3)>
     ```

4. 검증

   `full_clean()` 함수를 통해 저장하기 전 데이터 검증을 할 수 있음

   ```python
   >>> article = Article()
   >>> article.title = 'Python is good'
   >>> article.full_clean()
   Traceback (most recent call last):
     File "<console>", line 1, in <module>
     File "C:\Users\student\development\django\django_orm_crud\venv\lib\site-packages\django\db\models\base.py", line 1203, in full_clean
       raise ValidationError(errors)
   django.core.exceptions.ValidationError: {'content': ['이 필드는 빈
   칸으로 둘 수 없습니다.']}
   ```

---



## READ


- 객체표현변경

  ```python
  # articles/model.py
  
  class Article(models.Model):
  
      def __str__(self):
          return f'{self.id}번 글 - {self.title} : {self.content}'
  ```

  

- 모든 객체

  ```python
  >>> Article.objects.all()
  <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>, <Article: Article object (4)>]>
  ```



- DB에 저장된 글 중에서 title 이 `Second article` 인  글만 가져오기

  ```python
  >>> Article.objects.filter(title='Second article')
  <QuerySet [<Article: 2번 글 - Second article : hihi>]>
  ```

  

- DB에 저장된 글 중에서 title 이 `Second article` 인 글 첫 번째 꺼만 가져오기

  ```python
  querySet = Article.objects.filter(title='Second article')
  >>> querySet
  <QuerySet [<Article: 2번 글 - Second article : hihi>, <Article: 5번
  글 - Second article : content>]>
  
  >>> querySet.first()
  <Article: 2번 글 - Second article : hihi>
  ---
  Article.objects.filter(title='Second article').first()
  <Article: 2번 글 - Second article : hihi>
  ```

  

- DB에 저장된 글 중에서 PK가 1인 글만 가져오기(여기서 pk는 id)

  - `pk만 get()으로 가지고 올 수 있다`(get은 무조건 pk만 가져온다고 생각하면 된다)

  ```python
  # id(pk)가 1인 것 가져오기
  >>> Article.objects.get(pk=1)
  <Article: 1번 글 - First article : Hello  article?>
  ```

  

- 오름차순

  ```python
  >>> articles = Article.objects.order_by('pk')
  >>> articles
  <QuerySet [<Article: 1번 글 - First article : Hello  article?>, <Article: 2번 글 - Second article : hihi>, <Article: 3번 글 - Third : Django! good>, <Article: 4번 글 - title : >, <Article: 5번 글 - Second article : content>]>
  ```

  

- 내림차순

  ```python
  >>> articles = Article.objects.order_by('-pk')
  >>> articles
  <QuerySet [<Article: 5번 글 - Second article : content>, <Article: 4번 글 - title : >, <Article: 3번 글 - Third : Django! good>, <Article: 2번 글 - Second article : hihi>, <Article: 1번 글 - First article : Hello  article?>]>
  ```

  

- 인덱스 접근이 가능하다

  ```python
  >>> article = articles[2]
  >>> article
  <Article: 3번 글 - Third : Django! good>
          
  ---
  >>> articles = Article.objects.all()[1:3]
  >>> articles
  <QuerySet [<Article: 2번 글 - Second article : hihi>, <Article: 3번
  글 - Third : Django! good>]>
  ```

  

- LIKE - 문자열을 포함하고 있는 값을 가져옴

  - 장고 ORM은 이름(title)과 필터(contains)를 더블 언더스코어(__)로 구분함
  - 검색구현에 활용할 수 있음

  ```python
  >>> articles = Article.objects.filter(title__contains='Sec')
  >>> articles
  <QuerySet [<Article: 2번 글 - Second article : hihi>, <Article: 5번
  글 - Second article : content>]>
  ```



- startswith

  ```python
  >>> articles = Article.objects.filter(title__startswith='first')
  >>> articles
  <QuerySet [<Article: 1번 글 - First article : Hello  article?>]>
  ```

  

- endswith

  ```python
  >>> articles = Article.objects.filter(content__endswith='good')
  >>> articles
  <QuerySet [<Article: 3번 글 - Third : Django! good>]>
  ```

  

## Delete

article 인스턴스 호출 후, `.delete()` 함수를 실행함

```python
>>> article = Article.objects.get(pk=1)
>>> article.content
'Hello  article?'
>>> article
<Article: 1번 글 - First article : Hello  article?>
>>> article.delete()
(1, {'articles.Article': 1})
```



## Update

article 인스턴스 호출 후, 값 변경하여 `.save()` 함수 실행함

```python
# pk가 4인 값이 비었는 지 확인하고 새로운 값을 넣어줌

>>> article = Article.objects.get(pk=4)
>>> article.content
''
>>> article.content = 'new contents'
>>> article.save()
```

