'''
Created on Nov 13, 2025

@author: jacksonhooper
'''

import csv
import time

# After doing more research into possible interpretations of string hash encoding, I have adapted code that uses the alphanumeric
# interpreting to create the hash code that I used as the basis for my first control attempt. 

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
    
    p = 53
    m = 20011
    hash_value = 0
    p_pow = 1
    
    for c in str:
        
        hash_value = (hash_value + (ord(c) + 1) * p_pow) % m
        p_pow = (p_pow * p) % m
        
    return int(hash_value);

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
