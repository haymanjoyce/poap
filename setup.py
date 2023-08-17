from setuptools import setup, find_packages


setup(
   name='src',
   version='0.1',
   packages=find_packages(),
   install_requires=[
      'click',
   ],
   entry_points='''
      [console_scripts]
      tool=src.tool.commands:main
      ''',
)

# check entry point syntax

