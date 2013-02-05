#/usr/bin/env python
import os
class DirChanger(object):
    def __init__(self,path):
        self._path = path
    def __enter__(self):
        self._org_dir = os.getcwd()
        os.chdir(self._path)
    def __exit__(self,type,value,traceback):
        os.chdir(self._org_dir)



class CourseRepo(object):
    def __init__(self,surname):
        self.surname = surname
        
    @property
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname(self,name):
        self._surname = name
        self.required =  [".git","setup.py","README.md","scripts/getting_data.py",
                        "scripts/check_repo.py",self._surname+"/__init__.py",
                        self._surname+"/session3.py"]
    def check(self):
        for p in self.required:
            if not os.path.exists(p):
                return False
        return True