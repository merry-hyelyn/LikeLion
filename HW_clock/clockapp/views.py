from django.shortcuts import render

# Create your views here.

from django.utils import timezone


def clock(request):
    nowtime = timezone.now()
    li = [
        "월",
        "화",
        "수",
        "목",
        "금",
        "토",
        "일",
    ]

    AM = '오전'
    t_hour = nowtime.hour

    if nowtime.hour >= 12:
        AM = '오후'
        t_hour = nowtime.hour-12
    return render(request, 'index.html', {
        "a": nowtime,
        "AM": AM,
        "hour": t_hour,
        "weekday": li[nowtime.weekday()],
    })
