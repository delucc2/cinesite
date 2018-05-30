from Movie import *

class Archive(object):
    def __init__(self, movie):
        self.movielist = []
        self.movielist.append(movie)
        self.isavailable = True
        self.isupdated = False
    
    def getLength(self):
        return len(self.movielist)
        
    ## Check if movie is already in the list
    ## if so, mark it unavailable  
    ## if not, add it into the archive
    def addMovie(self, movie):
        self.isavailable = True
        title = movie.getTitle()
        for i in self.movielist:
            if i.getTitle() == title:
                date = i.getDate()
                self.isavailable = False
                break
        if self.isavailable == True:
            self.movielist.append(movie)
            self.movielist = sorted(self.movielist, key = lambda x: (x.year, x.month, x.day), reverse = True)
            return True
        else:
            print("{} cannot be shown until {}\{}\{}".format(title, date[1],date[2], int(date[0])+4))
            return False
    
    ## remove any movies that are more than 4 years old
    def update(self, expire_date):
        self.isupdated = False
        while self.isupdated != True:
            if len(self.movielist) <= 0:
                break            
            if self.movielist[len(self.movielist)-1].earlierThan(expire_date) == True:
                self.movielist.pop()
            else:
                break
        self.isupdated = True
    
    ## output current movies in archive    
    def printA(self):
        output = ""
        for i in self.movielist:
            output += i.formatMovie()
        return output
    
    
                
        
        