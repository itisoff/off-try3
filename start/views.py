from django.shortcuts import render
from django.http import HttpResponse
from .models import Detail, Details_of_Entry, Pricing

def home(request):
    return render(request, 'start/home.html')

def automated_consultancy(request):
    return render(request, 'start/automated_consultancy.html')

def estimated_cost(request):
    if request.method == 'POST':
        types = int(request.POST.get('type'))
        purpose =int(request.POST.get('purpose'))
        quantity = request.POST.get('quantity')
        length = int(request.POST.get('x'))
        width = int(request.POST.get('y'))
        height = int(request.POST.get('z'))
        budget = int(request.POST.get('budget'))
        
        print(types,purpose, budget, quantity, length, width, height)
        if(purpose==1):
            w = purpose+budget-1
            
        elif(purpose==2):
            w = (purpose*2)+budget+1
        else:
            w = (purpose*3)+budget+1
            
        v = w 
        # s = int(v.price)
        s = w * int(quantity) * ((2*height*width) + (2*height*length) + (length*width))
        context = {
            'v': v,
            's': s,
        }
        new = Detail(type=types, purpose= purpose, quantity=quantity, length=length, width=width, height=height, budget=budget, price=s)
        new.save()
        new2 = Pricing(type=types, purpose=purpose, budget=budget)
        new2.save()
        return render(request, 'start/estimated_cost.html', context)

def bidding(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        new = Details_of_Entry(email=email, phone=phone)
        new.save()
    return render(request, 'start/bidding.html')

def blog(request):
    return render(request, 'start/blog.html')

def popup(request):
    return render(request, 'start/popup.html')

