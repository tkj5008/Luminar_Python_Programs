def patt(n):
    for i in range(n):
        num=1
        for j in range(i):
            print(num,end=" ")
            num+=1
        print("\r")
patt(5)
