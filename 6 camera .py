import matplotlib.pyplot as plt
import numpy as np

fx, fy = 800, 800
cx, cy = 320, 240
k = [[fx, 0, cx],
     [0, fy, cy],
     [0, 0, 1]]
theta = np.radians(90)
C = [0, 0, 0]
R = [[np.cos(theta), -np.sin(theta), 0],
     [np.sin(theta), np.cos(theta), 0],
     [0, 0, 1]]
cube = [
    [1, 1, 5], [2, 1, 5], [2, 2, 5], [1, 2, 5],
    [1, 1, 6], [2, 1, 6], [2, 2, 6], [1, 2, 6]
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

projected = []
for p in cube:
    p_temp = [p[0] - C[0],
              p[1] - C[1],
              p[2] - C[2]]
    pc = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            pc[i] += R[i][j] * p_temp[j]
    p_img = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            p_img[i] += k[i][j] * pc[j]
    u, v = p_img[0] / p_img[2], p_img[1] / p_img[2]
    projected.append([u, v])

plt.figure(figsize=(10, 6))

ax1 = plt.subplot(121, projection='3d')
for i, p in enumerate(cube):
    ax1.scatter(p[0], p[1], p[2], color='black')
    ax1.text(p[0] + 0.01, p[1] + 0.01, p[2] + 0.01, str(i), color='blue')

for e in edges:
    p1 = cube[e[0]]
    p2 = cube[e[1]]

    ax1.plot([p1[0], p2[0]],
             [p1[1], p2[1]],
             [p1[2], p2[2]], color='black')
    ax1.set_title("Before Camera Projection (3D Cube)")

# =====================================================
# RIGHT: 2D PROJECTION (AFTER)
# =====================================================
ax2 = plt.subplot(1, 2, 2)

# edges
for e in edges:
    p1 = projected[e[0]]
    p2 = projected[e[1]]

    ax2.plot([p1[0], p2[0]],
             [p1[1], p2[1]])

# points + labels
for i, p in enumerate(projected):
    ax2.scatter(p[0], p[1])
    ax2.text(p[0] + 2, p[1] + 2, str(i), color='blue')

# camera center
ax2.scatter(cx, cy, color='red')
ax2.text(cx, cy, "Center")

ax2.set_title("After Camera Projection (2D Image)")
# ax2.invert_yaxis()
ax2.grid()

plt.show()

