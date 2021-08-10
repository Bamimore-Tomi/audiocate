from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from . models import Book, Genre,Explore,Bookmark,UserProfile,Featured
from django.contrib.auth.models import User
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
from gtts import gTTS
# will convert the image to text string
import pytesseract
from pdfminer.high_level import extract_text
from PIL import Image
import io
 # converts the text to speech
import pyttsx3
# Create your views here.

pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

def index(request):
    return render(request,"homepage.html")


def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        if User.objects.get(email=email):
            username=User.objects.get(email=email).username
        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("APP:dashboard")
        else:
            context={"message": "invalid login details"}
            return render(request,'index.html',context)
    else:
        return render(request,"index.html")

def convert(request):
    context={}
    if request.method == "POST":
        file=request.FILES.get("file")
        filename = str(file)
        rename=request.POST.get("name")
        name=rename+".mp3"
        link="media/"+name
        voice=request.POST.get("voice")
        if os.path.splitext(filename)[1] in [".jpg",".jpeg",".png"]:
            img = Image.open(file)
            # converts the image to result and saves it into result variable
            result = pytesseract.image_to_string(img)
            # write text in a text file and save it to source path
            myAudio = gTTS(text=result, lang=voice, slow=False)
            #Save as mp3 file
            myAudio.save(os.path.join("media",name))
            book=Book.objects.create(name=name,link=link,user=request.user)
            book.save()
            context={"message":"audio file successfully generated","finish":"true","link":link,"item":Book.objects.get(name=name,user=request.user)}
            return render(request,"examples/convert.html",context)
        elif os.path.splitext(filename)[1] in [".pdf"]:
            text = extract_text(file)
            new_text=text.replace("(cid:10)","")
            #Call GTTS
            try:
                if Book.objects.filter(link=link):
                    context={"message":"file already saved"}
                    return render(request,"examples/convert.html",context)
                else:
                    myAudio = gTTS(text=new_text, lang=voice, slow=False)
                    myAudio.save(os.path.join("media",name))
                    book=Book.objects.create(name=name,link=link,user=request.user)
                    book.save()
                    context={"message":"audio file successfully generated","finish":"true","link":link,"name":name}
            except:
                context={"message":"audio file successfully generated","finish":"true","link":link,"name":name}
                return render(request,"examples/convert.html",context)
            return render(request,"examples/convert.html",context)
        elif request.POST.get("publish")=="true":
            name=request.POST.get("name")
            link=request.POST.get("link")
            voice=request.POST.get("voice")
            explore=Explore.objects.create(name=name,link=link,voice=voice)
            explore.save()
            context={"message":"file published"}
            return render(request,"examples/convert.html",context)
        else:
            context={"message":"this file is not allowed"}
            return render(request,"examples/convert.html",context)
    else:
        return render(request,"examples/convert.html")

def register(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        if password1 == password2:
            if User.objects.filter(username=name):
                context={"message":"username already taken"}
                return render(request,"register.html",context)
            else:
                user=User.objects.create(username=name,email=email,password=password1)
                context={"message":"user created"}
                return render(request,"register.html",context)
        else:
            context={"message":"passwords dont match"}
            return render(request,"register.html",context)
    return render(request,"register.html")

def dashboard(request):
    return render(request,"dashboard.html")

def mybooks(request):
    context={"mybooks":Book.objects.filter(user=request.user)}
    return render(request,"examples/mybooks.html",context)

def genre(request):
    context={"genre":Genre.objects.all()}
    return render(request,"examples/genre.html",context)

def explore(request):
    if request.GET.get("favorite")=="true":
        name=request.POST.get("name")
        link=request.POST.get("link")
        if Bookmark.objects.filter(user=request.user,name=name):
            pass
        else:
            bookmark=Bookmark.objects.create()
            bookmark.save()
    context={"explore":Explore.objects.all().order_by("-date")}
    return render(request,"examples/explore.html",context)

def genre_all(request):
    if request.GET.get("genre"):
        name=request.GET.get("genre")
        context={"genre":Genre.objects.get(name=name)}
        return render(request,"examples/genre-all.html",context)
    else:
        return render(request,"examples/genre-all.html")

def logout(request):
    auth.logout(request)
    return redirect("index.html")


def settings(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        image=request.FILES.get("image")
        if UserProfile.objects.filter(user=request.user):
            profile=UserProfile.objects.get(user=request.user)
            if image:
                profile.image=image
            else:
                pass
            user=User.objects.get(username=username)
            if email:
                user.email=email
            else:
                pass
            if first_name:
                user.first_name=first_name
            else:
                pass
            if last_name:
                user.last_name=last_name
            else:
                pass
            profile.save()
            user.save()
        else:
            user=User.objects.get(username=username)
            if email:
                user.email=email
            else:
                pass
            if first_name:
                user.first_name=first_name
            else:
                pass
            if last_name:
                user.last_name=last_name
            else:
                pass
            user.save()
            profile=UserProfile.objects.create(user=request.user,image=image)
            profile.save()
    return render(request,"settings.html")

def contribute(request):
    if request.method=="POST":
        name=request.POST.get("name")
        authors_image=request.FILES.get("authors_image")
        authors_email=request.POST.get("email")
        cover_image=request.POST.get("cover_image")
        title=request.POST.get("title")
        summary=request.POST.get("summary")
        audio=request.FILES.get("audio")
        link=request.POST.get("link")
        featured=Featured.objects.create(name=name,authors_image=authors_image,authors_email=authors_email,cover_image=cover_image,title=title,summary=summary,audio=audio,link=link)
        featured.save()
        context={"message":"Your book has been submitted and will be reviewd in 2 to 3 working days. Keep an eye on the email you submitted"}
        return render(request,"examples/contribute.html",context)
    else:
        return render(request,"examples/contribute.html")

def featured(request):
    if request.GET.get("favorite")=="true":
        name=request.POST.get("name")
        link=request.POST.get("link")
        if Bookmark.objects.filter(user=request.user,name=name):
            pass
        else:
            bookmark=Bookmark.objects.create()
            bookmark.save()
    context={"featured":Featured.objects.all()}
    return render(request,"examples/featured.html",context)
