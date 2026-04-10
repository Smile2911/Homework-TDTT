#1
n = int(input("nhap n: "))
 
def tongcacsoden(n):
  tong=0
  for i in range(1,n+1):
    tong = tong + i
  return tong 
    
print(tongcacsoden(n))

#2
import math 
n= int(input())
if n <0:    
    print("vui long nhap so nguyen duong")
elif 0<=n<2:
    print('không phải số nguyên tố ')
elif n>=2:
      for i in range (2, int(math.sqrt(n))+1 ):
        if n%i ==0:
          print('ko phai so nguyen to ')
          break
      else: print('đây là số nguyên tố ')   


#3
giai_thua=1
a = int(input())
for i in range(1, a+1):
  giai_thua = (i)* giai_thua 

print (f'giai thừa của {a} là {giai_thua}')  

#4 
a = int(input())
sochuso =0
while a>10:
     a % 10 !=0
sochuso = sochuso +1
a = a //10
print(sochuso)
 #5
dayso = list(map(int,input().split()))
x= 42
if x in dayso:
    print("i have found meaning of life")
else:
    print("it's just a joke ")    
 #6

import math 
a,b= map(int,input().split())
tong=0
def locsonguyento(n):
    if n <2 : 
        return False
    for i in range (2,int(math.sqrt(n)+1 )):
        if n % i == 0 :
            return False
        

    return True
for so_hien_tai in range (a,  b+1  ):
    if locsonguyento(so_hien_tai): 
        tong = tong + so_hien_tai 
print (tong )         

#7
import math 

def tim_uoc_nguyen_to_max():
  maxprime = -1 
  
  try :
    n = int ( input () ) 
    if n <2 : 
      print ( ' vui long nhap so lon hon 2 ')
      return 
    while n%2 == 0   : 
      maxprime =2
      n= n //2    
    for i in range(3, int(math.sqrt(n))+1,2):
        while n %i ==0: 
          maxprime = i
          n = n //i
    if n >2 : 
      maxprime = n  
    print(f'tim_uoc_nguyen_to_max: {maxprime }')      
  except ValueError:
    print (' nhap so nguyen ')

#9
def kiem_tra_chuso_khacnhau(so):
    chuoi_so = str(so)
    return len(set(chuoi_so)) == len(chuoi_so)

def tim_sochinhphuong_distinct():
    try:
        so_n = int(input())
    except ValueError:
        return

    ketqua = []
    gioihan = int(math.sqrt(so_n))
    
    for i in range(1, gioihan + 1):
        so_chinhphuong = i * i
        if kiem_tra_chuso_khacnhau(so_chinhphuong):
            ketqua.append(str(so_chinhphuong))
            
    print(" ".join(ketqua))

#10
def tinh_dodai_collatz(so_batdau):
    dodai = 1
    so_hientai = so_batdau
    while so_hientai != 1:
        if so_hientai % 2 == 0:
            so_hientai = so_hientai // 2
        else:
            so_hientai = 3 * so_hientai + 1
        dodai += 1
    return dodai

def tim_collatz_dainhat():
    try:
        so_n = int(input())
    except ValueError:
        return

    dodai_max = 0
    so_khoitao = 0

    for i in range(1, so_n + 1):
        dodai_hientai = tinh_dodai_collatz(i)
        
        if dodai_hientai > dodai_max:
            dodai_max = dodai_hientai
            so_khoitao = i
            
    print(f"{so_khoitao} {dodai_max}")

#11
def check(x):
    dem = 0
    if x == 1:
        return dem
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0 and i * i != x:
            if i % 2 == 0:
                dem += 1
            if (x // i) % 2 == 0:
                dem += 1
        elif i * i == x and i % 2 == 0:
            dem += 1
    return dem
n = int(input())
print(check(n))

#12 
a,b = map(int,input().split())
print(int(a*((1+0.7/100)**b)))

#13
def sum(x):
    tong = 1
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            if i * i != x:
                tong += i + x // i
            else:
                tong += i
    return tong
a,b = map(int, input().split())
if sum(a) == b and sum(b) == a:
    print("true")
else:
    print("false")
 
#14
def GCD(c,d):
    while d != 0:
        c,d = d, c%d
    return c
a,b = map(int,input().split())
print(GCD(a,b))

#15
a,b = map(int,input().split())
for i in range(b//2,-1,-1):
    for j in range(b//4,-1,-1):
        if i*2 + j*4 == b and i + j == a:
            print(i," ",j)
            exit()
print("invalid") 


#16
for i in range(0,101,2):
    if i % 3 == 0:
        print(i)

#17
a = int(input())
for i in range(1,11):
    print(f"{a} x {i} = {a*i}")

#18
def gcd(a,b):
    while b != 0:
        a, b = b, a % b 
    return a
c,d = map(int, input().split())
for i in range(1, gcd(c,d)+1):
    if gcd(c,d) % i == 0:
        print(i,end=' ')

#19
n = int(input())
for i in range(2,n+1,2):
    print(i, end=' ')

#20
n = int(input())
while n % 2 == 0:
    n //= 2
if n == 1:
    print("true")
else:
    print("false")            

#21
n = int(input())
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print(sum)

#22
even = 0
odd = 0
n = int(input())
while n > 0:
    res = n % 10
    if res % 2 == 0:
        even += 1       
    else:
        odd += 1    
    n = n // 10
print("Even:", even)
print("Odd:", odd)

#23
n = int(input())
for i in range(n//2,-1,-1):
    if (i*(i+1))/2 < n:
        print(i)
        break

#24
n = int(input())
s = 0
i = 1
while s < n:
    s += 1/i
    i += 1
print(i-1)

#25
list=[]
dem = 0
while True:
    n = int(input())
    list.append(n)
    if n == -1:
        break
    dem +=1
list.sort()
print(list[0]," ",list[dem-1])

#26
def check(n):
    list = [1,1]
    x = 1
    y = 1
    z = 0
    while z < n:
        z = x + y
        list.append(z)
        x = y
        y = z
    if n in list:
        return True
    return False
k = int(input())
for i in range(k,-1,-1):
    if check(i):
        print(i)
        break
#27
s = input().strip()
dem = 0
for i in s:
    if i == ' ':
        dem += 1
print(dem + 1)    

#28
s = input()
xau = ''
for i in range(len(s)):
    if s[i] != ' ':
        xau +=s[i]
    else:
        break
print(xau)

#29
a,b,c = map(int,input().split())
print(a + b + c)

#30
xau = input()
t = 0
h = 0
s = 0
for i in xau:
    if 'a' <= i <= 'z':
        t +=1
    if 'A' <= i <= 'Z':
        h +=1
    if '0' <= i <= '9':
        s +=1
print(t," ",h," ",s)


#31
s = input()
sum = 0
for i in s:
    if '0' <= i <= '9':
        sum += int(i)
print(sum)

#32
s = input()
sum = 0
for i in s:
    if '0' <= i <= '9':
        sum += int(i)
print(sum)

#33
n = int(input())
s = ""
dem = 0
xau = str(n)
for i in xau:
    dem += 1
    if dem % 3 == 0 and dem != len(xau):
        s += i + "."
    else:
        s += i
print(s)

#34
a = input()
b = input()
pos = a.find(b)
a = a[:pos] + a[pos+len(b):]
if a[0] == ' ':
    a = a[1:]
print(a)