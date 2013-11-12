Simple data analysis using NumPy and plotting using Matplotlib
===


In this introductory tutorial we will learn how to load a text file containing numerical data into a [NumPy](http://www.numpy.org/) array, 
analyze it and finally plot it using [Matplotlib](http://matplotlib.org/). 
To write Python commands we will use interactive Python console [IPython](http://ipython.org/).


Getting necessary packages
---
For **Windows** users the most convenient way to get IPython, NumPy and Matplotlib is to 
download the [Canopy](https://www.enthought.com/products/canopy/) installation file. 
Depending on your operating system type, you will need either 32-bit or 64-bit version.
If you're unsure which version to download you can find the information by right click on `My Computer` and `Properties`.
Canopy file contains much more packages than needed for this exercise, 
but if you decide to do the other one it will be useful.

**Linux** users can get the packages by entering the following command in Terminal:
```
sudo apt-get install python-numpy python-scipy python-matplotlib ipython 

```

For **Mac** users there is [Macports](http://www.macports.org/). After installing it run the following command in Terminal:
```
sudo port install py27-numpy py27-scipy py27-matplotlib py27-ipython
```


Get the data
---
Our data is stored as a Google spreadsheet and you can download it [here](https://docs.google.com/spreadsheet/ccc?key=0ArfNOZkGFBb0dGpyVVhGY1ZNMDh1dE5HMzRrQTk0YVE&usp=sharing). 
To download the spreadsheet, click on `File` and `Download as` > `Comma Separated Values`. 
Comma Separated Values is another format of a simple text file, where values are separated by commas (surprising!). 
There's nothing special about a `.csv` format, you can think of it as a it's a bit nicer `.txt` file.
Feel free to take a look at it using your favorite text editor.

The spreadsheet contains some made up data: in the first column we have listed ages and in the second 
column the number of electronic devices. Each row in the column corresponds to data from one person.


Load the data
---
Start your IPython console and import the NumPy and matplotlib package:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Load the data with the following command:
```python
data = np.genfromtxt('data - Sheet1.csv', delimiter=',', skiprows=1)
```

In this example, our data is stored in a file called `data - Sheet1.csv` and 
we tell NumPy function `genfromtxt` to read the data which is separated by commas to skip the first row which 
contains two strings: `Age` and `Electronic devices`. 
If at any point in the future we forget how to use this function, we can remind ourselves by using IPython's built in help function:
```python
np.genfromtxt?
```

To make sure that our data is indeed what we had in the spreadsheet, 
print the data, print the data type and its dimensions by simply typing in the two following commands:
```python
data
type(data)
data.shape
```
Notice that there is a dot `.` in the output, this means our numbers are stored as floating-point numbers. 
To write `1.` is a lazy way of writing `1.0` and it's pretty common. 

Executing `data.shape` returns the number of rows and number of colums. 
We say that our NumPy array `data` has two dimensions with the number of rows being the first, and the number of columns the second.

To access the first row, aka data from the first person:

```python
data[0,:]
```

Remember, to access the first row we use the index 0 because indexing in Python starts with 0. 
`:` simply means give me everything in that row.
If we want to know how many electronic devices this person has we type:
```
data[0,1]
```

How to get all the ages? Well, knowing that `:` gives us everything, this is easy:
```python
data[:,0]
```

Navigate using the `cd` (change directory) command to the folder where the downloaded .csv file is contained. 
To see in which folder you are at the moment use the `pwd` (print working directory). 
If you want to list all the files contained in the folder use `ls`.


Let's analyze
---
So, we have our data ready and we would like to know who is the youngest, who is the oldest and what's the mean age. 
Well, that's easy:

```python
ages = data[:,0]
min_age = np.min(ages)
max_age = np.max(ages)
mean_age = np.mean(ages)

print "The youngest person is ", min_age, " years old."
print "The oldest person is ", max_age, " years old."
print "On average, people are ", mean_age, " years old."
```

Obtaining the standard deviation is also easy:
```python
np.std(data)
```

Let's sort the ages in ascending order:
```python
np.sort(ages)
```

Let's say we are teleported in the future, year 2042 where everyone has twice as much devices as we have today.
Based on our data, the number of devices in 2013 for a list of people are:
```
devices_now = data[:,1]
```

How wold we compute the number of devices `devices_future` in the future?
Fist, let's initialize an empty NumPy array that has the same number of elements as `devices_now`:

```python
devices_future = np.zeros(devices_now.shape)
```

One way is to use a for loop, and multiply each element in the arrray `devices_now` by 2.
This is the way to do it:
``` python
for i in range(len(devices_now)):
  devices_future[i] = 2*devices_now[i]

print "Numbers of devices in 2042:", devices_future
```

Whoa, that's a lot of code! Well, NumPy comes to rescue here and we can replace the code by this line:
```python
devices_future = 2*devices_now
```
Not only is this much nicer to read, but it's also much faster. 
Notice that if we were using build-in Python list of integers we would get something different if we used the same syntax.
Here we're using `range` to create a list of 4 subsequent integers. Check this out:

```python
a = range(4)
a*2
```

When not sure if dealing with lists or NumPy arrays, use `type`.

Plotting
---
Let's make some nice simple plots. First, we can plot our two arrays:
```python
pl.figure()
pl.plot(ages, label='Ages')
pl.plot(devices_now, label='Devices')
pl.xlabel('Person ID')
pl.title('Data')
pl.legend()
```

This looks nice but it's not so informative, let's try something else. How about plotting distribution of ages using histograms?
We split our bins into equally spaced intervals of 10 years.

```python
pl.figure()
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
pl.hist(ages, bins, histtype='bar', rwidth=0.8)
pl.ylabel('Number of people')
pl.xlabel('Age')
pl.title('Distribution of ages')
```

Much better! How about using the PyLadies color?

```
pl.hist(ages, bins, histtype='bar', rwidth=0.8, color=['crimson'])
```



