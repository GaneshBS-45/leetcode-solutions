def func(i:int,n:int):
    if i<1:
        return
    print(i,end=" ")
    func(i-1,n)

func(4,4)

print()
# with backtracking

def funct(i:int,n:int):
    if i>n:
        return
    funct(i+1,n)
    print(i,end=" ")

funct(1,20)