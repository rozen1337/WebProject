from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import FeedbackForm, CommentForm, ArticleForm
from .models import Article, Comment


def home(request):
    return render(
        request,
        "app/index.html",
        {
            "title": "Главная",
            "year": datetime.now().year,
        },
    )


def links(request):
    return render(
        request,
        "app/links.html",
        {
            "title": "Полезные ресурсы",
            "year": datetime.now().year,
        },
    )


def feedback(request):
    gender = {"m": "Мужской", "f": "Женский"}
    data = None
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = dict()
            data["name"] = form.cleaned_data["name"]
            data["gender"] = gender[form.cleaned_data["gender"]]
            data["notice"] = form.cleaned_data["notice"]
            data["email"] = form.cleaned_data["email"]
            data["message"] = form.cleaned_data["message"]
    else:
        form = FeedbackForm()
    return render(
        request,
        "app/feedback.html",
        {
            "title": "Оставить отзыв",
            "year": datetime.now().year,
            "form": form,
            "data": data,
        },
    )


def about(request):
    return render(
        request,
        "app/about.html",
        {
            "title": "О сайте",
            "year": datetime.now().year,
        },
    )


def videopost(request):
    return render(
        request,
        "app/videopost.html",
        {
            "title": "Видео",
            "year": datetime.now().year,
        },
    )


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_active = True
            user.is_superuser = False
            user.date_joined = datetime.now()
            user.last_login = datetime.now()
            form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(
        request,
        "app/registration.html",
        {
            "title": "Регистрация",
            "year": datetime.now().year,
            "form": form,
        },
    )


def blog(request):
    posts = Article.objects.all()
    return render(
        request,
        "app/blog.html",
        {
            "title": "Блог",
            "posts": posts,
            "year": datetime.now().year,
        },
    )


def article(request, parametr):
    post = Article.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.date = datetime.now()
            comment.post = Article.objects.get(id=parametr)
            comment.save()
            return redirect("article", parametr=post.id)
    else:
        form = CommentForm()

    return render(
        request,
        "app/article.html",
        {
            "title": post.title,
            "post": post,
            "comments": comments,
            "form": form,
            "year": datetime.now().year,
        },
    )


def newpost(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.posted = datetime.now()
            article.save()
            return redirect("blog")
    else:
        form = ArticleForm()

    return render(
        request,
        "app/newpost.html",
        {
            "title": "Добавить статью блога",
            "articleForm": form,
            "year": datetime.now().year,
        },
    )
