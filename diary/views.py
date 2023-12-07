from django.shortcuts import render#HTMLテンプレートを使用してwebページを生成し、クライアントに返す際に使われる
from django.views import generic#genericモジュールのimport→djangoのビューのクラスを拡張する

class IndexView(generic.TemplateView):#IndexViewクラスの作成→diary/urls.pyの第2引数にあたるものモジュールgeneric.TemplateVuewクラスを継承、Tenplateview→テンプレートを用いた静的なページを表示するのに向いている
    template_name = "index.html"#ビュークラス内で指定されるHTMLテンプレートファイルの指定