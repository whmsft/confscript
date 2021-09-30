from setuptools import setup

with open("README.md", "r") as file:
   long_description = file.read()

setup(
	name='confscript',
	version='1.6b0',    
	description='''A configuration definition language''',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/Whirlpool-Programmer/confscript',
	author='Whirlpool-Programmer',
	author_email='whirlpool.programmer@outlook.com',
	license='GNU General Public License v3 (GPLv3)',
	packages=['confscript'],
	classifiers =[
	'Programming Language :: Python :: 3',
	'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
	'Operating System :: OS Independent'
	]
	
)

'''
BUILD COMMANDS
python setup.py sdist
python setup.py bdist_wheel --universal
python -m twine upload dist/*.*
'''