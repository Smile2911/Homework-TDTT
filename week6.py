#1
dayso =  list(map(int, input().split()))
daysoloc = list(dict.fromkeys(dayso))
print (daysoloc)
#2
dayso = list (map(int, input().split()))
ketqua = []
tong = 0

for so in (dayso) :
  tong = tong + so
  ketqua.append(tong)
print (ketqua)
#3
a = tuple(map(int, input().split()))

k  = int (input())
if len(a)>0:
  k = k % len(a)
ketqua =  a[k:]+a[:k]
print(ketqua)
#4
listcap = list(map(str, input().split()))
ketqua = {}
for cap in listcap :
  key, value = cap.split(':')
if key in ketqua :
  ketqua[key].append(value)
else :
  ketqua[key]= value
print (ketqua)
#5
a = list (map(int , input ().split()))
ketqua = {'positives':0 ,'negatives':0 , 'zeros':0 }
for so in a :
  if so >0 :
    ketqua['positives']+=1
  elif so <0 :
    ketqua['negatives']+=1
  else :
    ketqua['zeros']+=1
print(ketqua)


#6
a = list (map ( int , input().split() ))
tong= 0
for so in range (0,len(a)+1):
  tong  = tong  + so
print (tong)
#7
a=tuple(map(str , input().split()) )
print (a[0])
print (a[-1])
print (sorted(a, reverse=True ))
#8
a = list (map (str, input().split()))
ketqua={}
for i in a :
  if i in ketqua :
    ketqua[i]+=1
  else :
    ketqua[i]=1
print (ketqua)
#9 
line1 =  input().split()
dict1= {}
for  i in line1:
  k , v = i.split(':')
  dict1[k]= int(v) 
line2 =  input().split() 
dict2 =  {}
for i in line2 : 
   k , v = i.split(':')
   dict2[k]= int(v)
for k ,v  in dict2.items() :
  if k  in dict1 :
    dict1[k]+=v  
  else :
    dict1[k]=v 
print(dict1)     
#10 
dayso = list(map(int, input().split()))
k = int(input())
ketqua = []
for so1 in range(len(dayso)):
  for so2 in range(so1+1,len(dayso)):
    if dayso[so1]+dayso[so2]==k:
      ketqua.append((so1,so2))
print(ketqua)
   

  #11
tup1 = tuple(map(int,input().split()))
tuchan = []
tule=[]
for i in tup1:
  if i % 2 ==0 :
    tuchan.append(i)
  else :
    tule.append(i)
print(tuple(tuchan),tuple((tule)))  

#12
#12
line = list(map(int,input().split()))
dem={}
for so in line :
  if so in dem : 
    dem[so]+=1 
  else : 
    dem[so]=1 
solanmax = 0 
for so in dem : 
  if dem[so] >solanmax :
    solanmax = dem[so] 
cacsonhieunhat = []
for so ,solan in dem.items() : 
  if solan == solanmax: 
    cacsonhieunhat.append(so) 
print(min(cacsonhieunhat))       
#13
a = input().split()
dict1 = {}
for i in a : 
  k ,v  = i.split(':')
  dict1[k]= v 
dict2 = {}
for k, v in dict1.items(): 
  dict2[v]=k 
print(dict1)
print(dict2 )    
#14
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
ketqua =[]
for i in list1:
  if i in list2 : 
    ketqua.append(i)

print(list(set(ketqua)))
#15
line1 = input().split()
a = int(input())
dict1 = {}
for i in line1 : 
  k , v = i.split(':')
  dict1[k]= int(v)
ketqa = {}
for k ,v in dict1.items():
  if  v > a :
    ketqa[k]=v
print (ketqa)    

#16

n, m = map(int, input("Nhập n, m: ").split())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Ma trận:")
for i in range(n):
    for j in range(m):
 
        print("{:>4}".format(matrix[i][j]), end='') 

    print()
#17
n = int(input("Nhập kích thước n: "))
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

print("Đường chéo chính:", end=" ")
for i in range(n):
    print(matrix[i][i], end=" ")

print("\nĐường chéo phụ:", end=" ")
for i in range(n):
    print(matrix[i][n - 1 - i], end=" ")     
#18

data = list(map(int, input("Nhập n m k: ").split()))
n, m, k = data[0], data[1], data[2]

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
tong_cot = 0
for i in range(n):
    tong_cot += matrix[i][k]

print(f"Tổng cột {k}: {tong_cot}")    
#19
def tim_vi_tri_lon_nhat(danh_sach):
    vi_tri_max = 0 
    for i in range(1, len(danh_sach)):
        if danh_sach[i] > danh_sach[vi_tri_max]:
            vi_tri_max = i 
            
    return vi_tri_max
#20
def tim_vi_tri_k(danh_sach, k):
    for i in range(len(danh_sach)):
        if danh_sach[i] == k:
            return i 
            
    return -1

#21
line = input().split()
ketqua = {}
for i in range(len(line)):
    chuoi = line[i]
    if chuoi in ketqua:
        ketqua[chuoi] += (i,)
    else:
        ketqua[chuoi] = (i,)
print(ketqua)
#22
def tim_vi_tri_lon_nhat(danh_sach):
    if len(danh_sach) == 0:
        return -1
    vi_tri_max = 0 
    for i in range(1, len(danh_sach)):
        if danh_sach[i] > danh_sach[vi_tri_max]:
            vi_tri_max = i 
    return vi_tri_max

# Test
a = list(map(int, input().split()))
print(tim_vi_tri_lon_nhat(a))
