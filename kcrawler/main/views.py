from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import EntryItemForm
from .models import EntryItem, ArticleItem
from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http://localhost:6800')

# Create your views here.
def CreateEntry(request):
    form = EntryItemForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        #scrapyd.schedule('default', 'mainspider', keyword = request.POST.get('keyword', None))
        form.save()

    objects = EntryItem.objects.all()
    return render(request, 'main/index.html', {'objects': objects, 'form': form})

def ListArticles(request, pk):
    entry = EntryItem.objects.get(pk=pk)
    return render(request, 'main/list.html', {'objects': entry.enteredBy.all()})
