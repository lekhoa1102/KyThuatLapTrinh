def separate(n):
    n1=n//100 # // là chia lấy phần nguyên
    n2=(n//10)%10 # % là chia lấy phần dư
    n3=(n%100)%10
    return n1, n2, n3
n=587
n1,n2,n3=separate(n)
print(f"n={n}, có các chữ số:")
print("n1=",n1)
print("n2=",n2)
print("n3=",n3)