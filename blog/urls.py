from django.urls import path
from . import views #доступны все функции с файла views.py


urlpatterns = [
    path('home/', views.main_site, name='main_site'), 
    path('economic/',views.economic_info, name='economic_info'),#www.google.com/economic
    path('document/',views.doc_info,name='doc_info'),
    path('contact/',views.contact_info,name='contact'),
    
    #GET второй шаг
    path('test_page_HttpResponse/',views.test_GET_HttpResponse,name='test_page_HttpResponse'),# единичкная функция 
    path('test_page_render/',views.test_GET_render,name='test_page_render'),#работа с целой страницей 
]

