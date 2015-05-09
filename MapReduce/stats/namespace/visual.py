#!/usr/bin/python

###############################################
#    Visualization for namespace histogram    #
#                                             #
#    Maya Rotmesnch                           #
###############################################


import matplotlib.pyplot as plt
import numpy as np

# get results
f = open("results", "r")
namespace = []
count = []
for line in f:
   new = line.strip().split('\t')
   namespace.append(new[0])
   count.append(int(new[1]))
f.close()

# get decoding information
namespace_helper = open("namespace_helper.txt", "r")
namespace_dict = {}
namespace_helper.readline() # ignore comment line
for i in namespace_helper:
    clean = i.strip().split(":")
    namespace_dict[clean[0]] = clean[1]
namespace_helper.close()


# sort results
together = zip(namespace,count)
ordered = sorted(together, key=lambda x: x[1])
namespace, count = zip(*ordered)

# plot results
pos = np.array(range(len(count)))+0.5

plt.figure(figsize=(20,10))
plt.barh(pos,np.log(count))
plt.yticks(pos, [namespace_dict[i] for i in namespace])
plt.xlabel('Log of Page count')
plt.title("Histogram of pages per namespace (logged)")
plt.savefig('Histogram of pages per namespace (logged).png')

