from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from . import forms, models


def all_articles(request):
    articles = models.Article.objects.all()
    context = {
        "articles": articles,
    }

    return render(request, "all_articles.html", {"context": context})


def all_reviews(request):
    reviews = models.Review.objects.all()
    context = {
        "reviews": reviews,
    }

    return render(request, "all_reviews.html", {"context": context})


def article_detail(request, article_id):
    if request.method == "POST":
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            article = get_object_or_404(models.Article, id=article_id)
            models.Review.objects.create(text=text, article=article)
            return redirect(reverse("article", args=[article_id]))
    elif request.method == "GET":
        form = forms.ReviewForm()
        article = get_object_or_404(models.Article, id=article_id)
        reviews = models.Review.objects.filter(article=article_id)
        context = {
            "form": form,
            "article": article,
            "reviews": reviews,
        }
        return render(request, "article.html", {"context": context})


def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("all_articles"))
            else:
                raise PermissionDenied
    elif request.method == "GET":
        form = forms.LoginForm()
        context = {
            "form": form,
        }
        return render(request, "login.html", {"context": context})


def logout_view(request):
    logout(request)
    return redirect(reverse("all_books"))
