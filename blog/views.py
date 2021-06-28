
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from blog.models import Blog,Category,Profile,Comment
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def home(request):
    categories = Category.objects.all()
    profile = Profile.objects.all()
    post = Blog.objects.all().order_by('date')[0:3]
    return render(request,'home.html',{'categories':categories,'profile':profile,'post':post})

def base(request):
    categories = Category.objects.all()
    post = Blog.objects.all().order_by('date')[0:3]
    return render(request,'base.html',{'categories':categories, 'post':post})


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Your BlogIN account has successfully created')
        return redirect('home')
    
    else:
        return HttpResponse('404 error occur')


def signin(request):
    if request.method=='POST':
        username1 = request.POST['username1']
        password1 = request.POST['password1']

        user = authenticate(username=username1, password=password1)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully logged in')
            return redirect('base')
        
        else:
            return HttpResponse('Incorrect Username or Password')
    
    else:
        return redirect('home')

def signout(request):
    logout(request)
    return redirect('home')

def blogadd(request):
    categories = Category.objects.all()
    if request.method=="POST":
        title = request.POST['title']
        post = request.POST['post']
        image = request.FILES["image"]
        category = request.POST.get("category")
        category_obj = Category.objects.get(name=category)
        blogs = Blog(title=title, post=post,image=image,category=category_obj)
        blogs.author = request.user
       
        blogs.save()

        messages.success(request,"your blog has been created")
        return redirect('base')
    
    else:
        return render(request,'blogadd.html',{'categories':categories})

def category(request):
    if request.method == "POST":
        name = request.POST['name']
        category_name = Category.objects.create(name=name)
        category_name.save()
        messages.success(request,"your category has been created")
        return redirect('base')
    else:
        return render(request,'category.html')


def post(request):
    post_list = Blog.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(post_list, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'post.html',{'posts':posts})


def fullpost(request, pk):
    posts = Blog.objects.get(id=pk)
    categories =Category.objects.all()
    profile = Profile.objects.get(writer=posts.author)
    blogs = Blog.objects.all().order_by('date')[0:5]
    if request.method=="POST":
        comment_text = request.POST["comment_text"]
        comments = Comment(comment_text=comment_text)
        comments.comment_by = request.user
        comments.comment_on_blog = posts
        comments.save()
        return redirect('base')

    return render(request, 'fullpost.html',{'posts':posts, 'profile':profile, 'categories':categories, 'blogs':blogs})


def search(request):
    if request.method == "GET":
        query = request.GET['query']
        queries = Blog.objects.filter(title__icontains=query)
        if queries.exists():
            return render(request,'search.html',{'queries':queries})
        else:
            return HttpResponse("No results")


def addprofile(request):
    profile= Profile.objects.all()
    if profile.filter(id=request.user.id).exists():
        return HttpResponse("your profile already exists")
    else:
        if request.method=="POST":
            about = request.POST['about']
            img = request.FILES['img']
            cover = request.FILES['cover']
            profile = Profile(about=about, img=img, cover=cover)
            profile.writer = request.user
            profile.id = request.user.id
            profile.save()
            return redirect('/base')

        else:
            return render(request,'addprofile.html')


def viewprofile(request):
    person = Profile.objects.all()
    if person.filter(id=request.user.id).exists():
        posts = Blog.objects.filter(author=request.user)
        profile = Profile.objects.get(writer = request.user)
        num_post = Blog.objects.filter(author=request.user).count()
        return render(request,'viewprofile.html',{'profile':profile, 'posts':posts,'num_post':num_post, 'person':person})
    else:
        return HttpResponse("Please add your profile first")

def filter_category(request,pk):
    category = Category.objects.get(id=pk)
    posts = Blog.objects.filter(category = category.id )
    return render(request, 'filter_category.html',{'category':category, 'posts':posts})

def editblog(request,id):
    posts = Blog.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        post=request.POST.get('post')
        image = request.FILES['image']
        posts.title = title
        posts.post=post
        posts.image=image
        posts.save()
        messages.success(request,'BLOG has been edited successfully')
        return redirect('base')
    return render(request,'editblog.html',{'posts':posts})

def deleteblog(request,id):
    posts = Blog.objects.get(id=id)
    posts.delete()
    return redirect('base')

def like(request, id):
    post = get_object_or_404(Blog, id=request.POST.get('post_id'))
    if post.like.filter(id=request.user.id).exists():
        messages.success(request,'You have already liked this post')
    else:
        post.like.add(request.user)
    return HttpResponseRedirect(reverse('fullpost',args=[str(id)]))

def dislike(request, id):
    post = get_object_or_404(Blog, id=request.POST.get('dislike'))
    if post.dislikes.filter(id=request.user.id).exists():
        messages.success(request,'You have already disliked this post')
    else:
        post.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('fullpost',args=[str(id)]))
    
def bloggers(request):
    profile_list = Profile.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(profile_list, 3)
    try:
        profile = paginator.page(page)
    except PageNotAnInteger:
        profile = paginator.page(1)
    except EmptyPage:
        profile = paginator.page(paginator.num_pages)
    return render(request,'bloggers.html',{'profile':profile})

def fullprofile(request,pk):
    profile = Profile.objects.get(id=pk)
    posts = Blog.objects.filter(author = profile.writer)
    num_post = Blog.objects.filter(author=profile.writer).count()
    user = User.objects.get(id=pk)
    return render(request,'fullprofile.html',{'profile':profile, 'posts':posts, 'user':user, 'num_post':num_post})

def editprofile(request,id):
    profile = Profile.objects.get(id=id)
    if request.method == 'POST':
        about=request.POST.get('about')
        img = request.FILES['img']
        cover = request.FILES['cover']
        profile.about = about
        profile.img=img
        profile.cover=cover
        profile.save()
        messages.success(request,'BLOG has been edited successfully')
        return redirect('base')
    
    return render(request,"editprofile.html",{'profile':profile})

def deleteprofile(request,id):
    profile = Profile.objects.get(id=id)
    profile.delete()
    return redirect('base')



    




    





        
           
        









