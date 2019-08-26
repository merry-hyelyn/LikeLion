from django.shortcuts import render

# Create your views here.

import random

def home(request):
    
    arr = []

    num = random.randint(1, 46)
    for i in range(7) :
        while num in arr : 
            num = random.randint(1, 46)
        
        arr.append(num)

    return render(request,'home.html',{
        "a" : arr[0],
        "b" : arr[1],
        "c" : arr[2],
        "d" : arr[3],
        "e" : arr[4],
        "f" : arr[5],
        "g" : arr[6]
    })
