from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='brynjar',
      version=version,
      description="First package for python course",
      long_description=""" """,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python scilifelab',
      author='Brynjar Smari Bjarnason',
      author_email='binni@binnisb.com',
      url='https://github.com/binnisb',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      scripts=["scripts/getting_data.py","scripts/check_repo.py"],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
