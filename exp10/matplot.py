import matplotlib.pyplot as plt
x=[10,15,20,25,30,35,80]
y=[1,2,3,4,5,6,7]
x1=[7,14,19,23,27,30,40]
y1=[1,2,3,4,5,6,7]

plt.plot(x,y,'r',marker='o',mfc='y',markersize=10)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph')
plt.grid(color='b',linestyle='--',linewidth='0.2')
plt.plot(x1,y1,'r',marker='o',mfc='y',markersize=10)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph')
plt.grid(color='b',linestyle='--',linewidth='0.2')
plt.show()
