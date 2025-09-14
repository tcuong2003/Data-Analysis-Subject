import math

print("Tính chu vi và diện tích hình tròn")
r = float(input("Nhập bán kính r: "))

cv = 2 * math.pi * r
dt = math.pi * r**2

print("Bán kính r = %.2f" % r)
print("Chu vi = %.2f" % cv)
print("Diện tích = %.2f" % dt)
