"""
To reder the html webpages
"""

## 1. Way to return a response --> Through HttpResponse methor
from django.http import HttpResponse
from matplotlib.style import context
from articles.models import Article
from django.template.loader import render_to_string

import random

##################################################
#### Custom Response
name = 'Piyush'
name2 = 'Samu'

HTML_STRING_HARDCODED = """
<h1>Hello {}, {}!</hname1>
""".format(name, name2)

##################################################
#### Getting data from the model (--databases)
num = random.randint(1, 4)
article_obj = Article.objects.get(id = num)

HTML_STRING_DB = f"""
<h1>Article-({article_obj.id}), {article_obj.title}</h1>
<p>{article_obj.content}</p>
"""

##################################################
#### Templates rendering
context = {
    'id': article_obj.id,
    'title': article_obj.title,
    'content': article_obj.content,
}
HTML_STRING_TEMP = render_to_string('home-view.html', context = context)


def home_view(req): 
    """
    Take in: req --> Send by django
    Return: res --> We return the response
    """
    print('Request is here: ', req)
    print(article_obj.id)
    return HttpResponse(HTML_STRING_TEMP)