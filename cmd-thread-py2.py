# importing libraries
from threading import Thread
import subprocess
import os

def runCmd(cmd):
    process = subprocess.Popen([cmd], shell = True, stdout = subprocess.PIPE)
    output = process.communicate()

    return output

def run_cmd(cmd):
    process = subprocess.Popen([cmd], shell = True, stdout = subprocess.PIPE)
    output = process.communicate()
    print str(output[0])


    return output


# a function to ping given host
def find(path,args=[]):

	# command is pong
	os.chdir(path)
	cmd = "ls -d */ |  sed 's/\///g'"
	
	ls_output = runCmd(cmd)

	# Converting into list of strings
	dirs = str(ls_output[0]).split("\n")

	# Removing empty strings
	dirs = [string for string in dirs if string != ""]

	dirs_len = len(dirs)
	chunk_size = 30
	next = 0
	i = 0
	# print dirs

	while dirs_len > 0:
		if(dirs_len >= chunk_size):
			print "-------------",dirs_len,"----------" 
			dir_chunk=" ".join(dirs[next:next+chunk_size])
			# print(dir_chunk)

			find_cmd = "find "+dir_chunk+" -type f -name \"*.sh\""
			print find_cmd

			# find_output = run_cmd(find_cmd)
			t = Thread(target=run_cmd, args=(find_cmd,))
			t.start()
			# t.join()

			# print(str(find_output[0], "utf-8"))

			next+=chunk_size
		else:
			print "-------------ending--",dirs_len,"----------"
			dir_chunk=" ".join(dirs[next:next+chunk_size])
			# print(dir_chunk)

			find_cmd = "find "+dir_chunk+" -type f -name \"*.sh\""
			print find_cmd

			# find_output = run_cmd(find_cmd)
			t = Thread(target=run_cmd, args=(find_cmd,))
			t.start()
			# t.join()
			
			# print(str(find_output[0], "utf-8"))

		dirs_len = dirs_len - chunk_size
			
		

	return ls_output


if __name__ == '__main__':
    res = find('/usr/lib')
    print("-------Done-----")
