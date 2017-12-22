from django.forms import ModelForm

from django.db import models
#from cms.models import Book, Impression

# Create your models here.

class Book(models.Model):
    """書籍"""
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255)
    page = models.IntegerField('ページ数', blank=True, default=0)

    def __str__(self):
        return self.name

class Impression(models.Model):
    """感想"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='書籍', related_name='impressions')
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return seld.comment

class ImpressionForm(ModelForm):
    """感想のフォーム"""
    class Meta:
        model = Impression
        fields = ('comment', )