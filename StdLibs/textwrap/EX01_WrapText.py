#!/usr/bin/env python


"""

    
"""
import sys
import textwrap

if ( len(sys.argv[1:]) == 0 or ("help" in sys.argv[1]) ):
    print "\nUsage:\n\t", sys.argv[0] , " <fileName> \n"; 
    exit(0)

fileName = sys.argv[1];

wrap = textwrap.TextWrapper();  # Create a text Wrap Object

fp = open(fileName , "r")

print "-="*35;print "Actual text".center(70);print "-="*35
txt = fp.read()

print txt

print "-="*35;print " txtList = textwrap.wrap(txt,70)\n print'\\n'.join(txtList)".ljust(70);print "-="*35
txtList = textwrap.wrap(txt,70);
print "\n".join(txtList)

print "-="*35;print " txtList = textwrap.fill(txt,70)".ljust(70);print "-="*35
print textwrap.fill(txt,70);

wrapObj = textwrap.TextWrapper();  # Create a text Wrap Object

wrapObj.initial_indent="     ";

#print wrapObj.fill(txt);

def PrintWrapObjAttri(wrapObj=None):
   if not wrapObj:
       wrapObj = textwrap.TextWrapper();  # Create a text Wrap Object

   AttriList = """
        width
        expand_tabs
        replace_whitespace
        drop_whitespace
        initial_indent
        subsequent_indent
        fix_sentence_endings
        break_long_words
        break_on_hyphens
   """.split()

   for Attri in AttriList:
       print " ".ljust(8), Attri.ljust(25) , "= '" , eval(str("wrapObj."+ Attri)) , "'"
 

def FormatKeyWordColumn(txt, keyWord="*", wrapObj=None):
   if not wrapObj:
       wrapObj = textwrap.TextWrapper();  # Create a text Wrap Object

   wrapObj.initial_indent    = keyWord + " ";
   wrapObj.subsequent_indent =" "*len(keyWord) + " "
   wrapObj.replace_whitespace = False
   PrintWrapObjAttri(wrapObj); print "-="*35

   return wrapObj.fill(txt)


wrapObj.width=70
wrapObj.drop_whitespace=True

print "-="*35;
print " FormatKeyWordColumn( txt,keyWord='[Notes]'.ljust(10) )".ljust(70);
print "-="*35

keyWord = '[Notes]'.ljust(10)
print FormatKeyWordColumn( txt,keyWord=keyWord )


