
import os

for root, dirs, files in os.walk("."): 
    print "-="*70;
    print "root : ", root;
    print "dirs : ", dirs ;
    print "files : ", files ;

    
print "-="*70;

