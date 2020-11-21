

from schema import Schema, Use, And, Or, Optional, SchemaError
Schema([ (str,int,float), [(str, int, float)]] ).validate([1 , [1]])
Schema([ (str,int,float), [(str, int, float)]] ).validate([ ('a', 1, 1.0) , [('a', 1, 1.0)]])
Schema([ (str,int,float), [(str, int, float)]] ).validate([ (1.2 , 1, 1.0) , [('a', 1, 1.0)]])
Schema([ (str,int,float), [(str, int, float)]] ).validate([ ('1.2', '1', '1.0') , [('a', 1, 1.0)]])


Schema([(str,int,float), [(str, int, float)]]).validate([1 , [1])
Schema([(str,int,float), [(str, int, float)]]).validate([1 , [1]])
Schema([(str,int,float)]).validate([1])
Schema([(str,int,float)]).validate([('a', 1, 1.0)])
Schema([Or(str,int,float)]).validate([('a')])
Schema([Or(str,int,float), Or(list, tuple)]).validate(['a', [1,2]])
Schema([Or(str,int,float), Or(list, tuple)]).validate(['a', {1:2}])


try:
    Schema([Or(str,int,float), Or(list, tuple)]).validate(['a', {1,2}])
except SchemaError as details:
    print details



# use Model

attriTypeSchema = { 
                    'type0' : Schema( Or(str,int,float) ),
                    'type1' : Schema( [Or(str,int,float), ( Or(str,int,float) ) ] )
                    'type2' : Schema( [Or(str,int,float), [ Or(str,int,float) ] ] )
                  }

attriTypeSchema['type0'].validate('a')
attriTypeSchema['type0'].validate(1)
attriTypeSchema['type0'].validate([1])

attriTypeSchema['type1'].validate(['a'])
attriTypeSchema['type1'].validate(['a', ( 'a', 1 , 3 )])
attriTypeSchema['type1'].validate(['a', [ 'a', 1 , 3 ]])

attriTypeSchema['type2'].validate(['a',  'a', 1 , 3.0 , ['a'] ])
attriTypeSchema['type2'].validate(['a',  'a', 1 , 3.0 , ['a', 1 ] ])
