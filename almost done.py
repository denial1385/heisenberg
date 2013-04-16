#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ngibuini
#
# Created:     15/04/2013
# Copyright:   (c) Ngibuini 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from os import curdir
from collections import deque
from time import *
from datetime import datetime
import math

#LISTS
#these are the various lists used in the program:-

proc_list = [ ] #1) which is a list of all the total processes to be simulated prior
                                                #to system initialization

proc_arrival_time_list = [ ] #2) is a list that assigns the new process a
                                                #respective arrival time

proc_service_request_time_list = [ ] #3) is a list that assigns the new process a
                                                #respective service time t orequest for its completion
#

archive_proc_list = [ ] #4) directly copies proc_list for archival sake since the #real proc_list is cleared by popping

archive_proc_arrival_time_list = [ ] #5) directly copies proc_arrival_time_list for #archival sake since the real proc_arrival_time_list is cleared by popping

archive_proc_service_request_time_list = [ ] #6) directly copies proc_service_request_time_list
                                                #for archival sake since the real proc_service_request_time_list is cleared by popping

#LIST SIZES
#list sizes or count of items in lists:-

proc_list_size = 0
proc_arrival_time_list_size = 0
proc_service_request_time_list_size = 0

archive_proc_list_size = 0
archive_proc_arrival_time_list_size = 0
archive_proc_service_request_time_list_size = 0

#Post Arrival Variables

curr_proc = chr
curr_arrival_time = 0
curr_request_time = 0


def main():

    proc_list = deque('abcde')
    proc_arrival_time_list = deque([0, 10, 15, 80, 90])
    proc_service_request_time_list = deque([75, 40, 25, 20, 45])

    proc_list_size = len(proc_list)
    print "This is the list of processes to be simuated today: ",proc_list
    print "This is the number of processes: ",proc_list_size

    proc_arrival_time_list_size = len(proc_arrival_time_list)
    print "This is the list of the arrival times of said processes: ",proc_arrival_time_list
    print "This is the number of arrival times: ",proc_arrival_time_list_size

    proc_service_request_time_list_size = len(proc_service_request_time_list)
    print "This is the list of the service time each respective process requests of the CPU: ",proc_service_request_time_list
    print "This is the number of service times requested: ",proc_service_request_time_list_size,"\n"

    archive_proc_list_size = len(proc_list)


    while archive_proc_list_size>0:

        curr_proc = proc_list.popleft()
        curr_arrival_time = proc_arrival_time_list.popleft()
        curr_request_time = proc_service_request_time_list.pop()

        proc_list_size = len(proc_list)
        print curr_proc
        print curr_arrival_time
        print curr_request_time

        if proc_list_size == 0:
            break

        archive_proc_list_size - 1

    print "Archive process list =",archive_proc_list
    print "Current process is",curr_proc
    print "Current arrival time is",curr_arrival_time
    print "hi"

    pass

if __name__ == '__main__':
    main()
