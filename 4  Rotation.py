import matplotlib.pyplot as plt
import math

square = [
    [1,1,1],
    [4,1,1],
    [4,3,1],
    [1,3,1]
]

# Rotation angle
theta = math.radians(90)

# Rotation matrix (Z-axis)
R = [
    [math.cos(theta), -math.sin(theta), 0],
    [math.sin(theta),  math.cos(theta), 0],
    [0, 0, 1]
]

rotated = []

# Manual matrix multiplication (same style)
for p in square:
    p_temp = [0,0,0]
    for i in range(3):
        for j in range(3):
            p_temp[i] += R[i][j] * p[j]
    rotated.append(p_temp)

# Plot
plt.figure(figsize=(6,6))

# Original square
for i in range(4):
    x1,y1 = square[i][0], square[i][1]
    x2,y2 = square[(i+1)%4][0], square[(i+1)%4][1]
    plt.plot([x1,x2],[y1,y2], color='black')

# Rotated square
for i in range(4):
    x1,y1 = rotated[i][0], rotated[i][1]
    x2,y2 = rotated[(i+1)%4][0], rotated[(i+1)%4][1]
    plt.plot([x1,x2],[y1,y2],color='red')

plt.title("Square Rotation (90°)")
plt.grid()
plt.axis('equal')
plt.show()
