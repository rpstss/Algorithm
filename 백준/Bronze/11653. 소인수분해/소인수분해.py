N=int(input())
def func(X):
    for i in range(2,X+2):
        if X==1:
            return
        if X%i==0:
            print(i)
            X=int(X/i)
            func(X)
            break
            
        
func(N)        