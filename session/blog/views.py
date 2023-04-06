from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from blog.forms import CommentForm


def home(request, user_name):
    try:
        user = User.objects.get(username=user_name)
        if request.method == "POST":
            if request.user.is_authenticated:
                logout(request)
                return redirect('home', user_name=user_name)
        blogs = Blog.objects.filter(author__username=user_name)
        if (user_name == request.user.username):
            is_Login = True
        else:
            is_Login = False
        return render(request, 'home.html', {'blogs': blogs, 'user_name': user_name, 'is_Login': is_Login})
    except User.DoesNotExist:
        # 유저가 존재하지 않는 경우 404 에러 발생
        raise Http404("User does not exist")

def detail(request, user_name, blog_id):
    user = get_object_or_404(User, username=user_name)
    blog = get_object_or_404(Blog, pk=blog_id, author__username=user_name)
    comments = blog.comments.all()

    if (user_name == request.user.username):
            is_Login = True
    else:
            is_Login = False

    if request.method == 'POST' and 'logout' in request.POST:
        # 로그아웃 처리
        logout(request)
        return redirect('home', user_name)

    elif request.method == 'POST':
        # 댓글 작성 처리
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog
            new_comment.author = request.user
            new_comment.save()
            return redirect('detail', user_name=user_name, blog_id=blog_id)

    else:
        comment_form = CommentForm()

    return render(request, 'detail.html', {'blog': blog, 'user_name': user_name, 'is_Login': is_Login, 'comments': comments, 'comment_form': comment_form})



@login_required
def new(request, user_name):
    if (user_name == request.user.username):
        is_Login = True
    else:
        is_Login = False
    return render(request, 'new.html', {'user_name': user_name, 'is_Login': is_Login})


@login_required
def create(request, user_name):
    if request.method == 'POST':
        if 'logout' in request.POST:  # 로그아웃 요청일 경우
            logout(request, user_name)
            # return redirect('home', user_name)

        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            return redirect('detail', user_name=user_name, blog_id=new_blog.id)
    else:
        form = BlogForm()

    return render(request, 'new.html', {'form': form, 'user_name': user_name})


@login_required
def edit(request, user_name, blog_id):
    user = get_object_or_404(User, username=user_name)
    edit_blog = get_object_or_404(Blog, pk=blog_id, author=user)
    return render(request, 'edit.html', {'edit_blog': edit_blog, 'user_name': user_name, 'blog_id': blog_id})


@login_required
def update(request, user_name, blog_id):
    user = get_object_or_404(User, username=user_name)
    old_blog = get_object_or_404(Blog, pk=blog_id, author=user)
    form = BlogForm(request.POST, instance=old_blog)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.save()
        return redirect('detail', user_name=user_name, blog_id=old_blog.id)
    return render(request, 'new.html')


@login_required
def delete(request, user_name, blog_id):
    user = get_object_or_404(User, username=user_name)
    delete_blog = get_object_or_404(Blog, pk=blog_id, author=user)
    delete_blog.delete()
    return redirect('home', user_name=user_name)


def blog_search(request, user_name):
    user = get_object_or_404(User, username=user_name)
    blogs = Blog.objects.filter(author__username=user_name)
    query = request.GET.get('query')
    if query:
        blogs = blogs.filter(title__icontains=query)
    else:
        blogs = []
    if (user_name == request.user.username):
        is_Login = True
    else:
        is_Login = False
    context = {
        'blogs': blogs,
        'user_name': user_name,
        'query': query,
        'is_Login': is_Login
    }
    return render(request, 'home.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home', user_name=user.username)
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_v(request):
    form = AuthenticationForm()
    # if request.user.is_authenticated:
    #     return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home', user_name=request.user.username)
    return render(request, 'login.html', {'form': form})

def logout_v(request):
    user_name = request.user.username
    print(user_name)
    if request.method == 'POST':
        logout(request)
        print("slba")
        return redirect('home', user_name)
    return render(request, 'logout.html')