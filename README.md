# Django Bike Shop E-Commerce Website
นี่คือเว็บไซต์อีคอมเมิร์ซสำหรับขายจักรยานออนไลน์ที่สร้างขึ้นด้วย Django (Python)

## คุณสมบัติของโปรเจคนี้

### A. ผู้ใช้ Admin สามารถทำได้
1. จัดการหมวดหมู่ (เพิ่ม, อัปเดต, กรอง, และ ลบ)
2. จัดการสินค้า (เพิ่ม, อัปเดต, กรอง, และ ลบ)
3. จัดการผู้ใช้ (อัปเดต, กรอง, และ ลบ)
4. จัดการคำสั่งซื้อ (ดูและ ประมวลผล)

### B. ผู้ใช้ทั่วไปที่ไม่ได้ลงทะเบียนสามารถทำได้
1. ดูสินค้า (สามารถกรองตามหมวดหมู่ได้)
2. สำรวจรายละเอียดสินค้าและสินค้าที่เกี่ยวข้อง


### C. ผู้ใช้ที่ลงทะเบียนได้ทำได้
1. ทุกอย่างของผู้ใช้ทั่วไป
2. เพิ่มในตะกร้า
3. ชำระเงิน (Cash on Delivery)
4. ดูสถานะคำสั่งซื้อ
5. ดูประวัติคำสั่งซื้อ
6. อัปเดตโปรไฟล์
7. เปลี่ยนรหัสผ่าน
8. รีเซ็ตรหัสผ่าน

## วิธีการติดตั้งและรันโปรเจคนี้?

### การเตรียมพร้อมก่อน:
1. ติดตั้ง Git Version Control
[ https://git-scm.com/ ]

2. ติดตั้ง Python เวอร์ชันล่าสุด
[ https://www.python.org/downloads/ ]

3. ติดตั้ง Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*ทางเลือกของ Pip คือ Homebrew*

### การติดตั้ง
**1. สร้างโฟลเดอร์ที่คุณต้องการเก็บโปรเจค**

**2. สร้าง Virtual Environment และเปิดใช้งาน**

ติดตั้ง Virtual Environment ก่อน
```
$  pip install virtualenv
```

สร้าง Virtual Environment

สำหรับ Windows
```
$  python -m venv venv
```
สำหรับ Mac
```
$  python3 -m venv venv
```

เปิดใช้งาน Virtual Environment

สำหรับ Windows
```
$  source venv/scripts/activate
```

สำหรับ Mac
```
$  source venv/bin/activate
```

**3. โคลนโปรเจคนี้**
```
$  git clone https://github.com/godzillafiw/djungo-bike-shop.git
```

จากนั้น เข้าไปในโปรเจค
```
$  cd django-bike-shop
```

**4. ติดตั้ง Requirements จาก 'requirements.txt'**
```python
$  pip install -r requirements.txt
```

**5. พิ่ม hosts**

- เข้าไปที่ไฟล์ settings.py
- บน allowed hosts, เพิ่ม [‘*’].
```python
ALLOWED_HOSTS = ['*']
```
*ไม่จำเป็นต้องเปลี่ยนแก้สำหรับ Mac*


**6. รันเซิร์ฟเวอร์**

คำสั่งสำหรับ PC:
```python
$ python manage.py runserver
```

คำสั่งสำหรับ Mac:
```python
$ python3 manage.py runserver
```

**7. ข้อมูลการเข้าสู่ระบบ**

สร้าง Super User (Admin)

คำสั่งสำหรับ PC:
```
$  python manage.py createsuperuser
```

คำสั่งสำหรับ Mac:
```
$  python3 manage.py createsuperuser
```
จากนั้น เพิ่มอีเมล์, ชื่อผู้ใช้, และรหัสผ่าน