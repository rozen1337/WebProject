from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Comment, Article


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            {"class": "form-control", "placeholder": "Имя пользователя"}
        ),
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput({"class": "form-control", "placeholder": "Пароль"}),
    )


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Ваше имя",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        min_length=2,
        max_length=100,
    )
    gender = forms.ChoiceField(
        label="Ваш пол",
        choices=(("m", "Мужской"), ("f", "Женский")),
        widget=forms.RadioSelect,
    )
    notice = forms.BooleanField(label="Получать новости на e-mail", required=False)
    email = forms.EmailField(
        label="Ваш e-mail",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        min_length=7,
    )
    message = forms.CharField(
        label="Ваши предложения по улучшению сайта",
        widget=forms.Textarea(attrs={"rows": 8, "cols": 20, "class": "form-control"}),
        required=False,
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"class": "form-control"})}


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            "title",
            "description",
            "content",
            "image",
        )
        labels = {
            "title": "Заголовок",
            "description": "Краткое содержание",
            "content": "Полное содержание",
            "image": "Картинка",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }