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
remaining_time = 0
request_time = 0
time_quantum = 10
process_done = 0

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

init_proc_ready = True
next_proc_ready = False
has_been_executed_on = False
has_been_completed = bool
still_more = True

curr_proc = chr
curr_arrival_time = 0
curr_request_time = 0

amount_of_iterations = math.ceil(0.0)
iteration_into_next_time_quantum = 0
actual_iteration = 0.0
total_iterations = 0.0

execute_counter = 0.0

turnaround_time = 0.0

exec_list = [ ]
request_time_in_exec_list = [ ]

exec_list_size = 0

#**************************************************************
#
#**************************************************************

##def timertimer():
##
##    dispatcher_time = dispatcher_time + time_quantum
##
##pass

#**********************************
#**********************************

def main():

    init_proc_ready = True
    next_proc_ready = False
##    has_been_executed_on = False
##    has_been_completed = False
##    still_more = True


    dispatcher_time = 0
    #arrival_time = 0
    #request_time = 45
    #curr_arrival_time = 0
    #curr_request_time = 45

    turnaround_time = 0

    execute_counter = 0
    arrival_time = curr_arrival_time

    remaining_time = curr_request_time

    print "Commencio"





    while(arrival_time>dispatcher_time):

        if(arrival_time>dispatcher_time):
            print "Process is not here"
            print "Remaining time:",remaining_time
            dispatcher_time = dispatcher_time + time_quantum
            print "Before-Dispatcher time:",dispatcher_time


            next_proc_ready = False
            print "Is the next process here: ",next_proc_ready
            #break

        elif(arrival_time==dispatcher_time):
            next_proc_ready = True
            print "Is the next process here: ",next_proc_ready

            print "\nProcess is here"


            print "My request time:",curr_request_time
            amount_of_iterations = curr_request_time/time_quantum
            print amount_of_iterations
            iteration_into_next_time_quantum = curr_request_time%time_quantum
            print iteration_into_next_time_quantum
            actual_iteration = iteration_into_next_time_quantum*0.1
            print actual_iteration

            total_iterations = amount_of_iterations + actual_iteration

            print "Process",curr_proc,"shall use",total_iterations,"time quantums."
            #break

    #if arrival_time == dispatcher_time:
        #init_proc_ready = True

    print "The init proc flag status is",init_proc_ready
    print "The NEXT proc flag status is",next_proc_ready
    print "\n***********\nBeginning execution"
    print "Initial request time is",remaining_time

#**************************************************************************
#
#Actual Round Robin Scheduling Check Mechanism
#
#**************************************************************************




    print "\nInitial execution of this process at discrete time",dispatcher_time

    if init_proc_ready == True and next_proc_ready == False:
        print "Business as usual"
        print "The time now is",dispatcher_time

        while remaining_time > process_done:

            if next_proc_ready ==True and has_been_executed_on==False:
                print "\n\n\n\n\nSkipping since the next process is already here!"
                print "The time now is",dispatcher_time
                break

            elif remaining_time > time_quantum:

                print "Execute!"
                print "Is the next process here: ",next_proc_ready
                remaining_time = remaining_time - time_quantum
                has_been_executed_on = True
                execute_counter = execute_counter + 1
                print "Execute number",execute_counter," on this process has been done."

                print "Here-Remaining time:",remaining_time
                dispatcher_time = dispatcher_time + time_quantum
                print "The time now is",dispatcher_time
                break

            elif remaining_time == time_quantum:
                print "After this iteration, this process shall be completed."

                print "Execute!"
                print "Is the next process here: ",next_proc_ready
                remaining_time = remaining_time - time_quantum
                has_been_executed_on = True
                execute_counter = execute_counter + 1
                print "Perfect! Execute number",execute_counter," on this process has been done."

                print "Here-Remaining time:",remaining_time
                dispatcher_time = dispatcher_time + time_quantum

                turnaround_time = dispatcher_time

                print "The process completed at time",turnaround_time
                has_been_completed = True

                print "The time now is",dispatcher_time
                break


            elif (remaining_time - time_quantum)<time_quantum:

                has_been_completed = True
                print "The time now is",dispatcher_time,"\n"
                print "This process shall complete before the time quantum is over"
                print "I shall queue the next process automatically instead of waiting the full quantum."

                print "Execute!"
                print "Is the next process here: ",next_proc_ready


                remaining_time = process_done



                has_been_executed_on = True
                execute_counter = execute_counter + (1*0.5)
                print "Bucko! Execute number",execute_counter," on this process has been done."

                print "Here-Remaining time:",remaining_time

                dispatcher_time = dispatcher_time + remaining_time

                turnaround_time = dispatcher_time
                print "The process completed at",turnaround_time



                print "The time now is",dispatcher_time,"\n"

            continue

        #dispatcher_time = dispatcher_time + remaining_time

            #if





    else:
        print "Request time is",remaining_time
        print "The time now is",dispatcher_time
        print "The process completed at time",turnaround_time
        print "Process is done"

    print "After-Dispatcher time:",dispatcher_time
    print "Exiting dispatcher time is",dispatcher_time
    print "Finito\n\n******************************************************\n\n\o/ PROCESS DONE!\n"
    print "\n******************************************************\n"
pass

#************************************************************
#
#
#
#************************************************************

##if __name__ == '__main__':
##    main()




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

    while archive_proc_list_size>0 and still_more==True:

     if (proc_list_size>0):
        print "Logibear"
        print proc_list_size
        curr_proc = proc_list.popleft()
        curr_arrival_time = proc_arrival_time_list.popleft()
        curr_request_time = proc_service_request_time_list.popleft()

        proc_list_size = len(proc_list)
        print proc_list_size

        print curr_proc
        print curr_arrival_time
        print curr_request_time

        main()

        if proc_list_size == 0:
                break

     archive_proc_list_size - 1

    print "Archive process list =",archive_proc_list
    print "Current process is",curr_proc
    print "Current arrival time is",curr_arrival_time
    print "hi"


