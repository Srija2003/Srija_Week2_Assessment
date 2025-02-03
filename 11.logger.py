class logger:
    def log(self,message):
        print(f"{message}")
        
    def log(self,message,error=""):
        print(f"{message},{error}")
    
l=logger()
l.log("hello")
l.log("hii","error")