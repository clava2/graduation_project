""" import numpy as np

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

idx = np.argsort(length_list)

max_population_station = []

for index in idx[-500:]:
    max_population_station.append(result.keys()[index])

population_in_station = []
for station in max_population_station:
    population_in_station.extend(result[station])


population_count = 0
 "population count = %d" %population_count

print "length of population_in_station: %d" %(len(population_in_station))

np.unique(population_in_station)

print len(population_in_station)or index in idx[-500:]:
 "population count = %d" %population_count

print "length of population_in_station: %d" %(len(population_in_station))

np.unique(population_in_station)

print len(population_in_station)   population_count = population_count + length_list[index]
 "population count = %d" %population_count

print "length of population_in_station: %d" %(len(population_in_station))

np.unique(population_in_station)

print len(population_in_station)
 "population count = %d" %population_count

print "length of population_in_station: %d" %(len(population_in_station))

np.unique(population_in_station)

print len(population_in_station)rint "population count = %d" %population_count

print "length of population_in_station: %d" %(len(population_in_station))

np.unique(population_in_station)

print len(population_in_station) """



# the following code is used to filter the original data, find the station which has
# most population

""" import numpy as np
from functions import *

file = open('2014-11-21to2014-11-21')
mat = read_file(file)

print "file loaded"

station_dict = get_station_user_dict(mat)

print "station dict generated!"

selected_station = select_station(station_dict)

print "selected station!"

filtered_mat = filter_by_station(mat,station_dict.keys())

print "filtered station!"

np.savetxt('filtered_mat.txt',filtered_mat) """


#the floolwing code is used to set up the user path dictionary

""" from functions import *
import json

file = open('2014-11-21to2014-11-21')
mat = read_file(file)
unique_user = get_unique_user(mat)
print unique_user
print len(unique_user)
user_path_dict = get_user_path_dict(mat)
meeting_mat = get_meeting_mat(user_path_dict) """

from functions import *

file = open('2014-11-21to2014-11-21')
mat = read_file(file)
unique_user = get_unique_user(mat)
print len(unique_user)
unique_station = get_unique_station(mat)
print len(unique_station)
print generate_keys(unique_station)