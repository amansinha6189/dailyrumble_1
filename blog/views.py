from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Blog
from blog.models import BlogComment
from blog.models import Contact
from blog.models import About
from blog.models import Tag
from blog.models import FrontPage
from blog.models import SocialContact
from blog.templatetags import extras

# Create your views here.
def home(request):
    texts = FrontPage.objects.all()
    params = {'texts':texts}
    return render(request, "home.html", params)
    
def about(request):
    abouts = About.objects.all()
    data2 = {'abouts':abouts}
    return render(request, "about.html", data2)
    

def blog(request):
    blogs = Blog.objects.all().order_by('-pk')
    context = {'blogs': blogs}
    return render(request, "blog.html", context)

def contact(request):
    socialContacts = SocialContact.objects.all()
    params1 = {'socialContacts':socialContacts}



    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        # is_private = request.POST['is_private']
        # print(name, email, content)
        if len(name)<2 or len(email)<3 or len(content)<3:
            messages.error(request,"Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, content= content)
            contact.save()
            messages.success(request,"your message has been successfully sent")
    
    return render(request, "contact.html", params1)



def search(request):
    query = request.GET['query']
    blogsTitle = Blog.objects.filter(title__icontains=query)
    blogsContent = Blog.objects.filter(content__icontains=query)
    blogs = blogsTitle.union(blogsContent)

    data1 = {'blogs': blogs, 'query':query}
    return render(request, "search.html", data1)


def tag(request):
    tags = Tag.objects.all()
    print(tags)
    data3 = {'tags':tags}
    return render(request, "base.html", data3)

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(blog=blog, parent = None)
    replies= BlogComment.objects.filter(blog=blog).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'blog':blog, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blogpost.html", context)

def blogComment(request):
    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        blogSno = request.POST.get("blogSno")
        blog = Blog.objects.get(sno=blogSno)
        parentSno= request.POST.get('parentSno')
        
        
        
        if parentSno == None:
            comment=BlogComment(comment= comment, user=user, blog=blog)
            comment.save()
              
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, blog=blog , parent=parent)
            comment.save()
            
        

        
    return redirect(f"/blog/blogpost/{blog.slug}")


def handleSignup(request):
    if request.method=="POST":
        # get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        #check for errorneous inputs
        userCheck = User.objects.filter(username=username)

        if userCheck:
            messages.error(request, "Username Already taken")
            return redirect('/')

        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"your account has been successfully created")
        return redirect('/')
    else:
        HttpResponse('404-not found')

def user_login(request):
    if request.method=="POST":
        user_name = request.POST.get('username', ' ')
        user_password = request.POST.get('password', ' ')
        
        #if user account exist or not
        user =  authenticate(username=user_name, password=user_password)

        if user is not None:
            login(request, user)
            messages.success(request, "logged in")
            return redirect('/')
        else:
            messages.error(request, "invalid credentials")
            return redirect('/')


def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect("/")