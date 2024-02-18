from django.contrib import admin
from .models import Post

admin.site.register(Post) # 管理画面上で見えるようにするためにモデルを登録

