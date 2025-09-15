import math

def azimut(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    angle_rad = math.atan2(dx, dy)   # atan2(dx, dy) → orientación geográfica
    angle_deg = math.degrees(angle_rad)
    return angle_deg % 360

# Ejemplo:
p1 = (100, 200)
p2 = (120, 230)

print(f"Azimut de P1 a P2: {azimut(*p1, *p2):.2f}°")
