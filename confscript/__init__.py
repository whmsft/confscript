import os
import re
import sys
import random

def read(data):
	def parsedata(thisdata):
		readydata = {} if ':' in thisdata.split('\n') else [] 
		for i in thisdata.split('\n'):
			if i == "" or i == '\n' or i.isspace():
				pass
			else:
				if ':' in i:
					i = i.replace('!:', '$COLON$')
					var = i.split(':')[0][::-1]
					con = i.split(':')[1] if len(i.split(':')) == 2 else ':'.join(i.split(':')[1:])
					for char in var:
						if char.isspace():
							var = var[1:]
						else:
							break
					for char in con:
						if char.isspace():
							con = con[1:]
						else:
							break
					var = var.replace('$NOLOC$', ':')
					con = con.replace('$COLON$', ':')
					con = con[::-1]
					for char in con:
						if char.isspace():
							con = con[1:]
						else:
							break
					con = con[::-1]
					if con.lower() == "true":
						readydata[var[::-1]] = True
					elif con.lower() == "false":
						readydata[var[::-1]] = False
					elif con.lower() == "none":
						readydata[var[::-1]] = None
					else:
						try:
							readydata[var[::-1]] = int(con)
						except ValueError:
							if ',' in con:
								readydata[var[::-1]] = con.split(',')
							else:
								readydata[var[::-1]] = con
				else:
					con = i
					if ',' in con:
						readydata.append(con.split(','))
					else:
						readydata.append(con)
		return readydata
	readdata = {}
	data = data.split('---\n')
	for i in data:
		for x in i.split('\n'):
			if re.match(r'== *.* ==', x):
				readdata[x[3:-3]] = parsedata(i[i.find(x)+len(x):])
	return readdata
	
def readFile(filepath):
	if os.path.isfile(filepath):
		contents = open(filepath).read()
		return read(contents)
	else:
		raise FileNotFoundError(f"File does not exist!")

def dump(data):
	def reverseParse(thisdata):
		newdata = ''
		for i in thisdata.keys():
			value = thisdata[i]
			if str(type(value)) == "<class 'list'>":
				value = ",".join(value)
			newdata += "{}: {}\n".format(i,value)
		return str(newdata)
	__data__ = ""
	length = len(data)
	for i in data.keys():
		__data__ += "== {} ==\n".format(i)
		__data__ += reverseParse(data[i])
		length -= 1
		if length >= 1:
			__data__ += '---\n'
	return __data__