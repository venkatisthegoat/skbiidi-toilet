#!/usr/bin/env python
# coding: utf-8

# In[5]:

#21-10-2024
import matplotlib.pyplot as plt
#Define the points
x = [2, 5]
y = [9, 10]
#Create the line chart

plt.plot(x, y, marker = "p", color= "blue", linestyle="--")

#Add titles and labels
plt.title("Line chart from (2,5) to (9,10)")
plt.xlabel("X-axis")
plt.ylabel("Y-Axis")
plt.xlim(0,10)
plt.ylim(0,11)
plt.grid()
plt.show()


# In[6]:

#21-10-2024
import statistics
ages = [20, 35, 32, 40, 70 ,72, 64, 50]

mean = statistics.mean(ages)
median = statistics.median(ages)
mode = statistics.mode(ages)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")


# In[ ]:

#28-10-2024
list1 = [1, 2, 3]
list2 = [4, 5, 6]
added_list = []
for i in range(len(list1)):
    added_list.append(list1[i] +  list2[i])
    
print(added_list)

