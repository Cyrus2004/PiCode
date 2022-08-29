test = ["k", 8, 9 , "u"]

for i in test:
    print(test.index(i))
    if test.index(i) == len(test) - 1:
        print("End")