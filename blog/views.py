from django.shortcuts import render
from django.http import HttpResponse # нужно для HttpResponse
from django.utils import timezone
from .models import Post # работа с бд и с шаблонами базы данных 

# Create your views here.

def main_site(request):   
    return render(request,'main_site/index.html',{})

def doc_info(request):
    return render(request,'doc_info/index.html',{}) # ввывод сайта на страничке

def economic_info(request):
    return render(request,'economic_info/index.html',{})

def contact_info(request):
    return render(request,'contact_info/index.html',{}) 


#Третий шаг 
def test_GET_HttpResponse(request):               
    msg=request.GET['message_contact_HttpResponse']# перехват get 
    return HttpResponse(msg)                       # возращение значения(вывод страничкм)


def test_GET_render(request):
    msg=request.GET['message_contact_render'] # перехват get
    word = len(msg.split())                   # длина слов
    return render(request,'test_page/index.html',{'word':word,'msg':msg}) #вывод странички и передача значений на страничку 


