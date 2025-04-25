import matplotlib.pyplot as plt
x=[10,15,20,25,30,35,40,45,50,55,60,65,70,80]
y=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
x1=[7,14,19,23,27,30,40,33,47,50]
y1=[1,2,3,4,5,6,7,8,9,10]
x2=[55,61,67,73,77,84,64,90,98,100]
y2=[1,2,3,4,5,6,7,8,9,10]
x3=[13000,18000,23000,29000,33000,41000,50000,45000,70000,92000]
y3=[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]

plt.subplot(2,2,1)
plt.plot(x,y,'--b',marker='o',mfc='y',markersize=10)
plt.xlim(10,max(x))
plt.ylim(1,max(y))
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.grid(color='b',linestyle='--',linewidth=0.2)

plt.subplot(2,2,2)
plt.scatter(x1,y1,color='r',marker='o',edgecolors='y',s=100)
plt.xlim(7, max(x1))
plt.ylim(1, max(y1))
plt.xlabel('Avg Temp of Earth')
plt.ylabel('No. of Decades')
plt.title('Scatter')
plt.grid(color='b',linestyle='--',linewidth=0.2)

plt.subplot(2,2,3)
plt.bar(x2,y2,color='red')
plt.xlim(55, max(x3))
plt.ylim(1, max(y3))
plt.xlabel('Average Percentage')
plt.ylabel('Batch No')
plt.title('Bar Chart')
plt.grid(color='b',linestyle='-',linewidth=0.2)

plt.subplot(2,2,4)
plt.hist(x3,bins=10,color='red',edgecolor='black',alpha=0.7)
plt.xlabel('X-axis')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid(color='b',linewidth=0.2)

plt.suptitle('MATPLOT LIBRARY')
plt.subplots_adjust(left=0.1,right=0.9,top=0.9,bottom=0.1,wspace=0.4,hspace=0.4)
plt.show()
