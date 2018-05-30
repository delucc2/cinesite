## Name: Movie Archive File Test
## Purpose: Test functionality for UPAC Cinema site and outputs updated archive to file
## Programmer: Autumn Walters on May 25, 2018

from Movie import *
from Archive import *
import sys

def read_from_file(filename):
    file = open(filename, "r")
    count = -1
    ## Handle one input line at a time
    for line in file:
        info = line.strip().split("*")
        ## Outputs error if number of values read in is not 4
        if len(info) != 4:
            print(info)
            print("Error: Incorrect number of inputs")
            file.close()
            return None
        movie = Movie(info[0].strip(), info[3].strip(), info[1].strip(), info[2].strip())
        count += 1
        ## Add movies to archive
        if count == 0:
            archive = Archive(movie)
        else:
            archive.addMovie(movie)
    file.close()
    return archive

if __name__=="__main__":
    fn = "movie_archive.txt"
    
    ## Open file and populate archive
    archive = read_from_file(fn)
    if archive == None:
        print("Error: Read Failed")
        sys.exit()
    else:
        ## Will change later to read in the current date
        print("Enter current date:")
        month = input("Month: ")
        day = input("Day: ")
        year = input("Year: ")
        expire = [int(year)-4, month, day]
        archive.update(expire)
        
        ## Continues to ask user to input movies until it one is available
        movie_title = input("Request a movie: ")
        movie = Movie(movie_title.strip(), year, month, day)
        added = archive.addMovie(movie)
        while added == False:
            movie_title = input("Request a movie: ")
            movie = Movie(movie_title.strip(), year, month, day)
            added = archive.addMovie(movie)
        print("Added! {} on {}\{}\{}".format(movie_title, month, day, year))
        
        ## Output archive to new file [We can change this to overwrite the previous file]
        file = open("updated_archive.txt","w")
        file.write(archive.printA())
        file.close()
        
