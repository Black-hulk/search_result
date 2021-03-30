from django.shortcuts import render
from .models import *
import datetime

# Create your views here.
def search(request):
    if request.method=="POST":
        query_name=request.POST.get('search',None)
        if query_name:
            results=Searchitem.objects.filter(name__contains=query_name)
            #record=Searchrecord(sresult=results)
            #record.save()
            return render(request, 'search.html', {"results":results})
            
            #request.sessions['results']=Searchitem.objects.filter(name__contains=query_name)
    #now = datetime.datetime.now().strftime('%H:%M:%S')
    #results=request.sessions['results']
    if request.method=="POST":
        skeyword=request.POST['search']
        record=Searchrecord(skeyword=skeyword)
        record.save()
        return print('ok............')
    #record=Searchrecord(results=sresult)
    #record.save()
    return render(request, 'search.html')

"""def searchrecord(request):
    #now = datetime.datetime.now().strftime('%H:%M:%S')
    #results=request.sessions['results']
    if request.method=="POST":
        skeyword=request.POST['search']
        record=Searchrecord(skeyword=skeyword)
        record.save()
        return print('ok............')
    #record=Searchrecord(now=stime,results=sresult)
    #record.save()"""

    


def test(request):
    return render(request, 'test.html')