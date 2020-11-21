#!/usr/bin/env python

import os


tmpDir = "tmpDir";
print "-="*35 ; "File Creation and reamoving".center(70) ; "-="*35

if os.path.exists(tmpDir):
    print "os.path.exists('{0}') : {1}".format(tmpDir, os.path.exists(tmpDir) )
    print "os.rmdir('{0}')  : delects the directory".format(tmpDir)
    os.removedirs(tmpDir) ;
    os.rmdir(tmpDir) ; 

os.mkdir(tmpDir) ; 
print "os.mkdir('{0}') , creates the directory".format(tmpDir)

tmpdir=os.path.join(tmpDir, "abc", "123")
os.makedirs(tmpdir);
os.system('find '+ tmpdir)
tmpDirFile = os.path.join(tmpdir, 'foo.txt')

print "-="*35 ; "File Queries".center(70) ; "-="*35

print "os.path.exists('{0}') : {1}".format(tmpDir, os.path.exists(tmpDir) )
print "os.path.isdir('{0}')  : {1}".format(tmpDir, os.path.isdir(tmpDir) )
print "os.path.isfile('{0}') : {1}".format(tmpDir, os.path.isfile(tmpDir) )
print "os.path.isabs('{0}')  : {1}".format(tmpDir, os.path.isabs(tmpDir) )

print "-="*35 ; "Directory Attribute".center(70) ; "-="*35
print "os.path.abspath('{0}')     : {1}".format(tmpDir, os.path.abspath(tmpDir) )
print "os.path.basename('{0}')    : {1}".format(tmpDir, os.path.basename(tmpDir) )
print "os.path.dirname('{0}')     : {1}".format(tmpDir, os.path.dirname(tmpDir) )
print "os.path.join('a','b','c')     : {1}".format(tmpDir, os.path.join('a','b','c') )


print "-="*35 ; "File Attribute".center(70) ; "-="*35
tmpDirFile = os.path.join(tmpDir, "foo.txt") 
print "os.path.abspath('{0}')     : {1}".format(tmpDirFile, os.path.abspath(tmpDirFile) )
print "os.path.basename('{0}')    : {1}".format(tmpDirFile, os.path.basename(tmpDirFile) )
print "os.path.dirname('{0}')     : {1}".format(tmpDirFile, os.path.dirname(tmpDirFile) )
print "os.path.splitext('{0}')[0] : {1}".format(tmpDirFile, os.path.splitext(tmpDirFile)[0] )
print "os.path.splitext('{0}')[1] : {1}".format(tmpDirFile, os.path.splitext(tmpDirFile)[1] )


"""
try:
    os.mkdir("tmpDir")
except Exception as Details:
    print Details
"""

