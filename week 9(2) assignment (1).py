#!/usr/bin/env python
# coding: utf-8

# Q-1: What is Matplotlib? Why is it used? Name five plots that can be plotted using the Pyplot module of 
# Matplotlib.

# Ans-1 Matplotlib is a widely used python library for creating static , animated , and interactive visualizations in a variety of formats .It provids a high level interface for drawig attractive and informative statistical graphics .It is practicularly well- suited for creating plots such as line plot ,bar plot , scatter plots histogram plots an more.
# 
# FIVE TYPE OF PLOTS:
# 
# 1. LINE PLOT :- Used to visualize the relationship between two continuous variable by connecting data points with lines.
# 
# 2. SCATTER PLOT:- Used to display the relationship between two continuous variable , showing individual data points.
# 
# 3. BAR PLOT :- Suitable for comparing categories of data by displaying vertical bars for each category .
# 
# 4. HISTOGRAM :- Visualizes the distribution of a single variable by dividing the data into bins and displaying  the frequency of each bin.
# 
# 5. PIE CHART:- Represents categorical data in a circular chart , with each category represented as a slice of the pie.

# Q-2: What is a scatter plot? Use the following code to generate data for x and y. Using this generated data 
# plot a scatter plot.
# 
# 

# In[2]:


import numpy as np


np.random.seed(3)

x = 3 + np.random.normal(0, 2, 50)

y = 3 + np.random.normal(0, 2, len(x))


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


plt.plot(x,y)
plt.xlabel("this is my x axis")
plt.ylabel("this is my y axis")
plt.title("this is my title")


# In[6]:


plt.scatter(x,y)


# Q-3: Why is the subplot() function used? Draw four line plots using the subplot() function.
# 
# Use the following data.

# import numpy as np
# 
#  for lie 1: x = np.array([0, 1, 2, 3, 4, 5]) and  y = np.array([0, 100, 200, 300, 400, 500])
# 
# For line 2: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([50, 20, 40, 20, 60, 70])
# 
# For line 3: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([10, 20, 30, 40, 50, 60])
# 
# For line 4: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([200, 350, 250, 550, 450, 150])

# Ans-3 The subplot() function in matlotlib is used to create a grid of subplots within a single figure . This allows you to display multiple plots in a structured layout, making it easier to compare and analyze different aspects of your data.

# In[28]:


A=[ x = np.array([0, 1, 2, 3, 4, 5]),
y = np.array([0, 100, 200, 300, 400, 500])]

 
B=[x = np.array([0, 1, 2, 3, 4, 5]),
y = np.array([50, 20, 40, 20, 60, 70]) ]


C=[ x = np.array([0, 1, 2, 3, 4, 5]),
y = np.array([10, 20, 30, 40, 50, 60])]

D=[ x = np.array([0, 1, 2, 3, 4, 5]),
y = np.array([200, 350, 250, 550, 450, 150])]


fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.scatter(A,B,C,D)
ax.show()


# In[24]:


x=np.random.rand(50)
y=np.random.rand(50)
z=np.random.rand(50)
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.scatter(x,y,z)
ax.show()


# Q-4: What is a bar plot? Why is it used? Using the following data plot a bar plot and a horizontal bar plot. 
# 

# In[30]:


import numpy as np

company = np.array(["Apple", "Microsoft", "Google", "AMD"])

profit = np.array([3000, 8000, 1000, 10000])


# Ans-4 Bar plot , also known as a bar chart or bar graph , is a type of data visualization that represents categoriacal data with rectungular bars.Each bar's length or height is prorpotional to the fraquency or count of the category it.
# 
# REPRESENTS: Bar plots are used to compare and diplay the relative quantities or frequencies of different categories  or group.

# In[31]:


plt.bar(company,profit)
plt.xlabel('company')
plt.ylabel('profit')
plt.title('bar plot')
plt.show()


# In[32]:


plt.barh(company,profit)
plt.xlabel('company')
plt.ylabel('profit')
plt.title('bar plot')
plt.show()


# Q-5: What is a box plot? Why is it used? Using the following data plot a box plot.

# In[34]:


box1 = np.random.normal(100, 10, 200)

box2 = np.random.normal(90, 20, 200)


# Ans-5 A box plot =, aslo known as a whisker plot , is a type of statistical visualization used to display the distribution and spread of a dataset . It provide a summary of key statistical measures ,such as the median , quartiles , and potential outliers.

# In[35]:


plt.boxplot(box1,box2)
plt.xlabel('box1')
plt.ylabel('box2')
plt.title('box plot')
plt.show()


# In[ ]:




