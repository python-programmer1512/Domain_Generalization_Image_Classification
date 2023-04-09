T=[]
while 1:
    a=input()
    if a=="end":
        break
    T.append(a.split("\t"))

def sort_out(T):
    R=[]
    for i in range(len(T)):
        Q=T[i][:12]
        Q.insert(0,float(T[i][12]))
        R.append(Q)

    R.sort(reverse=True)
    print("R")
    print(R[0])
    OUT=[1,2,3,4,5,6,0]

    for i in range(min(10,len(R))):
        for out in OUT:
            print("|",end="")
            if out==0:
                print(format(R[i][out],".4f"),end="")
            else:
                if R[i][out]=="x":
                    print("❌",end="")
                elif R[i][out]=="o":
                    print("⭕",end="")

        print("|")

def non_sort_out(T):

    #print(T)
    OUT=[0,1,2,3,4,5,12]
    for i in range(len(T)):
        for out in OUT:
            print("|",end="")
            if out==12:
                print(format(float(T[i][out]),".4f"),end="")
            else:
                if T[i][out]=="x":
                    print("❌",end="")
                elif T[i][out]=="o":
                    print("⭕",end="")

        print("|")

sort_out(T)
