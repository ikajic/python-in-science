import numpy as np
import matplotlib.pyplot as pl

# Load the data into a NumPy array
data = np.genfromtxt('data - Sheet1.csv', delimiter=',', skiprows=1)

# Store the number of rows and number of columns 
nr_rows, nr_cols = data.shape
print "There are %d rows and %d columns"%(nr_rows, nr_cols)

# Get the min, max and average age
ages = data[:, 0]
min_age = np.min(ages)
max_age = np.max(ages)
mean_age = np.mean(ages)

print "The youngest person is ", min_age, " years old."
print "The oldest person is ", max_age, " years old."
print "On average, people are ", mean_age, " years old."

#Print sorted ages
np.sort(ages)

# Get the numer of devices
devices_now = data[:,1]

# Initialize empty array
devices_future = np.zeros(devices_now.shape)

# Double the number of devices
for i in range(len(devices_now)):
  devices_future[i] = 2*devices_now[i]

print "Numbers of devices in 2042:", devices_future

devices_future = np.zeros(devices_now.shape)
devices_future = 2*devices_now

# Watch out for this
a = range(4)
a*2

# Plotting
pl.figure()
pl.plot(ages, label='Ages')
pl.plot(devices_now, label='Devices')
pl.xlabel('Person ID')
pl.title('Data')
pl.legend()

pl.figure()
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
pl.hist(ages, bins, histtype='bar', rwidth=0.8)
pl.ylabel('Number of people')
pl.xlabel('Age')
pl.title('Distribution of ages')


pl.figure()
bins = np.arange(0, 90, 10)
pl.subplot(1,2,1)
pl.title('Distribution of ages')
pl.hist(ages, bins, histtype='bar', rwidth=0.8, color=['crimson'])

pl.subplot(1,2,2)
pl.title('Distribution of devices')
bins_dev = np.arange(0, 30, 5)
pl.hist(devices_now, bins_dev, histtype='bar', rwidth=0.8, color=['burlywood'])

pl.show()
