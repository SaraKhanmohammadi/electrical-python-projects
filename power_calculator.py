# power_calculator.py
# اولین پروژه پورتفولیو هوش مصنوعی من
# آذر ۱۴۰۴

v = float(input("ولتاژ (V): "))
i = float(input("جریان (A): "))
cos_phi = float(input("ضریب توان (پیش‌فرض ۱): ") or "1")

p = v * i * float(cos_phi)
print(f"\nتوان اکتیو = {p:.1f} وات")
print("پروژه ۱ از ۱۲ — شروع تغییر مسیر به AI")
