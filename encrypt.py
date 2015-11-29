#!/usr/bin/python

import encryptlib
import sys,getopt

with open("encrypt_key") as myfile:
   key = myfile.read()
with open("encrypt_names") as myfile:
   filenames = myfile.read().split()

options = getopt.getopt(sys.argv, 'ed',['encrypt','decrypt'])
for opt in options[1][1:]:
   scrambler = None; read_filenames = None; write_filenames = None
   if opt in ('-e','--encrypt'):
      scrambler = encryptlib.encrypt
      read_filenames = (fn for fn in filenames)
      write_filenames = ('encrypted_files/'+fn+'.enc' for fn in filenames)
   elif opt in ('-d','--decrypt'):
      scrambler = encryptlib.decrypt
      read_filenames = ('encrypted_files/'+fn+'.enc' for fn in filenames)
      write_filenames = ('encrypted_files/'+fn+'.dec' for fn in filenames)
   else:
      print("ERROR!", opt)
   for rfn,wfn in zip(read_filenames,write_filenames):
      with open(rfn, "rb") as myfile:
         text = myfile.read()
      with open(wfn, "wb") as myfile:
         myfile.write(''.join(scrambler(text, key)))
