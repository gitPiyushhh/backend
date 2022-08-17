from django.http import HttpResponse
import random

##############################################
#### Templates render
from django.template.loader import render_to_string

str1 = """
<h1>Hello world!</h1>
"""

str2=""" 
<h3>This is cart page</h3>
"""

str3= """ 
<h2>beginner</h2>
"""

num = random.randint(1, 5)
str4= f""" 
<h2>Integer: {num}</h2>
"""

context = {
    'id': num,
    'name': 'Piyush',
}

context_home = {
    'id': num,
    'name': 'Himanshu',
}

def home_view(req):
    # return HttpResponse(str1)
    return HttpResponse(render_to_string('home.html', context=context_home))

def page(req):
    return HttpResponse(render_to_string('page1.html', context=context))

def about(req):
    return HttpResponse(str2)

def me(req):
    print('This is req: {}'.format(req))
    return HttpResponse(str3)

def random(req):
    print(num)
    return HttpResponse(str4)

    