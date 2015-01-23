import matplotlib.pyplot as plt
import numpy as np
import sys

f = open(sys.argv[1], 'r')

tc = f.readline()
sc = f.readline()

names = []
nums = []

for l in f.readlines():
    s = l.split(" ")
    names.append(s[0])
    nums.append(int(s[1]))


plt.bar(np.arange(len(names)), nums, align="center", width=2)
#plt.xticks(np.arange(len(names)), names, rotation='vertical')

plt.margins(0)
plt.subplots_adjust(bottom=0.3)

plt.title("Successfully Attacked Connections by Hostname")
plt.ylabel("successfully attacked connections")
plt.ylim(0, int(max(nums)+0.1*max(nums)))
plt.show()
