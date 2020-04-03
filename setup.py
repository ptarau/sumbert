import subprocess
from sys import platform
import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()
with open("README.md","r") as f:
    long_description = f.read()

version = "1.0.0"
setup(name='sumbert',
  version=version,
  description='sumbert: A BERT-based summarizer with a frindly API',
  long_description = long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/ptarau/sumbert.git',
  author='Paul Tarau',
  author_USER_EMAIL='<paul.tarau@gmail.com>',
  license='Apache',
  packages=['sumbert'],
  package_data={'sumbert': ['*.txt']},
  include_package_data=True,
  install_requires = required,
  zip_safe=False
  )

