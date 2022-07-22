from flagser import *
def getUsernamefile(option):
	try:
		users = open("../.users",option)
	except:
		temp = open("","x")
		users = open("../.users",option)
	return users

class SetName(Flag):
    shortFlag = "name"

    def removeLastUsername(self,args):
        usernames = []
        usersread = getUsernamefile("r")
        for line in usersread.readlines():
            if(args[1] not in line):
                usernames.append(line)
        usersread.close()

        u = getUsernamefile("w")
        for line in usernames:
            u.write(line)
        u.close

    def onCall(self, args):
        self.removeLastUsername(args)
        users = getUsernamefile("a")
        users.write(args[0].replace("\n","")+":"+args[1])
        users.write("\n")
        users.close()
  