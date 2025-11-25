'''
Created on Nov 13, 2025

@author: jacksonhooper
'''

import csv
import time

# First attempt at a hash table implementation. This attempt is simple and relies on the first
# letter of the title or quote to create the key. This iteration is primarily to have a 
# predictable outcome so that I may ensure that my functions for obtaining statistics about
# the construction of the hash tables are working properly.

class DataItem:
    
    def __init__(self, title, genre, date, director, revenue, rating, duration, company, quote):
        
        self.title = title
        self.genre = genre
        self.date = date
        self.director = director
        self.revenue = revenue
        self.rating = rating
        self.duration = duration
        self.company = company
        self.quote = quote


def hashTitle(data, title):
    
    collisions = 0
    
    alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    indexTitle = alphanumeric.find(data.title[0].lower())
    
    if title[indexTitle] != None:
        collisions = 1
    
    title[indexTitle] = data
    
    return title, collisions


def hashQuote(data, quote):
    
    collisions = 0
    
    alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    indexQuote = alphanumeric.find(data.quote[0].lower())
    
    if quote[indexQuote] != None:
        collisions = 1
    
    quote[indexQuote] = data
    
    return quote, collisions
    


def main():
    
    title = [None] * 36
    quote = [None] * 36
    
    titleCollisions = 0
    quoteCollisions = 0
    
    file = "MOCK_DATA.csv"
    counter = 1
    
    with open(file, 'r', newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            
            # create a DataItem from row
            # feed the appropriate field into the hash function to get a key
            # mod the key value by the hash table length
            # try to insert DataItem into hash table
            # handle any collisions
            
            data = DataItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            
            tTime = time.perf_counter()
            title, tCollide = hashTitle(data, title)
            titleTime = time.perf_counter() - tTime
            
            qTime = time.perf_counter()
            quote, qCollide = hashQuote(data, quote)
            quoteTime = time.perf_counter() - qTime
            
            quoteCollisions += qCollide
            titleCollisions += tCollide
            counter += 1
        
    print("Time Table Statistics:")
    print(f"Time: {titleTime} seconds")
    
    tCountEmpty = 0
    for i in title:
        if i == None:
            tCountEmpty += 1
            
    print(f"Wasted space: {tCountEmpty}")
    print(f"Collisions: {titleCollisions}")
    
    print("")
    
    print("Quote Table Statistics:")
    print(f"Time: {quoteTime} seconds")
    
    qCountEmpty = 0
    for i in title:
        if i == None:
            qCountEmpty += 1
            
    print(f"Wasted space: {qCountEmpty}")
    print(f"Collisions: {quoteCollisions}")
    
    
    
if __name__ == '__main__':
    main()
