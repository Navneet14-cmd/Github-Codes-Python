import matplotlib.pyplot as plt
x=[10,15,20,25,30,35,40,45,50,55,60,65,70,80]
y=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
x1=[7,14,19,23,27,30,40,33,47,50]
y1=[1,2,3,4,5,6,7,8,9,10]
x2=[55,61,67,71,84,88,90,93,98,100]
y2=[1,2,3,4,5,6,7,8,9,10]
x3=[1300,1800,2300,2900,3300,4100,5000,4500,7000,9200]
y3=[2,4,6,8,10,12,14,16,18,19,20]




plt.subplot(2,2,1)
plt.plot(x2,y,'--b',marker='o',mfc='y',markersize=10)
plt.xlim(10,max(x2))
plt.ylim(1,max(y))
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph')
plt.grid(color='b',linestyle='--',linewidth='0.2')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.4)

plt.subplot(2,2,2)
plt.plot(x1,y1,'r',marker='o',mfc='y',markersize=10)
plt.xlim(7,max(x2))
plt.ylim(1,max(y))
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
#plt.title('Graph')
plt.grid(color='b',linestyle='--',linewidth='0.2')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.4)


plt.subplot(2,2,3)
plt.bar(x2,y2,'r',marker='o',mfc='y',markersize=10)
plt.xlim(7,max(x2))
plt.ylim(1,max(y))
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
#plt.title('Graph')
plt.grid(color='b',linestyle='--',linewidth='0.2')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.4)

plt.subplot(2,2,4)
plt.hist(x3,y3,'r',marker='o',mfc='y',markersize=10)
plt.xlim(7,max(x2))
plt.ylim(1,max(y))
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
#plt.title('Graph')
plt.grid(color='b',linestyle='--',linewidth='0.2')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.4)

plt.show()

