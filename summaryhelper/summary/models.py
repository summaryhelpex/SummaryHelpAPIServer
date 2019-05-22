from django.db import models

# Create your models here.

class Article(models.Model) :
    article_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.article_text
    def get_articletext(self):
        return article_text

class Summary(models.Model) :
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    summary_text = models.TextField()
    star = models.IntegerField(default=0)
    
    textrancres=[]
    def __str__(self):
        return self.summary_text
    def __init__(self,Article):
        article=Article



