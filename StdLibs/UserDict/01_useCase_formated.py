
from UserDict  import UserDict


class myDict(UserDict):
    """docString """

    def __init__(self, dictIn):
        """ Constructor Function 
        Options Usage:
        """

        UserDict.__init__(self, dictIn)
        self.data = dictIn


    def hasAllKeys(self, keys):
        missKeys = []
        status = True

        dictIn = self.data
        for key in keys:
            if not self.data.has_key(key):
                status = False
                missKeys.append(key)

        if missKeys:
            print "Missing Keys {0}".format(missKeys)
            status = False

        return False


    def isSubDict(self, subDict):
        
        dictIn = self.data

        missingKeys = []
        valMismatch = {}
        status = True
        for key, val in subDict.items():
            if not dictIn.has_key(key):
                missingKeys.append(key)
                status = False
                continue

            if val != dictIn[key]:
                valMismatch[key] = { "subDict": val, "dictVal": dictIn[key] }
                status = False

        if not status :
            print "missing keys : {misKey}, mismath in var {misVal}".format(misKey=missingKeys, misVal=valMismatch)
        
        return status



if __name__ == '__main__':
    
    varDict = { 
            "var1" : "val1",
            "var2" : "val2",
            "dep1_var1": "dep_val1",
        }

    obj = myDict(varDict)

    print "#-------    Object behaves like a dictionary"
    
    print obj["var1"]
    print obj.has_key("var1")
    print obj.has_key("Junk")

    if isinstance(obj, dict):
        print "Is dict Instance"
    else:
        print "Is Instance of type '{0}'".format( type(obj) )



    try:
        print obj["Junk"]
    except KeyError as e:
        print "KeyError : {0}".format(str(e))

    obj.data["new"] = "newVal"


    subDict = { 
            "var1" : "val1",
            "var2" : "val2",
        }

    misKeyDict = { 
            "var1" : "val1",
            "var2" : "val2",
            "misKey" : "dep_val1"
        }

    misValDict = { 
            "var1" : "val1_mis",
            "var2" : "val2",
        }
    
    print "exp = True , got = ", obj.isSubDict(subDict)
    print "exp = False, got = ", obj.isSubDict(misKeyDict)
    print "exp = False, got = ", obj.isSubDict(misValDict)

    print "odj         :", obj
    print "dict(obj)   :", dict(obj)
    print "obj.items() :", obj.items()

    genDict =  {"genVar": "genVal"}; genDict.update(obj)

    print 'genDict =  {"genVar": genVar}; genDict.update(obj); \n\t genDict : ', genDict
    print 





