#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ngibuini
#
# Created:     14/04/2013
# Copyright:   (c) Ngibuini 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from os import curdir
from collections import deque
from time import *
from datetime import datetime
import math

#**********************************

arrival_time = 0
dispatcher_time = 0
adjusted_dispatcher_time = 0
remaining_time = 0
request_time = 0
time_quantum = 10
temp_time_quantum = 0           #when a process completes before the end of a TQ
process_done = 0

#LISTS
#these are the various lists used in the program:-

proc_list = [ ] #1) which is a list of all the total processes to be simulated prior
                                                #to system initialization

proc_arrival_time_list = [ ] #2) is a list that assigns the new process a
                                                #respective arrival time

proc_service_request_time_list = [ ] #3) is a list that assigns the new process a
                                                #respective service time t orequest for its completion
ready_list = [ ]
ready_list_request_time_list = [ ]

execution_list = []
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

execution_list_size = 0

archive_proc_list_size = 0
archive_proc_arrival_time_list_size = 0
archive_proc_service_request_time_list_size = 0

ready_list_size = 0

#Post Arrival Variables

curr_proc = chr
curr_arrival_time = 0
curr_request_time = 0

curr_proc_ready = bool
next_proc_ready = bool

has_not_been_executed = bool
has_been_executed = bool

curr_proc_done = bool

hold = bool





stack = [ ]


#**************************************************************
#
#**************************************************************


#**********************************
#**********************************

def main():

    hold = False


    dispatcher_time = 0
    #dispatcher_time = adjusted_dispatcher_time
    #arrival_time = 90
    #request_time = 50
    #max_processes = 3
    #max_request_time = 50

    arrival_time = curr_arrival_time
    remaining_time = curr_request_time

    temp_time_quantum = time_quantum
    curr_proc_ready = True

    next_proc_ready = False
    has_been_executed = False
    has_not_been_executed =True

    print "There are",execution_list_size,"processes to be executed."

    if execution_list_size == 0:
        has_been_executed = False

    else:
        dispatcher_time = adjusted_dispatcher_time

    if (arrival_time>dispatcher_time):

                print "Process is not here"
                next_proc_ready = False
                print "Or is it? \/ This shoud be False!"
                print next_proc_ready
                print "Has it been executed?"
                print has_been_executed

                print "I shall arrive at", curr_arrival_time

                #print "Remaining time:",remaining_time
                #dispatcher_time = dispatcher_time + time_quantum
                print "After accounting for other processes, dispatcher time is:",dispatcher_time

    elif(arrival_time==dispatcher_time):
            print "\nProcess is here"

            next_proc_ready = True
            has_been_executed = False

            print "Are you sure its here?"
            print next_proc_ready

            print "Has it been executed? If above is true, this should be true as well, otherwise break!"
            print has_been_executed

            print "I will execute you now or next!"

            #print curr_proc
            #ready_list.append(curr_proc)
            ready_list_request_time_list.append(curr_request_time)


            print "Initial execution time is",dispatcher_time

            #print "I will break to execute! "
            if hold == True:
                dispatcher_time = dispatcher_time + temp_time_quantum
                execute()
                has_been_executed = True
            elif hold == False:
                execute()
##                if(arrival_time==dispatcher_time):
##                    print "\nProcess is here"
##                    print "\nInitial execution at discrete time",dispatcher_time
##                    next_proc_ready = True
##          has_been_executed = False

    else:
##        if next_proc_ready == True:
##            print "I will break to execute the new process"

        curr_proc = execution_list.popleft()

        if next_proc_ready == False:

            print "I will keep executing since no one else is here..."
            print "\n***********\nIt is now",dispatcher_time
            print "My request time is",remaining_time

            if remaining_time > process_done:

                if(remaining_time-time_quantum)<time_quantum:

                            print "This will finish before the end of the time quantum!"
                            temp_time_quantum = remaining_time-time_quantum

                            #THIS MEANS THAT IF A PROCESS GETS DONE BEFORE THE
                            #TIME QUANTUM EXPIRES, THE NEXT PROCESS SHALL BE
                            #BEGIN, USING A FULL TIME QUANTUM

                            hold = True
                            execute()
                            curr_proc_done = True
                            print "Process completed",execution_list.pop()


                else:
                            print "Execute!"
                            execute()
                            has_been_executed = True
                            print "Execute done."

                            print "Here-Remaining time:",remaining_time,"\n"
                            adjusted_dispatcher_time = dispatcher_time + time_quantum

            elif remaining_time == process_done:
                print "Process",curr_proc,"completed at time",adjusted_dispatcher_time

            else:

                print "Request time is",remaining_time
                print "Process is done"

                print "After-Dispatcher time:",dispatcher_time
                print "Exiting dispatcher time is",dispatcher_time
                print "Finito\n\n******************************************************\n\n\o/ PROCESS DONE!\n"
                print "\n******************************************************\n"

        #else:
pass

def execute():

    hold = True
    execution_list.append(curr_proc)
    request_time = curr_request_time - time_quantum

    adjusted_dispatcher_time = dispatcher_time + temp_time_quantum

pass

def complete():


    execution_list.pop

pass


#************************************************************
#
#
#
#************************************************************


if __name__ == '__main__':

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

    execution_list = deque([ ])

    dispatcher_time = 0

    while archive_proc_list_size>0:

        curr_proc = proc_list.popleft()
        curr_arrival_time = proc_arrival_time_list.popleft()
        curr_request_time = proc_service_request_time_list.popleft()

        proc_list_size = len(proc_list)
        print curr_proc
        print curr_arrival_time
        print curr_request_time

        curr_proc = ready_list.append(curr_proc)

        main()
        dispatcher_time = dispatcher_time + temp_time_quantum
        if proc_list_size == 0:
            break

        archive_proc_list_size - 1

    print "Archive process list =",archive_proc_list
    print "Current process is",curr_proc
    print "Current arrival time is",curr_arrival_time
    print "hi"


