class hour():
    
    def __init__(self, hh, mm, ss,hh1,mm1,ss1):
        self.houre = hh
        self.minute = mm
        self.second = ss

        self.hour1 = hh1
        self.minute1 = mm1
        self.second1 = ss1
        
    def sum(self):
        time ={}
        time.second = self.second + self.second1
        time.minute = self.minute + self.minute1
        time.hour = self.hour + self.hour1
        
        if time.second >= 60:
            time.second -= 60
            time.minute += 1
        
        if time.minute >= 60:
            time.minute -= 60
            time.hour += 1
            
        return time
    
    def sub(self, mehman):
        time = {}
        
        if self.second >= self.second1:
            time.second = self.second - self.second1
        else:
            self.second += 60
            self.minute -= 1
            time.second = self.second - self.second1
        
        if self.minute >= self.minute1:
           time.minute = self.minute - self.minute1
        else:
            self.minute += 60
            self.hour -= 1
            time.minute = self.minute - self.minute1
        
        time.hour = self.hour - self.hour1
        if time.hour < 0:
            time.hour += 24
        
        return time
    
    def hour_to_sec(self):
        time = {}
        time.hour = 0
        time.minute = 0
        time.second = self.second + self.minute * 60 + self.hour * 3600
        return time
    
    def sec_to_hour(self):
        time = {}
        
        time.hour = self.second // 3600
        self.second %= 3600

        time.minute = self.second // 60
        self.second %= 60

        time.second = self.second
        
        return time
    
    def show(self):
        print(self.hour, ':', self.minute, ':', self.second)

houre = int(input('please typr yore hour: '))
minute = int(input('please typr yore minute: '))
second = int(input('please typr yore second: '))

hour1 = int(input('please typr yore hour1: '))
minute1 = int(input('please typr yore minute1: '))
second1 = int(input('please typr yore second1: '))

    
a = (houre, minute, second)
b = (hour1,minute1,second1)

c1 = a.sum(b)
c1.show()

c2 = a.sub(b)
c2.show()

c3 = a.hour_to_sec()
c3.show()

c4 = c3.sec_to_hour()
c4.show()