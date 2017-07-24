import matplotlib.pyplot as plt
import numpy as np

config_file = 'config.txt'
with open(config_file,'r') as fp:
    line = ' '
    while line:
        line = fp.readline()
        line = line.strip()

        if line.startswith('file1:'):
            before, file1 = line.split('file1:')
            file1 = file1.strip()
        elif line.startswith('file2:'):
            before, file2 = line.split('file2:')
            file2 = file2.strip()
        elif line.startswith('***'):
            break
fp.close()

# y1 y2
y1_points = []
y2_points = []

fp1 = open(file1, 'r')
line = ' '
while line:
    line = fp1.readline()
    line = line.strip()
    if line:
        y1_points.append(int(line))
fp1.close()

fp2 = open(file2, 'r')
line = ' '
while line:
    line = fp2.readline()
    line = line.strip()
    if line:
        y2_points.append(int(line))
fp2.close()

# x
num = len(y1_points)
xpoints = range(num)

# plot
plt.rc('xtick', labelsize=8) 
plt.rc('ytick', labelsize=8)

fig, ax = plt.subplots()
ax.plot(xpoints, y1_points, 'b', xpoints, y2_points, 'r', linewidth=1)
# ax.set_xticks([0,20,40,60,80,100,120])
# ax.set_yticks(range(25,35))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(['anchor','proposed'])

plt.grid(True)
plt.show()