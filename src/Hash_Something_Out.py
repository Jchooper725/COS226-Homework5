'''
Created on Nov 13, 2025

@author: jacksonhooper
'''

import csv
import time

# Decided to focus on what could be causing the massive disparity between the collisions and wasted space between the hash function
# when called on the title as opposed to the quote. My first thought was that it may have something to do with the length of the strings 
# being used, since the quotes are consistently longer than the titles. To test this, I am going to turn the string inserted, whether a
# title or string, into a string of length 50 by having the original string repeat until it reaches that length.

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

def hashFunction(str):
    
    s = ""
    
    for i in range(50):
        
        s += str[i%len(str)]
    
    h = 0x811c9dc5  # 32-bit offset basis
    fnv_prime = 0x01000193  # 32-bit FNV prime

    for char in s:
        h ^= ord(char)
        h = (h * fnv_prime) % (2**32)  # stay in 32-bit space

    return h

def hashTitle(data, array):
    
    collisions = 0
    
    h = hashFunction(data.title)
    indexTitle = h % len(array)
    
    if array[indexTitle] != None:
        collisions = 1
    
    array[indexTitle] = data
    
    return array, collisions


def hashQuote(data, array):
    
    collisions = 0
    
    h = hashFunction(data.quote)
    indexQuote = h % len(array)
    
    if array[indexQuote] != None:
        collisions = 1
    
    array[indexQuote] = data
    
    return array, collisions
    


def main():
    
    title = [None] * 20011
    quote = [None] * 20011
    
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
    for i in quote:
        if i == None:
            qCountEmpty += 1
            
    print(f"Wasted space: {qCountEmpty}")
    print(f"Collisions: {quoteCollisions}")
    
    
    
if __name__ == '__main__':
    main()
