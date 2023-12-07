from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),#Djangoの管理サイト用
    path("",include("diary.urls")),#diaryアプリケーション用,どのアプリの処理を要求しているか識別し、アプリケーションに渡す、第一引数"はhttp(s)://<ホスト名>/~にマッチング
    #include→アプリケーションのURLパターンをルートのurls.pyを管理するために必要
]
