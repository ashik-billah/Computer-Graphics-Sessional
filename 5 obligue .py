import matplotlib.pyplot as plt
import numpy as np

cube = [[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,1],[1,0,1],[0,1,1],[1,1,1]]
edge = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,7),(7,6),(6,4),(0,4),(1,5),(2,7),(3,6)]

def oblique(points,alpha,L):
    alpha = np.radians(alpha)
    projected=[]
    for x,y,z in points:
        x_new = x + L *z * np.cos(alpha)
        y_new = y + L * z * np.sin(alpha)
        projected.append([x_new,y_new])
    return np.array(projected)

alpha = 45
L = 0.5
pro_cube = oblique(cube,alpha,L)

fig = plt.figure()
ax1 = fig.add_subplot(121,projection='3d')
for i,p in enumerate(cube):
    ax1.scatter(p[0],p[1],p[2],color='red')
    ax1.text(p[0]+0.01,p[1]+0.01,p[2]+0.01,str(i),color='blue')
for e in edge:
    p1 = cube[e[0]]
    p2 = cube[e[1]]
    ax1.plot([p1[0],p2[0]],
             [p1[1],p2[1]],
             [p1[2],p2[2]],color='black')
ax1.set_title("3D cube")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

ax2 = fig.add_subplot(122)
for i,p in enumerate(pro_cube):
    ax2.scatter(p[0],p[1],color='red')
    ax2.text(p[0]+0.01,p[1]+0.01,str(i),color='blue')
for e in edge:
    p1 = pro_cube[e[0]]
    p2 = pro_cube[e[1]]
    ax2.plot([p1[0],p2[0]],
             [p1[1],p2[1]],color='black')
ax2.set_title("Oblique Projection (2D)")
ax2.set_xlabel("X'")
ax2.set_ylabel("Y'")
ax2.axis('equal')

plt.tight_layout()
plt.show()
