import math

def azimut(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    angle_rad = math.atan2(dx, dy)  # atan2(dx, dy) → orientación geográfica
    angle_deg = math.degrees(angle_rad)
    return angle_deg % 360

# Pedir coordenadas por teclado
x1 = float(input("X1: "))
y1 = float(input("Y1: "))
x2 = float(input("X2: "))
y2 = float(input("Y2: "))

print(f"Azimut de P1 a P2: {azimut(x1, y1, x2, y2):.2f}°")

