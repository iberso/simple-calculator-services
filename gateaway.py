from http import HTTPStatus
from unicodedata import name
from flask import *
from celery import Celery
from calculator import primeNumberN
from calculator import primeNumberPalindrome

app = Flask(__name__)

@app.route('/api/prime/<int:index>',methods=['GET'])
def primenumber(index):
    if index is None:
        return Response(json.dumps({"result":"missing index"}),status=HTTPStatus.BAD_REQUEST,headers={'Content-Type':'application/json'})
    else:
        result = primeNumberN.delay(index)
        return Response(json.dumps({"result":result}),status=HTTPStatus.OK,headers={'Content-Type':'application/json'})

@app.route('/api/prime/palindrome/<int:index>',methods=['GET'])
def primenumberpalindrome(index):
    if index is None:
        return Response(json.dumps({"result":"missing index"}),status=HTTPStatus.BAD_REQUEST,headers={'Content-Type':'application/json'})
    else:
        result = primeNumberPalindrome.delay(index)
        return Response(json.dumps({"result":result}),status=HTTPStatus.OK,headers={'Content-Type':'application/json'})


if __name__ == '__main__':
    app.run()



