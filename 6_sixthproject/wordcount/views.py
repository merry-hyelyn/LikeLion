from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

# render 세개의 인자 가능 -> request, html 파일, 사전형 객체 받아들일 수 있음

def about(request):
    return render(request,'about.html')

def result(request):
    text =  request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        
        else:
            word_dictionary[word]=1

    return render(request,'result.html',{'full' : text, 'total': len(words),'dictionary' : word_dictionary.items()})


    #.items() : 사전의 쌍들을 보냄