txt="main.txt"
ntxt="newfile.txt"
import os
source="C:/Users/KskYm/Desktop/g"
if os.path.exists(source):
  root,extension = os.path.splitext(source)
  os.rename(source,input("what shall i change" + root + " into?"))