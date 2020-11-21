#!/usr/bin/env python

# Basic Data Types
import json

my_int = 1;
my_float = 1.4;
my_float2 = 2.64e-9;
myList = [ my_int , my_float , my_float2 ]
myDict = {'obj1':myList}

jsonObj = json.dumps(myList, myDict)

FileName = "/home/vmsreddy/Training/PYTHON/STDLIB/json/Ex1_DumpNLoad_DB.json"
FilePtr = open ( FileName,  "w") 
print "Dumping the Data into Json file - " ,  FileName
print "myDict = " ,  myDict
print json.dumps(myDict, myList)
# Dump the object 
print json.dump(myDict, FilePtr)   # Dump to a file
FilePtr.close

print "Reading the Json File - " ,  FileName
FilePtr = open ( FileName,  "r") 
MyDictJson = json.load(FilePtr)
print "MyDictJson =" ,  MyDictJson
print MyDictJson['obj1']

