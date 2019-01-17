#! /usr/bin/env python
"""
Create intro page from Jupyter Not book
   Markdown cell will Start with following KeyWord
      * Intro, Doc

Usage :  
    List of Notebooks
"""

nb_data = {
 "cells": [
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

import json, re, sys

def main(fileOut, nbs):
    
    for nb in nbs:
        fpin = open(nb, 'r')
        nb_cells = json.load(fpin)["cells"]
        nb_data["cells"].extend( getDocCells(nb_cells) )
        fpin.close()

    fpout = open(fileOut, 'w')
    txtOut = json.dumps(nb_data, sort_keys=True, indent=4, separators=(',', ': '))
    
    fpout.write( txtOut )
    fpout.close()
    

def getDocCells(nb_cells):
    docCells = []
    for cell in nb_cells:
        if cell["cell_type"] != "code":
            for line in cell["source"]:
                if re.match(r"^#\s", line)  :
                    docCells.append(cell); break
                # elif re.match(r"\s*Intro|\s*Doc", line, re.I):
                #     docCells.append(cell); break

    
    return docCells


if __name__ == '__main__':

    fileOut = sys.argv[1]
    # nbs = sys.argv[2:]
    fpin = open(sys.argv[2], 'r')
    nbs = []
    for line in fpin:
        line = re.sub(r"#.*", "", line).strip()
        if line: nbs.append(line)
        
    fpin.close()

    main(fileOut, nbs)

