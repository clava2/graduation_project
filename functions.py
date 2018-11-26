import numpy as np
import progressbar as pb

def read_file(file):
    mat = np.loadtxt(file,'string')
    return mat

def get_station_user_dict(mat):
    station_list = mat[:,5]
    unique_station = np.unique(station_list)
    station_dict = {}
    users = mat[:,0]
    pBar = pb.ProgressBar().start()
    total = len(unique_station)
    for i in range(total):
        station_dict[unique_station[i]] = np.unique(users[station_list == unique_station[i]])
        pBar.update(int(i*100/total))
    pBar.finish()

        
    return station_dict

def select_station(station_dict):
    length_list = []

    for station in station_dict.keys():
        length_list.append(len(station_dict[station]))
    idx = np.argsort(length_list)
    max_population_station = []
    for index in idx[-500:]:
        max_population_station.append(station_dict.keys()[index])
    return max_population_station

def filter_by_station(mat,unique_station):
    filtered_mat = []
    print "start_iteration"
    count = 0
    pBar = pb.ProgressBar().start()
    total = len(mat)
    for row in mat:
        if row[5] in unique_station:
            filtered_mat.append(row)
        count = count + 1
        pBar.update(int(count*100/total))
    return filtered_mat

def get_unique_user(mat):
    user_list = mat[:,0]
    user_list = np.unique(user_list)
    return user_list

def get_user_path_dict(mat):
    data_length = len(mat)
    user_path_dict = {}
    widgets = ['Progress:',pb.Percentage(),' ',pb.Bar('#'),' ',pb.Timer(),' ',pb.ETA(),' ',pb.FileTransferSpeed()]
    pBar = pb.ProgressBar(widgets=widgets).start()
    unique_user = get_unique_user(mat)
    user_number = len(unique_user)

    print "generating user dict..."

    dtype = [('StartingTime','S8'),('StationID','S9')]

    for index in range(user_number):
        user_path_dict[unique_user[index]] = []
        pBar.update(index*100/user_number)
    pBar.finish()

    print "generating user path dict..."

    pBar = pb.ProgressBar(widgets = widgets).start()
    for index in range(data_length):
        user_path_dict[mat[index,0]].append((mat[index,2],mat[index,5]))
        pBar.update(index*100/data_length)

    pBar.finish()

    print "sorting user_path_dict ..."

    pBar = pb.ProgressBar(widgets = widgets).start()
    for index in range(user_number):
        user_path_dict[unique_user[index]].sort()
        pBar.update(index*100/user_number)
    pBar.finish()
    return user_path_dict

def is_time_overlapped(start_time1,end_time1,start_time2,end_time2):
    if ((start_time1 < start_time2) and (start_time2 < end_time1)) or ((start_time1 > start_time2) and (start_time1 < end_time2)):
        return True
    return False

def is_user_meeting(user_1_path,user_2_path):
    if (len(user_1_path) == 1) or (len(user_2_path) == 1):
        return False
    user_1_node_number = len(user_1_path)
    user_2_node_number = len(user_2_path)
    for user_1_index in range(user_1_node_number-1):
        for user_2_index in range(user_2_node_number-1):
            if is_time_overlapped(user_1_path[user_1_index][0],user_1_path[user_1_index+1][0],user_2_path[user_2_index][0],user_2_path[user_2_index+1][0]):
                return True

def get_meeting_mat(user_path_dict):
    unique_user = user_path_dict.keys()
    user_number = len(unique_user)
    triple = [[False]*user_number]*user_number
    widgets = ['Progress:',pb.Percentage(),' ',pb.Bar('#'),' ',pb.Timer(),' ',pb.ETA(),' ',pb.FileTransferSpeed()]
    pBar = pb.ProgressBar(widgets = widgets).start()

    for row_index in range(user_number):
        for col_index in range(user_number):
            triple[row_index][col_index] = is_user_meeting(user_path_dict[unique_user[row_index]],user_path_dict[unique_user[col_index]])
            pBar.update((row_index*user_number+col_index)*100/user_number/user_number)
        print row_index
    pBar.finish()
    return triple

def is_time_between(test_time,start_time,end_time):
    if start_time <= test_time <= end_time:
        return True
    return False

def get_unique_station(mat):
    return np.unique(mat[:,5])

def generate_keys(station_list):
    keys = []
    for station in station_list:
        for time in range(60*60*24):
            keys.append(station+str(time))
