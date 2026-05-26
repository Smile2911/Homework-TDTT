#1 - Hình trụ: diện tích bề mặt và thể tích
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.pi = 3.14
    
    def surface_area(self):
        return 2 * self.pi * self.radius**2 + 2 * self.pi * self.radius * self.height
    
    def volume(self):
        return self.pi * self.radius**2 * self.height

r, h = map(float, input().split())
cyl = Cylinder(r, h)
print(f"{cyl.surface_area():.2f} {cyl.volume():.2f}")

#2 - Ngày tiếp theo (kiểm tra hợp lệ)
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def is_valid(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (self.year % 400 == 0) or (self.year % 4 == 0 and self.year % 100 != 0):
            days_in_month[1] = 29
        
        if self.month < 1 or self.month > 12:
            return False
        if self.day < 1 or self.day > days_in_month[self.month - 1]:
            return False
        return True
    
    def next_day(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (self.year % 400 == 0) or (self.year % 4 == 0 and self.year % 100 != 0):
            days_in_month[1] = 29
        
        d = self.day + 1
        m = self.month
        y = self.year
        
        if d > days_in_month[m - 1]:
            d = 1
            m += 1
            if m > 12:
                m = 1
                y += 1
        return Date(d, m, y)

date_str = input().strip()
try:
    dd, mm, yyyy = map(int, date_str.split("/"))
    d = Date(dd, mm, yyyy)
    if not d.is_valid():
        print("INVALID")
    else:
        next_d = d.next_day()
        print(f"{next_d.day:02d}/{next_d.month:02d}/{next_d.year:04d}")
except:
    print("INVALID")

#3 - Tọa độ điểm trong mặt phẳng
class ToaDo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def xet(self):
        if self.x == 0 and self.y == 0:
            return "Gốc toạ độ"
        elif self.x == 0 and self.y != 0:
            return "Trên trục Oy"
        elif self.x != 0 and self.y == 0:
            return "Trên trục Ox"
        else:
            khoang_cach = ((self.x**2) + (self.y**2))**0.5
            return f"khoảng cách: {khoang_cach}"

x, y = map(int, input().split())
a = ToaDo(x, y)
print(a.xet())

#4 - Máy tính bỏ túi (menu lặp)
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def set_numbers(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def product(self):
        return self.a * self.b
    
    def divide(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b
    
    def power(self):
        return self.a ** self.b
    
    def mod(self):
        if self.b == 0:
            return "Error: Modulo by zero"
        return self.a % self.b

a, b = map(float, input().split())
calc = Calculator(a, b)

while True:
    print("\n--- MENU ---")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Hàm mũ")
    print("6. Mod (phần dư)")
    print("7. Nhập lại 2 số mới")
    
    choice = input("Chọn phép toán (1-7): ")
    
    if choice == "1":
        print("Kết quả:", calc.add())
    elif choice == "2":
        print("Kết quả:", calc.subtract())
    elif choice == "3":
        print("Kết quả:", calc.product())
    elif choice == "4":
        print("Kết quả:", calc.divide())
    elif choice == "5":
        print("Kết quả:", calc.power())
    elif choice == "6":
        print("Kết quả:", calc.mod())
    elif choice == "7":
        a, b = map(float, input("Nhập 2 số mới: ").split())
        calc.set_numbers(a, b)
        print("Đã cập nhật 2 số mới.")
    else:
        print("Lựa chọn không hợp lệ!")
    
    thoat = input("Bạn có muốn thoát? (yes để thoát): ")
    if thoat.lower() == "yes":
        print("Chương trình kết thúc.")
        break

#5 - Giỏ hàng mua sắm
class ShoppingCart:
    def __init__(self):
        self.sp = []
    
    def them_sp(self, ten, gia):
        self.sp.append({"ten": ten, "gia": gia})
        print(f"đã thêm {ten} với giá {gia} vào giỏ hàng")
    
    def xoa_sp(self, ten):
        for sp in self.sp[:]:
            if sp["ten"] == ten:
                self.sp.remove(sp)
                print(f"{ten} đã được xóa khỏi giỏ hàng")
                return
        print(f"Không tìm thấy {ten}")
    
    def kt_rong(self):
        if len(self.sp) == 0:
            print("giỏ hàng hiện đang rỗng")
        else:
            print("giỏ hàng hiện không rỗng")
    
    def tien_tong(self):
        tong = 0
        for sp in self.sp:
            tong += sp["gia"]
        print(f"tổng tiền là {tong}")
    
    def hien_thi(self):
        print("danh sách sản phẩm trong giỏ hàng:")
        for sp in self.sp:
            print(f"{sp['ten']} với giá {sp['gia']}")
    
    def xoa(self):
        self.sp.clear()
        print("giỏ hàng đã được xóa")

Sh = ShoppingCart()
while True:
    print("1. thêm sản phẩm")
    print("2. xóa sản phẩm")
    print("3. kiểm tra giỏ hàng rỗng")
    print("4. tính tiền tổng")
    print("5. hiển thị giỏ hàng")
    print("6. xóa giỏ hàng")
    
    n = int(input("chọn chức năng: "))
    
    if n == 1:
        ten = input("nhập tên sản phẩm: ")
        gia = float(input("nhập giá sản phẩm: "))
        Sh.them_sp(ten, gia)
    elif n == 2:
        ten = input("nhập tên sản phẩm: ")
        Sh.xoa_sp(ten)
    elif n == 3:
        Sh.kt_rong()
    elif n == 4:
        Sh.tien_tong()
    elif n == 5:
        Sh.hien_thi()
    elif n == 6:
        Sh.xoa()
    
    thoat = input("bạn có muốn thoát không? (có để thoát): ")
    if thoat.lower() == "có":
        break

#6 - Hình chữ nhật (có hệ số k?)
class Hcn:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def dien_tich(self, k):
        return self.w * self.h * k * k
    
    def chu_vi(self, k):
        return (self.w * k + self.h * k) * 2

a, b, k = map(int, input().split())
h = Hcn(a, b)
print(h.dien_tich(k))
print(h.chu_vi(k))

#7 - Phân số + - * /
import math

class Fraction:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Mẫu số không được bằng 0")
        self.num = num
        self.den = den
        self.simplify()
    
    def simplify(self):
        g = math.gcd(self.num, self.den)
        self.num //= g
        self.den //= g
        if self.den < 0:
            self.num = -self.num
            self.den = -self.den
    
    def add(self, other):
        return Fraction(self.num * other.den + other.num * self.den,
                        self.den * other.den)
    
    def sub(self, other):
        return Fraction(self.num * other.den - other.num * self.den,
                        self.den * other.den)
    
    def mul(self, other):
        return Fraction(self.num * other.num, self.den * other.den)
    
    def div(self, other):
        return Fraction(self.num * other.den, self.den * other.num)
    
    def __str__(self):
        return f"{self.num}/{self.den}"

a, b, op, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
f1 = Fraction(a, b)
f2 = Fraction(c, d)

if op == '+':
    print(f1.add(f2))
elif op == '-':
    print(f1.sub(f2))
elif op == '*':
    print(f1.mul(f2))
elif op == '/':
    print(f1.div(f2))
else:
    print("Phép toán không hợp lệ")

#8 - Tài khoản ngân hàng (menu gửi/rút)
class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = int(balance)
    
    def lenh(self):
        n = int(input())
        for _ in range(n):
            print('----MENU----')
            print('chọn 1: deposit tiền gửi')
            print('chọn 2: withdraw tiền rút')
            choice = int(input())
            
            if choice == 1:
                pluss = int(input('nhập số tiền cần gửi: '))
                self.balance += pluss
            elif choice == 2:
                minus = int(input('nhập số tiền cần rút: '))
                if self.balance >= minus:
                    self.balance -= minus
                else:
                    print('số dư không đủ')
            
            print(f'Chủ tài khoản: {self.owner}, Số dư tài khoản: {self.balance}')

owner, balance = input().split()
acount = Bank(owner, balance)
acount.lenh()

#9 - Điểm trung bình và xếp loại sinh viên
class DiemTrungBinh:
    def __init__(self, name):
        self.name = name
    
    def tinh_diem_tb(self):
        n = int(input())
        tong = 0
        for _ in range(n):
            input("Nhap ten mon hoc: ")  # bỏ qua tên môn
            score = float(input("Nhap diem mon hoc: "))
            tong += score
        return tong / n
    
    def xep_hang(self, avg):
        if avg >= 8:
            return "Good"
        elif 6.5 <= avg < 8:
            return "Average"
        else:
            return "Poor"

ten = input("Nhap ten sinh vien: ")
sv = DiemTrungBinh(ten)
average = sv.tinh_diem_tb()
xep_loai = sv.xep_hang(average)
print(f"Diem trung binh cua {ten} la: {average} xep loai: {xep_loai}")

#10 - Quản lý thư viện (ADD, COUNT, COUNTYEAR)
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
    
    def add(self, book):
        self.books.append(book)
    
    def count_by_author(self, name):
        dem = 0
        for b in self.books:
            if b.author == name:
                dem += 1
        return dem
    
    def find_by_year(self, y):
        dem = 0
        for b in self.books:
            if b.year == y:
                dem += 1
        return dem

n = int(input().strip())
thu_vien = Library()

for _ in range(n):
    line = input().strip()
    if line.startswith("ADD"):
        _, rest = line.split(" ", 1)
        title_part, rest2 = rest.split(";")
        author_part, year_part = rest2.split(",")
        title = title_part.strip()
        author = author_part.strip()
        year = int(year_part.strip())
        thu_vien.add(Book(title, author, year))
    
    elif line.startswith("COUNTYEAR"):
        _, year_str = line.split(" ", 1)
        year = int(year_str.strip())
        print(thu_vien.find_by_year(year))
    
    elif line.startswith("COUNT"):
        _, author = line.split(" ", 1)
        print(thu_vien.count_by_author(author.strip()))

#11 - Góc giữa hai mặt phẳng (vector)
import math

A = list(map(float, input().split()))
B = list(map(float, input().split()))
C = list(map(float, input().split()))
D = list(map(float, input().split()))

AB = [B[i] - A[i] for i in range(3)]
AC = [C[i] - A[i] for i in range(3)]
n1 = [AB[1]*AC[2] - AB[2]*AC[1],
      AB[2]*AC[0] - AB[0]*AC[2],
      AB[0]*AC[1] - AB[1]*AC[0]]

BC = [C[i] - B[i] for i in range(3)]
BD = [D[i] - B[i] for i in range(3)]
n2 = [BC[1]*BD[2] - BC[2]*BD[1],
      BC[2]*BD[0] - BC[0]*BD[2],
      BC[0]*BD[1] - BC[1]*BD[0]]

cos_phi = sum(n1[i]*n2[i] for i in range(3)) / (math.sqrt(sum(x*x for x in n1)) * math.sqrt(sum(x*x for x in n2)))
cos_phi = max(-1, min(1, cos_phi))
phi = math.degrees(math.acos(cos_phi))

print(f"{phi:.2f}")

#12 - Nhân hai số phức
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def multiply(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

r1, i1 = map(float, input().split())
r2, i2 = map(float, input().split())
c1 = ComplexNumber(r1, i1)
c2 = ComplexNumber(r2, i2)
result = c1.multiply(c2)
print(f"{int(result.real)} {int(result.imag)}")

#13 - Diện tích tam giác (Heron)
import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def get_area(self):
        if (self.a + self.b <= self.c or
            self.a + self.c <= self.b or
            self.b + self.c <= self.a or
            self.a <= 0 or self.b <= 0 or self.c <= 0):
            return -1
        
        p = (self.a + self.b + self.c) / 2
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area

canh = list(map(int, input().split()))
tam_giac = Triangle(canh[0], canh[1], canh[2])
dien_tich = tam_giac.get_area()

if dien_tich == -1:
    print("invalid")
else:
    print(f"{dien_tich:.2f}")
