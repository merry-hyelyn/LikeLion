from django.shortcuts import render

print("킹혜린")
# Create your views here.

def index(request):
    myinfo = '''
            김혜린
            컴퓨터소프트웨어공학과
            20174016
            여자
            '''

    myinfo = myinfo.split("\n")
    # myinfo = {' ', 김혜린, 컴소공,20174016, 여자,' '}

    # for i, val in enumerate(myinfo):
    #     myinfo[i] = val.strip()

    for i in range(len(myinfo)):
        myinfo[i] = myinfo[i].strip()

    print(myinfo)

    while True:
        if '' in myinfo:
            myinfo.remove('')

        else:
            break

    return render(request, 'index.html',{
        "a" : myinfo[0],
        "b" : myinfo[1],
        "c" : myinfo[2],
        "d" : myinfo[3],
        "myinfo" : myinfo,
    })
