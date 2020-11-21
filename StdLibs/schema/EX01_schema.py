
from schema import Schema, And, Use, Optional, Or

sep = "#"  + "-="*45 + "\n"

def schema_validate(schema, data):

    sep = "#" + "--"*45 + "\n"
    try:
        validated = schema.validate(data)
        print sep + " INFO : Is valid data : {0}\n After Validate : {1}".format(data, validated)
    except Exception as err:
        print sep + " ERROR : Invalid data  : {0}\n {1}".format(data, err)

def validata_dict_known_keys():

    print "\n\n" + sep + "-------------    validata_dict_unknown_keys    -------------\n" + sep
    schema = Schema([{'name': And(str, len),
                  'age':  And(Use(int), lambda n: 18 <= n <= 99),
                  Optional('sex'): And(str, Use(str.lower),
                                       lambda s: s in ('male', 'female'))}])
    dataList = [
            [ {'name': 'foo', 'age': 50, 'sex': 'male' }                ],
            [ {'name': 'foo', 'age': 50, 'sex': 'male', 'junk':'junk' } ],
            [ {'name': 'foo', 'age': 52 }                     ],
            [ {'name': 'Sue', 'age': '28', 'sex': 'FEMALE'},
              {'name': 'Sam', 'age': '42'},
              {'name': 'Sacha', 'age': '20', 'sex': 'Male'}    ],
            ]
    
    for data in dataList: schema_validate(schema, data)

def validata_dict_unknown_keys():

    print "\n\n" + sep + "-------------    validata_dict_unknown_keys   -------------\n" + sep
    dataList = [
             { 'name': 'foo'   , 'age': 52                                       },
             { 'name': 'foo'   , 'age': 50   ,  'sex': 'male'                    },
             { 'name': 'Sue'   , 'age': '28' ,  'sex': 'FEMALE'                  },
             { 'name': 'Sacha' , 'age': '20' ,  'sex': 'Male'                    },
             { 'name': 'foo'   , 'age': 50   ,  'sex': 'male'   ,  'junk':'junk' },
             { 'name': 'foo'   , 'age': 50   ,  'sex': 'male'   ,  'junk':'junk', 'junk1':'junk1',  },
            ]

    # List of dictionary, Optional keys allowed
    schema = Schema({'name': And(str, len),
                  'age':  And(Use(int), lambda n: 18 <= n <= 99),
                  Optional('sex'): And(str, Use(str.lower), lambda s: s in ('male', 'female')),
                  Optional(str): object,
                  })               

    for data in dataList: schema_validate(schema, data)

def validate_schema_And():
    print "\n\n"
    print sep + "-------------    validate_schema_And    -------------\n" + sep

    schema = Schema( {'age': And(int, lambda n: 0 < n < 99)} )

    dataList = [ {'age': 7}, {'age': 70.0} ]

    for data in dataList: schema_validate(schema, data)


def validate_schema_Or_with_Use():
    
    print "\n\n" + sep + "-------------    validate_schema_Or_with_Use    -------------\n" + sep
    # With Use
    schema = Schema( {'percentage': Or( Use(int), Use(float) )  } )
    dataList = [  {'percentage': 70   },
                  {'percentage': 70.0 },
                  {'percentage': '70.0' },
                  {'percentage': 'inf' },
                  {'percentage': 'foo' },
               ]

    for data in dataList: schema_validate(schema, data)

if __name__ == '__main__':
    # validata_dict_known_keys()
    validata_dict_unknown_keys()

    validate_schema_And()

    validate_schema_Or_with_Use() 
