from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


def main_page(request):
    return render(request,'index.html')



def item(request, item_id: int):
    try:
        item = Item.objects.get(pk=item_id)
    except ObjectDoesNotExist:
        raise Http404(f"Item with id={item_id} not found")
    context = {
        "item":item
    }
    return render(request,'item.html', context)


def items_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'items_list.html', context)