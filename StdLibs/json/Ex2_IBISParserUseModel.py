#!/usr/bin/env python

import json

class c1:
    """
        Not working Strategy.  Need to write class specific methods
    """ 
    Json    =  "JsonDBName.db";
    ObjList     = [];
    def __init__(self):
        self.prop1 = "C1_Model"
        self.prop2 = "C1_ModelName"
        self.prop3 = "C1_Model_Text"

    def Kprint(self):
        print self.prop1
        print self.prop2
        print self.prop3

        for JsonDb in self.ObjList:
            fp = open(JsonDb ,  "r")
            Obj = json.load(fp)
            Obj.Kprint

    def Kwrite(self, JsonDb):
        fp =open(JsonDb ,  "w")
        print "Dumping JSON DB into " ,  fp.name
        json.dump(self.ObjList, fp)
        fp.close
        return JsonDb

class c2:
    """
    """
    ObjList     = [];
    def __init__(self):
        self.prop1 = "C2_Model"
        self.prop2 = "C2_ModelName"
        self.prop3 = "c2_Model Text"
        
    def Kprint(self):
        print self.prop1
        print self.prop2
        print self.prop3

        for JsonDb in self.ObjList:
            fp = open(JsonDb ,  "r")
            print "Dumping JSON DB into " ,  fp.name
            Obj = json.load(fp)
            print Obj
            #Obj.Kprint()
            
    def Kwrite(self, JsonDb):
        fp =open(JsonDb ,  "w")
        json.dump(self, fp)
        fp.close
        return JsonDb


c2Obj = c2()

c1Obj1= c1();
c1Obj2= c1();

c1Obj1.Kprint()
c1Obj2.Kprint()
#
#c2Obj.ObjList.append(c1Obj1.Kwrite("c1Obj1.Json"))
#c2Obj.ObjList.append(c1Obj2.Kwrite("c1Obj2.Json"))

#c2Obj.ObjList.append(json.dump(c1Obj1,"c1Obj1.Json"))
#c2Obj.ObjList.append(json.dump(c1Obj2,"c1Obj2.Json"))

c2Obj.Kprint()




