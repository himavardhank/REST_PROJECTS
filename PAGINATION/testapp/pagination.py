from rest_framework.pagination import PageNumberPagination
class Mypagination(PageNumberPagination):
    page_size=5
    page_query_param='mypage'
    page_size_query_param='num'
    max_page_size=11
    last_page_strings=('end_page',)
from rest_framework.pagination import LimitOffsetPagination
class Mypagination2(LimitOffsetPagination):
    default_limit=5
    limit_query_param='mylimit'
    offset_query_param='myoffset'
    max_limit=20
from rest_framework.pagination import CursorPagination
class Mypagination3(CursorPagination):
    ordering='esal'
    page_size=5
    cursor_query_param='mycursor'
