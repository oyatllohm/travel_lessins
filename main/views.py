from django.shortcuts import render
from django.views import View

# Create your views here.
from .models import  Deration , News ,Cantact
from django.http import JsonResponse
from django.contrib import messages


def cange_lane(request):
    lang = request.GET['currect_lang']
    
    if lang in ['en','uz','ru']:
        request.session['lang'] = lang
    return JsonResponse({'status':200})



class HomePageView(View):
    def get(self,request):
        destination = Deration.objects.all()
        news_ = News.objects.all()
        context ={
            'destination':destination,
            'news_':news_,
        }
        return render(request,'index.html',context)




class AboutView(View):
    def get(self,request):
        return render(request,'about.html')



class NewsView(View):
    def get(self,request):
        news__ = News.objects.all()
        context ={
           
            'news__':news__,
        }
        return render(request,'news.html',context)
    
class ContactView(View):


    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c = Cantact.objects.create(name=name,email=email,subject= subject,text=message)

        if name and email and subject and message:
            context = {'m': 'siznin izohingiz qabul qilindi '}
        else:
            context = {}

        return render(request, 'contact.html',context)

    def get(self, request):
        return render(request, 'contact.html')
def main():
    pass