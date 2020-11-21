#!/usr/bin/env python


print "="*10, " time other format", "="*10

from time import gmtime, strftime

print  "from datetime import datetime "
print strftime("%Y-%m-%d %H:%M:%S", gmtime())
print " year => ", strftime("%Y", gmtime())
print " month => ", strftime("%m", gmtime())
print " Date => ", strftime("%d", gmtime())
print " time => ", strftime("%H:%M:%S", gmtime())

print "="*10, " time other format 1", "="*10

import datetime
now = datetime.datetime.now()
print (now)
print "Current year: %d" % now.year
print "Current month: %d" % now.month
print "Current day: %d" % now.day
print "Current hour: %d" % now.hour
print "Current minute: %d" % now.minute
print "Current second: %d" % now.second
print "Current microsecond: %d" % now.microsecond

print
print "Current date and time using strftime:"
print now.strftime("%Y-%m-%d %H:%M")


