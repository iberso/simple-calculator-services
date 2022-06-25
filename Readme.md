# Simple Calculator Services
This project was created to fulfill an individual assignment in a service-oriented architecture course.

In this architecture we are asked to make a simple calculator application that calculates / performs calculations that are quite heavy. Therefore, they were asked to make an asynchronous application by utilizing Celery technology. (https://docs.celeryq.dev/en/stable/)

where this service has 2 main features:

- Finds the prime number that goes to index
- Finding palindrome primes to index

## Technologies Used:
- Python 3
- Flask
- Redis
- Celery

## Service Architecture
![Architecture-soa-Page-2 drawio](https://user-images.githubusercontent.com/74914280/175782895-ce977aaa-1352-40f8-be05-b6615c46fb95.png)

## REST API Endpoint
```bash
GET /api/prime/<int:index>
```

```bash
GET /api/prime/palindrome/<int:index>
```