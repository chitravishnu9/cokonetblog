from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.forms import ModelForm

from app.form import RegistrationForm
from app.models import blog


# Create your views here.
def home(request):
    return render(request,"home.html")

def main(request):
    if request.method == 'POST':
        topic = request.POST['topic']
        title = request.POST['title']
        img = request.FILES['img']
        desc = request.POST['content']
        data = blog.objects.create(topic=topic, title=title, img=img, desc=desc)
        data.save()
        return redirect(view)


    return render(request,"main.html")

def view(request):
    data = blog.objects.all()
    return render(request,"view.html",{'data':data})

def base(request):
    return render(request,"base.html")


def delete(request,id):

     data=blog.objects.get(id=id)
     data.delete()

     return redirect(view)


def edit(request, id):
    data = blog.objects.get(id=id)
    return render(request,'edit.html',{'data':data})


def update(request, id):
    data = blog.objects.get(id=id)
    data.topic = request.POST['topic']
    data.title = request.POST['title']
    data.img = request.FILES['img']
    data.desc = request.POST['content']
    data.save()
    return redirect(view)




def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)


    return render(request,'register.html',{'form':form})

#def user_login(request):
 #   if request.method=='POST':
 #       username=request.POST['username']
 #       password = request.POST['password']
 #       user=authenticate(username=username,password=password)
 #       if user is not None:
 #       else:
 #           return redirect(user_login)
 #           return HttpResponse('<h1>Invalid username and password</h1>')

 #   return render(request,'login.html')

