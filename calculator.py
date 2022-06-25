import json
from celery import Celery

app = Celery('calculator', broker='pyamqp://guest:guest@localhost:5672', backend=f'redis://localhost:6379')

@app.task
def primeNumberN(index):
    if(index >= 0):
        num = 1
        while(True):
            num+=1
            flag = True
            for j in range(2, num):
                if(num%j == 0):
                    flag = False
            if flag:
                index-=1;

            if(index < 0):
                # return num
                return json.dumps({'result':num})
@app.task
def primeNumberPalindrome(index):
    num = 1
    while(True):
        num+=1;
        flag = True
        check = False
        for j in range(2, num):
            if(num%j == 0):
                flag = False
                
        if flag:
            if(str(num)[::-1] == str(num)):
                index-=1;

        if(index < 0):
            # return num
            return json.dumps({'result':num})