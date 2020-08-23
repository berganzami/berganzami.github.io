#############################
# some functions of the Python 'os' and 'sys' modules, together with some coding exercises using these functions
# 3rd lesson of the course 'Sistemi Operativi', Laurea Triennale in Matematica
# Universita' di Roma, "La Sapienza"
# academic year 2016-2017  
# miguel.berganza@roma1.infn.it
#############################


#the module 'os': an operating system interface. Here there are some useful built-in functions:
#######################################################
import os

	# 'mystring' contains your favourite bash instruction	
os.system(mystring)

	#you can list the directories in a given folder:
os.listdir(yourfavoritepath)
	#the output being a list

	#you can check whether a given file is a directory or a regular file:
os.path.isdir(yourfavoritepath)

	#the size of a file in bytes:
os.stat(filename).st_size

	#is a given file a regular file, or a folder?
os.path.isfile(filename)
os.path.isdir(filename)

#the module 'sys': 'argv' and 'exit'
#######################################################
import sys
	
	#command-line arguments
if len(sys.argv) == 1:
	myintarg = int(sys.argv[1])
else:
	print 'ci vuole un argomento per riga di comando!'
	sys.exit()


#some exercises:
#######################################################
#EX1. Write a Python script that resizes all images with format '.jpg' in a given folder, using the bash command 'convert'. The script should take as command-line arguments the folder name and the percentage of compression. 
#EX2. Write a script that compresses all files in a given folder and provide the compression ratio. From the process, please exclude the hidden files (those beginning by a dot '.'), and also the directories. 
#EX3. Write a scritp which sorts an N-column file containing floating point numbers according to its n-th column elements (taking n and the file name as arguments), and prints the result (the rest of the columns of the file must be sorted coherently with the n-th column sorting, of course). The function must be such that, for common values of the n-th column element, higher rows in the original file result higher in the sorted file. 
#######################################################
