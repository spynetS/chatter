import os
import socket

prevPath = "../.prev.txt"

def getPrev(option):
	global prevPath
	try:
		prev = open(prevPath,option)
	except FileNotFoundError:
		temp = open(prevPath,"x")
		prev = open(prevPath,option)
	return prev

def newCon():
	global prevPath
	ip = input("server ip:")
	port = input("server port:")
	prev = getPrev("a")
	prev.write(ip+":"+port)
	prev.close()
	os.system("python client.py "+ip+" "+port)


def prevCon(ip,port):
	os.system("python client.py "+ip+" "+port)

def printServer(index,ip,port):
	#check online status
	#thows error server is offline
	server = socket.socket()
	try:
		server.connect((ip, int(port)))
		test = server.recv(2048).decode()
		#if we dont get a connected back the server is offline and we throw a erroe
		if(test!="connected"):
			raise
		print(index,ip+":"+port,"online")

	except Exception as e:
		print(index,ip+":"+port,"offline")
	finally:
		server.close()

# print prev connectens and handle connections
prev = getPrev("r")
i = 1
lines = []
for line in prev.readlines():
	printServer(i,line.split(":")[0],line.split(":")[1].replace("\n",""))
	lines.append(line)
	i+=1
print()
connection = input("Select previus connection with index (0 for new connection) \n")

if(connection == "0"):
	newCon()
else:
	line = lines[int(connection)-1]
	prevCon(line.split(":")[0],line.split(":")[1])


