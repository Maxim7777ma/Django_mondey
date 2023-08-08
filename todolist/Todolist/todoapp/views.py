from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

plans=[
    {
        'title':'Sunday',
        'todo':'mod'
    },

    {
         'title':'Wednesday',
         'todo':'help'
    },
    {
         'title':'Tuesday',
         'todo':'cool'
    },
]

i=0
for plan in plans:
    i+=1
    plan['id']=i




def todoapp(req) :
    sting=""
    for plan in plans:
        sting+= f"""
        <div>
            <h3>{plan['id']}</h3>
            <a href="{plan['title']}">{plan['title']}</a>
        </div>
            <br>
        \n
        """
    print(sting)
        
        
        
    return HttpResponse(sting)

def title_page(req,title):
    for plan in plans:
        if plan['title']==title:
            
            return HttpResponse(f"""
        <div>
            <h3>{plan['id']}</h3>
            <a href="">{plan['title']}</a>
            <p>{plan['todo']}</p>
        </div>
            <br>
        \n
        """)