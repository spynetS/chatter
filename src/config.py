

class Config:
    path = ""
    def __init__(self,path):
        self.path = path
    
    def __getFile__(self,option):
        file = ""
        try:
            file = open(self.path,option)
        except FileNotFoundError:
            f = open(self.path,"x")
            f.write("servername=test\n")
            f.write("maxmembers=\n")
            f.write("ip=192.168.1.119\n")
            f.write("port=8000\n")
            f.close()

            file = open(self.path,option)
        
        return file

    def getValue(self,key):
        f = self.__getFile__("r")
        
        for line in f.readlines():
            if(line.split("=")[0]==key):
                return line.split("=")[1].replace("\n","")
        return ""