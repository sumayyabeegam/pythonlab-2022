class Time:
    def __init__(self,hour=0,min=0,sec=0):
        self.__hour = hour
        self.min = min
        self.sec = sec
    def show(self):
        print("EARLIEST TIME=",self.__hour,':',self.min,':',self.sec)
    def __lt__(self,other):
        if(self.__hour<other.__hour):
            return True
      
        if(self.__hour==other.__hour):
            if(self.min<other.min):
                return True
            if self.min==other.min:
                if self.sec<other.sec:
                    return True
                else:
                    return False
        else:
            return False
        

t1=Time(14,45,35)
t2=Time(14,25,24)
if(t1<t2):
    t1.show()

else:
    t2.show()
