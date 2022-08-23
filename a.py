import time
import datetime

# def f1(func):
#     def wrapper():
#         print("Started")
#         func()
#         print("Ended")
#     return wrapper

# def f(a, b):
#     c = a + b
#     print(c)

# f1(f(2, 3))


# dateTime = datetime.datetime.now()

while True:
    f = open("example.txt", "r")
    text = f.read()
    print(text)
    time.sleep(1)