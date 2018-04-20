
from django.utils.crypto import get_random_string
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

items = {'1001': 19.99,
		 '1002': 24.99,
		 '1003': 4.99,
		 '1004': 49.99
}
def index(request):
    return render(request,'Amazon/index.html')

def buy(request):
	request.session['purchase'] = items[request.POST['product_id']] * int(request.POST['quantity'])

	if 'item_count' not in request.session:
		request.session['item_count'] = 0
	if 'total_spent' not in request.session:
		request.session['total_spent'] = 0

	request.session['item_count'] += int(request.POST['quantity'])
	request.session['total_spent'] += float(request.session['purchase'])
	return redirect('/checkout')


def checkout(request):
	return render(request, 'Amazon/checkout.html')

def clear(request):
	request.session.clear()
	return redirect('/')

# def add(request):
#     if request.method == "POST":
#         date = datetime.now().strftime('%-I:%-M:%S%p, %b %-d %Y')
#         content = {
#         'newword': request.POST['newword'],
#         'color': request.POST['color'],
#         'big': request.POST['big'],
#         'added': str(date)
#         }
#         if not 'list' in request.session:
#             request.session['list'] = []
#         saved_list = request.session['list']
#         saved_list.append(content)
#         request.session['list'] = saved_list
#         print(request.session['list'])
#         return redirect('/')
#     else:
#         return redirect('/')


    
    

# def clear(request):
#     request.session.clear()
#     return redirect('/')