# W7A1 - Tìm vị trí phần tử bằng binary search
def binary_search(arr, l, r, target):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

dayso = list(map(int, input().split()))
n = int(input())
print(binary_search(dayso, 0, len(dayso) - 1, n))

# W7A2 - Đếm số lần xuất hiện
dayso = list(map(int, input().split()))
x = int(input())
dem = 0
for so in dayso:
    if so == x:
        dem += 1
print(dem)

# W7A3 - Selection sort
dayso = list(map(int, input().split()))
n = len(dayso)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if dayso[j] < dayso[min_idx]:
            min_idx = j
    dayso[i], dayso[min_idx] = dayso[min_idx], dayso[i]
print(dayso)

# W7A4 - Số xuất hiện nhiều nhất, in số đầu tiên nếu bằng nhau
dayso = list(map(int, input().split()))
mp = {}
max_dem = 0
for so in dayso:
    mp[so] = mp.get(so, 0) + 1
    if mp[so] > max_dem:
        max_dem = mp[so]

for so in dayso:
    if mp[so] == max_dem:
        print(f"{so} xuat hien nhieu nhat, som nhat, {max_dem} lan")
        break

# W7A5 - Đếm cặp có tổng bằng x
dayso = list(map(int, input().split()))
x = int(input())
mp = {}
ketqua = 0
for so in dayso:
    can = x - so
    if can in mp:
        ketqua += mp[can]
    mp[so] = mp.get(so, 0) + 1
print(ketqua)

# W7A6 - Làm phẳng list lồng nhau 1 cấp
s = input()
li = eval(s)
ketqua = []
for mangcon in li:
    for so in mangcon:
        ketqua.append(so)
print(ketqua)

# W7A7 - Dãy con tăng dài nhất
li = eval(input())
n = len(li)
if n == 0:
    print(0)
else:
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if li[i] > li[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))

# W7A8 - Tìm độ dài đoạn ngắn nhất chứa x
def tim_do_dai_ngan_nhat(x, cac_doan):
    ans = -1
    for doan in cac_doan:
        L, R = doan
        if L <= x <= R:
            dai = R - L + 1
            if ans == -1 or dai < ans:
                ans = dai
    return ans

cac_doan = eval(input())
cac_doan.sort(key=lambda d: d[1] - d[0] + 1)
cac_x = eval(input())
for x in cac_x:
    print(tim_do_dai_ngan_nhat(x, cac_doan), end=" ")

# W7A9 - Đếm số phần tử nhỏ hơn đã xuất hiện trước (dùng BST đơn giản)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.nho_hon = 0
        self.trung = 1

def chen_va_dem(root, val):
    node = root
    dem = 0
    while True:
        if val < node.val:
            node.nho_hon += 1
            if node.left is None:
                node.left = Node(val)
                break
            node = node.left
        elif val > node.val:
            dem += node.nho_hon + node.trung
            if node.right is None:
                node.right = Node(val)
                break
            node = node.right
        else:
            dem += node.nho_hon
            node.trung += 1
            break
    return dem

dayso = list(map(int, input().split()))
if not dayso:
    print()
else:
    root = Node(dayso[-1])
    ketqua = [0]
    for i in range(len(dayso)-2, -1, -1):
        dem = chen_va_dem(root, dayso[i])
        ketqua.append(dem)
    print(*ketqua[::-1])

# W7A10 - Đoạn con dài nhất tổng % m == 0
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def chen_va_tim(root, val, m):
    node = root
    ans = 0
    while node:
        if val < node.val:
            ans = max(ans, m - (node.val - val))
            if node.left is None:
                node.left = Node(val)
                return ans
            node = node.left
        else:
            ans = max(ans, val - node.val)
            if node.right is None:
                node.right = Node(val)
                return ans
            node = node.right
    return ans

dayso = list(map(int, input().split()))
m = int(input())
if not dayso:
    print(0)
else:
    prefix = 0
    root = Node(0)
    max_dai = 0
    for so in dayso:
        prefix = (prefix + so) % m
        dai = chen_va_tim(root, prefix, m)
        max_dai = max(max_dai, dai)
    print(max_dai)

# W7A11 - Đếm chuỗi con (loại dấu câu cuối)
s1 = input().split()
s2 = input().split()

for i in range(len(s1)):
    while s1[i] and not s1[i][-1].isalpha():
        s1[i] = s1[i][:-1]

dem = 0
for i in range(len(s1) - len(s2) + 1):
    if s1[i:i+len(s2)] == s2:
        dem += 1
print(dem)

# W7A12 - Sắp xếp 4 chuỗi và in A B C D
li = []
for i in range(4):
    s = input().strip()
    li.append((s, i))

li.sort()
idx = ['A', 'B', 'C', 'D']
for item in li:
    print(idx[item[1]], end=" ")

# W7A13 - Dãy con liên tiếp dài nhất các số khác nhau
dayso = list(map(int, input().split()))
if not dayso:
    print(0)
else:
    ans = 1
    mp = {}
    for so in dayso[::-1]:
        cnt = 1
        if so - 1 in mp:
            cnt = max(cnt, mp[so - 1] + 1)
        if so + 1 in mp:
            cnt = max(cnt, mp[so + 1] + 1)
        mp[so] = cnt
        ans = max(ans, cnt)
    print(ans)

# W7A14 - Vị trí số 7 (giảm dần)
n = int(input())
dayso = list(map(int, input().split()))
vi_tri = []
for i in range(len(dayso)):
    if dayso[i] == 7:
        vi_tri.append(i)
if not vi_tri:
    print("Not found")
else:
    vi_tri.sort(reverse=True)
    print(*vi_tri)

# W7A15 - Nemo và 2 hàng xóm (vòng tròn)
n = int(input())
ten = []
for _ in range(n):
    ten.append(input().strip())

tim_thay = False
for i in range(n):
    if ten[i] == 'Nemo':
        tim_thay = True
        if n == 1:
            print("Nemo is alone")
        elif i == 0:
            print(f"{ten[-1]} and {ten[1]}")
        elif i == n - 1:
            print(f"{ten[i-1]} and {ten[0]}")
        else:
            print(f"{ten[i-1]} and {ten[i+1]}")
        break
if not tim_thay:
    print("Nemo not found")

# Bài 1 - Loại bỏ trùng lặp giữ thứ tự
dayso = list(map(int, input().split()))
daysoloc = list(dict.fromkeys(dayso))
print(daysoloc)

# Bài 2 - Tổng tích lũy
dayso = list(map(int, input().split()))
ketqua = []
tong = 0
for so in dayso:
    tong += so
    ketqua.append(tong)
print(ketqua)

# Bài 3 - Dịch vòng trái k bước
dayso = tuple(map(int, input().split()))
k = int(input())
if len(dayso) == 0:
    print(dayso)
else:
    k = k % len(dayso)
    ketqua = dayso[k:] + dayso[:k]
    print(ketqua)
