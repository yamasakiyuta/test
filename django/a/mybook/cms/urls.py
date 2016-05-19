from django.conf.urls import url
from cms import views


urlpatterns = [
    #関数辞典タイトル
    url(r'^home/$', views.home, name='home'),   # 一覧
    # 書籍
    url(r'^book/$', views.book_list, name='book_list'),   # 一覧
    url(r'^book/add/$', views.book_edit, name='book_add'),  # 登録
    url(r'^book/mod/(?P<book_id>\d+)/$', views.book_edit, name='book_mod'),  # 修正
    url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name='book_del'),   # 削除

    url(r'^search/$', views.book_list2,name='book_list2'),
    url(r'^get/$', views.hello_get_query, name='hello_get_query'),
    # 感想
    url(r'^impression/(?P<book_id>\d+)/$', views.ImpressionList.as_view(), name='impression_list'),  # 一覧
    url(r'^impression/add/(?P<book_id>\d+)/$', views.impression_edit, name='impression_add'),  # 登録
    url(r'^impression/mod/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.impression_edit, name='impression_mod'),  # 修正
    url(r'^impression/del/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.impression_del, name='impression_del'),   # 削除url(r'^search/$', 'mybook.book.views.search'),
]

