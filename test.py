import numpy as np

file = open('2014-11-21to2014-11-21')
print 'file loaded'
mat = np.loadtxt(file,'string')

unique_station = np.unique(mat[:,5])
print unique_station
print unique_station[0]

station_list = np.copy(mat[:,5])
users = mat[:,0]

result = {}

count = 0

for station in unique_station:
    result[station] = np.unique(users[station_list == station])
    if not count%10:
        print "%d of %d" % (count,len(unique_station))
    count = count + 1

length_list = []

for station in result.keys():
    length_list.append(len(result[station]))

length_list.sort()
print length_list