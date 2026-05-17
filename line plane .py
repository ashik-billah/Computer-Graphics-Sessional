import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ----- Plane: 2x + 3y + 5z = 5 -----
x = np.linspace(-2, 5, 10)
y = np.linspace(-2, 5, 10)
X, Y = np.meshgrid(x, y)

Z = (5 - 2*X - 3*Y) / 5

ax.plot_surface(X, Y, Z, alpha=0.5)

# ----- Line -----
t = np.linspace(-2, 2, 100)

x = 2 + t
y = 1 + 2*t
z = 3 + 3*t

ax.plot(x, y, z, color='red')

# ----- Intersection -----
# solve: 2(2+t) + 3(1+2t) + 5(3+3t) = 5
t = -17/23

x = 2 + t
y = 1 + 2*t
z = 3 + 3*t

ax.scatter(x, y, z, color='black', s=60)

# labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()