class Movie(object):
    def __init__(self, t, y, m, d):
        self.title = t
        self.year = int(y)
        self.month = int(m)
        self.day = int(d)
    
    def getTitle(self):
        return self.title
    
    def getDate(self):
        return (self.year, self.month, self.day)
    
    def getYear(self):
        return self.year
    
    def getMonth(self):
        return self.month
    
    def getDay(self):
        return self.day   
        
    def earlierThan(self, date):
        if self.year > int(date[0]):
            return False
        elif self.year < int(date[0]):
            return True
        elif self.year == int(date[0]):
            if self.month > int(date[1]):
                return False
            elif self.month < int(date[1]):
                return True
            elif self.month == int(date[1]):
                if self.day < int(date[2]):
                    return True
                else:
                    return False
    
    def formatMovie(self):
        output = "{}: {}\{}\{}\n".format(self.title, self.month, self.day, self.year)
        return output
    
            
        
        
        