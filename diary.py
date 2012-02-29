#!/usr/bin/python
import sys, os, datetime, glob
diary_folder = ""
now = datetime.datetime.now()


def main():
	"""Diary txt"""
	action = ''
	argument = ''

	if len(sys.argv) >= 2:
		action=sys.argv[1]
	if len(sys.argv) >= 3:
		argument=sys.argv[2]
	else:
		argument=None
	
	{'add': add,
 	'ls': list,
 	'find': d_search,
 	'help': help,
	}.get(action, help)(argument)


def add(text):
	todays_diary = datetime.date.today().strftime("%Y-%m-%d") + ".txt"
	with open(diary_folder+todays_diary, "a") as today:
		today.write(text+"\n")
		print("Added diary entry")

def list(diary_date=None):
	"""List all elements for a specific date"""
	if diary_date==None:
		diary_date = datetime.date.today().strftime("%Y-%m-%d")

	abs_file = diary_folder + diary_date + ".txt"
	if os.path.isfile(abs_file):
		diary_file = open(abs_file,'r').read()
		print diary_file
	else:
		print('No diary entry specified')


def d_search(pattern):
	file_list = glob.glob(os.path.join(diary_folder, '*.txt'))
	file_list.sort()
	for infile in file_list:
		file = open(infile,"r")
		text = file.read()
		file.close()
		index = text.find(pattern)
		if index > 0:
			file_name = infile.split('/')
			lines = text.split('\n')
			for line in lines:
				index = line.find(pattern)
				if index > 0:
					print ("%s -- %s" % (file_name[-1], line))

def help(argument):
	"""test"""
	print "Usage:"
	print "\tdiary.py add 'Today I went to the @shops and bought some cake for the #party'"
	print "\tdiary.py find '#party'"
	print "\tdiary.py ls"
	print "\tdiary.py help"

if __name__ == '__main__':
  main()
