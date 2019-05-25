#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 01:27:38 2019

@author: byakuya
"""
import sys

class Root_trips:
    def __init__(self,filepath):
        self.filepath=filepath
    #to calculate time in Hours.
    def Hours(self,time):
        Hours=map(float, time.split(':'))
        return Hours[0]+(Hours[1]/60)
    #Final print in the desired format
    def print_summary(self,Driver_trip):
        for x in Driver_trip:
            if x[2]>0:
                print '%s: %d miles @ %d mph'%(x[0],x[1],x[2])
            else:
                print '%s: %d miles '%(x[0],x[1])
    #reading the input file to read the commands and details
    def readfile(self,filepath):
        Driver_list={}
        Trip_details=[]
        #f = open('input.txt', 'r') used for testing in Anaconda IDE
        f = open(filepath, 'r') 
        num=0   #for line number 
        for line in f:      # seperating the input file to trips list and driver dictionary 
                            #so that the order in which trips and drivers appear doesnt matter 
            x= line.split()
            num+=1
            if len(x)!=0: # to avoid empty lines
                if x[0].lower()=='driver' :  # to consider input irrespective of its case
                    Driver_list.update({x[1]:[]})
                elif x[0].lower()=='trip':
                    Trip_details.append(x[1:])
                else:    # an add-on to give the line number incase of a wrong/garbage value. 
                     print 'Invalid Entry in line %d' %num      
        f.close()
        #associating trip details to each driver while discarding trips that don't have a driver initialised
        [Driver_list[y[0]].append(y[1:]) for y in Trip_details if y[0] in Driver_list]
        return Driver_list
    # the abpve step can be included while scanning the file if we for sure know that the order will not defer and the driver would come before 
    # the trip even during connection issues or improper processing.
    
    def trip_summary(self,drivers):       # calculating total distance and avg speed for each driver
        Driver_trip=[]
        for x in drivers:
            
            distance_total=[]
            total_time=[]
            for t in drivers[x]:
                distance=float(t[-1])
                
                time=self.Hours(t[1])-self.Hours(t[0])
                #print self.velocity(distance,time) debugging
                #checking for speed above 5 and below 100
                if self.velocity(distance,time)>5 and self.velocity(distance,time)<100: 
                    total_time.append(time)
                    distance_total.append(distance)
            if len(total_time) !=0:
                Driver_trip.append([x, round(sum(distance_total)), round(sum(distance_total)/sum(total_time))])
            else:
                Driver_trip.append([x,0,0])
        Driver_trip=sorted(Driver_trip,key=lambda y: y[1],reverse=True) #sorting according to distance
        self.print_summary(Driver_trip) #printing in desired output sequence
        return Driver_trip
    
    def velocity(self,dist,time): #calculating speed for a trip
        return round(dist/time)
    
    
    def main(self): #sample main functions to run the program and get the summary
        drivers=self.readfile(self.filepath)
        summary=self.trip_summary(drivers)
        return summary

# runing the main function
root=Root_trips(sys.argv[1]).main()
  
       
        
        