import matplotlib.pyplot as plt

p = [1,2,1]
tx,ty = 3,4
T = [[1,0,tx],
     [0,1,ty],
     [0,0,1]]
translated = [0,0,0]
for i in range(3):
    for j in range(3):
        translated[i] += T[i][j] * p[j]

x_new, y_new = translated[0], translated[1]
print(f"Original point : ({p[0]},{p[1]})")
print(f"Translated point : ({x_new},{y_new})")

plt.figure(figsize=(6,6))
plt.scatter(p[0],p[1],color='black')
plt.text(p[0]+0.01,p[1]+0.01,f"Original point : ({p[0]},{p[1]})")

plt.scatter(x_new,y_new,color='black')
plt.text(x_new+0.01,y_new+0.01,f"Translated point : ({x_new},{y_new})")

plt.arrow(p[0],p[1],tx,ty,head_width=0.3,length_includes_head=True)
plt.xlim(0,10)
plt.ylim(0,10)
plt.title("Translation")
plt.grid()
plt.show()

