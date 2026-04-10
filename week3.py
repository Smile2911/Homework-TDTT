#

n = int(input("Nhập một số nguyên: "))
n_daonguoc = 0

while n>0 :
  phandu = n % 10
  n_daonguoc = n_daonguoc * 10 + phandu
  n=n//10

print("Số đảo ngược là:", n_daonguoc)
#

a,b=map(int,input().split())
a = a^b
b = a^b
a = a^b
print(a)
print(b)
#

a = int(input())
b = a&(a-1)
if b == 0:
  print("True")
else:
  print("False")

#

import math
a=float(input())
b=float(input())
c =a/b
print(math.floor(c))
#

a = float(input())
b = float(input())
c= a/b
print(round(c))
#

a = int(input())
b = a%2
if b == 0:
  print("Even")
else:
  print("Odd")
#

a = int(input())
b = int(input())
if a<0 and b<0 :
  print('true')
else :
  print('false')
#

a = input()
b = input()
if len(a) > len(b) :
  print('true ')
else : print ('false')
#

a = float(input(' cạnh thứ nhất :'))
b = float (input(' cạnh thứ hai :'))
c = float (input(' cạnh thứ ba :'))
if a+b >c and a+c>b and c+b>a :
  print ('3 cạnh tạo thành 1 tam giác' )
else : print('3 cạnh không tạo thành tam giác')
#

a = int(input())
b = int(input())
c = int(input())
if a>b and a>c :
  print(a)
elif b>a and b>c :
  print(b)
else :
    print(c)

#

a = float(input(' cạnh thứ nhất :'))
b = float (input(' cạnh thứ hai :'))
c = float (input(' cạnh thứ ba :'))
if a+b >c and a+c>b and c+b>a  :
  if a==b==c :
    print('tam giác đều')
  elif a==b or a==c or b==c :
    print('tam giác cân')
  elif a*a + b*b == c*c or a*a +c*c == b*b or b*b + c*c == a*a :
    print('tam giác vuông')
  else : print('tam giác thường')
else : print('3 cạnh không tạo thành tam giác')
#

a = int(input('năm:'))
if a%400==0: print('năm nhuận')
elif a%4==0 and a % 100 != 0 :
  print('năm nhuận')
else : print('năm không nhuận')


#
a = float(input('số kWh tiêu thụ :'))
if 0<a and a<50 :
  print(a*1500,'đ')
elif 50<a and a<100 :
  print(a*2000,'đ')
else : print(a*3000,'đ')

#\

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

if a == 0:
    if b == 0:
        print("Vô số nghiệm")
    else:
        print("Vô nghiệm")
else:
    x = -b / a
    print(f"Nghiệm của phương trình là: {x:.2f}")

    #

diem_trung_binh = float(input("Nhập điểm trung bình: "))

if diem_trung_binh >= 8.0:
  print("Học lực: Giỏi")
elif diem_trung_binh >= 6.5:
  print("Học lực: Khá")
elif diem_trung_binh >= 5.0:
  print("Học lực: Trung bình")
else:
  print("Học lực: Yếu")
  #

x = float(input("Nhập vào một số thực: "))
if x >= 0:
    down = int(x)
else:
    down = int(x) - (x != int(x))
if x > 0:
    up = int(x) + (x != int(x))
else:
    up = int(x)

# Làm tròn tới số nguyên gần nhất
if x - int(x) >= 0.5:
    nearest = int(x) + 1
elif x - int(x) <= -0.5:
    nearest = int(x) - 1
else:
    nearest = int(x)

print(up, down, nearest)
