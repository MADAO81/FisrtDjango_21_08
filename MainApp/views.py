from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

author = {
    "first_name": "Evgeniy",
    "nickname" : "MADAO",
    "last_name": "Chernyshev",
    "phone": "89932765699",
    "email": "chernyshev.evgeniy@gmail.com",
}

items = [
   {"id": 1, "name": "sneakers ", "quantity":32},
   {"id": 2, "name": "leather jacket", "quantity":5},
   {"id": 3, "name": "coca cola", "quantity":64},
   {"id": 4, "name": "cheetos chips", "quantity":23},
   {"id": 5, "name": "sombrero", "quantity":8},
]

def main_page(request):
    return render(request,'index.html')

def about(request):
    result = f"""first_name: <b>{author["first_name"]}</b></br>,
                nickname :<b>{author["nickname"]}</b></br>,
                last_name: <b>{author["last_name"]}</b></br>,
                phone: <b>{author["phone"]}</b></br>,
                email: <b>{author["email"]}</b></br>
    """
    return HttpResponse(result)

def item(request, item_id: int):
    for item in items:
        if item["id"] == item_id:
            item_result = f"Item: {item['name']}, quantity:{item['quantity']}"
            return HttpResponse(item_result)
    # return HttpResponseNotFound(f"Item with id={item_id} not found")
    raise Http404(f"Item with id={item_id} not found")

def items_list(request):
    context = {
        'items': items
    }
    return render(request, 'items_list.html', context)