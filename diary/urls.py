from django.urls import path#Djangoのpath関数のimport→URLパターンを定義するために使用

from . import views#viewモジュールのimport→urls.pyで定義されるURLパターンがviewsモジュール内の関数やクラスと結びつけることができる

app_name = "diary"#diaryアプリケーションのルーティングに名前を付ける→ほかのアプリケーションで同じ名前のルーティング設定があってっも識別できるようにするため
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),#第一引数"はprivate_diary/urls.pyで設定したものと同じ物を指定"はトップページを指定（アプリぇーしょん）、第2引数→views.pyのIndex.Viewクラスをビューに指定、.as_view()でクラスから関数のビューに指定に変換と結びつける、第3引数→ルーティング処理を識別するための名前（tag名のようなもの）
    #name="index"→テンプレートで{% url "diary:index" %}のように指定することができる
]#プロジェクト（private_diary/urls.py)のルーティング処理から、アプリ側(diary/urls.py)のルーティング処理でURLパターンとトップページ用のViewを結びつける