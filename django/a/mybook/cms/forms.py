from django.forms import ModelForm
from django import forms
from cms.models import Book,Impression


class BookForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Book
        fields = ('func_name', 'program_name', 'tag','author','Github','test',)


class ImpressionForm(ModelForm):
    """感想のフォーム"""
    class Meta:
        model = Impression
        fields = ('comment', )

class BookSearchForm(forms.Form):
   func1 = forms.CharField(min_length=2, max_length=100)

class SearchForm(forms.Form):
    q = forms.CharField(label="キーワード")

class ArticleSearchForm(forms.Form):
    word = forms.CharField()



