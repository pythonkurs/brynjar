#/usr/bin/env python
import sys
import os
from brynjar.session3 import DirChanger, CourseRepo
(basepath,repo)=os.path.split(sys.argv[1])

with DirChanger(basepath) as dc:
    a = CourseRepo(repo)
    if a.check():
        print "PASS"
    else:
        print "FAIL"
