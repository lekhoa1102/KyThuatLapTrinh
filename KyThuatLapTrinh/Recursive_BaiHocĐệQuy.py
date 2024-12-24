#Tính giai thừa
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print("5!=", factorial(5))
#Coi thêm trong ppt để hiểu nó chạy ntn

def H10toH2(n):
    if n>0:
        sd=n%2
        n=n//2
        H10ToH2(n)
        print(sd, end= '')
n=587
H10ToH2(n)