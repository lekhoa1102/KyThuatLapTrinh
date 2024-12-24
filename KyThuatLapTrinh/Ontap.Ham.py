def giaithua(n):
    gt=1
    for i in range(1,n+1):
        gt=gt*i
    return gt 

def A(n,k):
    return giaithua(n)/giaithua(n-k) #tái sử dụng hàm giaithua(n) => miễn là giống hình thức của tham số hình thức thì cái dữ liệu nào cũng xài đc

def C(n,k):
    return giaithua(n)/(giaithua(n-k)*giaithua(k))

gt_5=giaithua(5)
print("5!=", gt_5)