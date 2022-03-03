# importing libraries
from threading import Thread
import subprocess
import os
import sys

class FindCmd:

	def __init__(self):
		self.res = []

	def runCmd(self,cmd):
		process = subprocess.Popen([cmd], shell = True, stdout = subprocess.PIPE)
		output = process.communicate()

		return output

	def run_cmd(self,cmd):
		process = subprocess.Popen([cmd], shell = True, stdout = subprocess.PIPE)
		output = process.communicate()
		str_list = output[0].split("\n")
		self.res = self.res + str_list
		# print output[0]

		return output

	def find(self,path,chunk=40):
		# command is pong
		try:
			os.chdir(path)
			cmd = "ls -d */ |  sed 's/\///g'"
			
			ls_output = self.runCmd(cmd)

			# Converting into list of strings
			dirs = str(ls_output[0]).split("\n")

			# Removing empty strings
			dirs = [string for string in dirs if string != ""]

			dirs_len = len(dirs)
			chunk_size = chunk
			next = 0
			i = 0
			# print dirs
			threads = []

			while dirs_len > 0:
				if(dirs_len >= chunk_size):
					dir_chunk=" ".join(dirs[next:next+chunk_size])
					# print(dir_chunk)

					find_cmd = "find "+dir_chunk+" -type f -name \"*.sh\" -exec grep -q \"host\" {} \\; -exec dirname {} \\; |  grep -v \"na-clients\""
					# print find_cmd

					t = Thread(target=self.run_cmd, args=(find_cmd,))
					threads.append(t)
					t.start()
					i+=1

					next+=chunk_size
				else:
					dir_chunk=" ".join(dirs[next:next+chunk_size])
					# print(dir_chunk)

					find_cmd = "find "+dir_chunk+" -type f -name \"*.sh\" -exec grep -q \"host\" {} \\; -exec dirname {} \\; |  grep -v \"na-clients\""
					# print find_cmd

					t = Thread(target=self.run_cmd, args=(find_cmd,))
					threads.append(t)
					t.start()
					i+=1

				dirs_len = dirs_len - chunk_size

			for x in threads:
				x.join()
		except Exception, e:
			print e
		# finally:
		# 	print "Completed"


if __name__ == '__main__':
	chunks = int(sys.argv[1])
	
	findcmd = FindCmd()
	findcmd.find('/usr/lib', chunks)
	findcmd.res = [string for string in findcmd.res if string != ""]
	res = "\n".join(findcmd.res)
	print res
