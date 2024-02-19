from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post) # 管理画面上で見えるようにするためにモデルを登録
admin.site.register(Comment)
