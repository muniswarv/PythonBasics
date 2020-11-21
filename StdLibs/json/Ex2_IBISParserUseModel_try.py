#!/usr/bin/env python

import json

class c1:
    """
        Not working Strategy.  Need to write class specific methods
    """ 
    Json    =  "JsonDBName.db";
    dataHash = {};

    def __init__(self):
        self.dataHash["prop1"] = "C1_Model"
        self.dataHash["prop2"] = "C1_ModelName"
        self.dataHash["prop3"] = "C1_Model_Text"
        self.dataHash["ObjList"] = [];

    def Kprint(self):
        print self.dataHash["prop1"] 
        print self.dataHash["prop2"] 
        print self.dataHash["prop3"] 

        for JsonDb in self.dataHash["ObjList"]:
            fp = open(JsonDb ,  "r")

            JsonObj = json.load(fp)
            Obj=eval( JsonObj[0] ) (); print Obj
            Obj.dataHash =  JsonObj[1] ;
            Obj.Kprint

    def Kwrite(self, JsonDb):
        fp =open(JsonDb ,  "w")
        print "Dumping JSON DB into " ,  fp.name
        JsonData = ["c1" , self.dataHash ];

        json.dump(JsonData, fp)
        fp.close

        return JsonDb

c1Obj = c1();
JsonDb = c1Obj.Kwrite("c1ObjDB.json")


fp = open(JsonDb, "r")

JsonObj = json.load(fp)
Obj=eval( JsonObj[0] ) (); # print "Obj - " ,  Obj
Obj.dataHash =  JsonObj[1] ;
Obj.Kprint()
