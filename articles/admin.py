from django.contrib import admin
# 동일한 model에서 Article을 가져오겠다
from .models import Article

# Register your models here.
# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at',)
