'''
Created on Nov 13, 2025

@author: jacksonhooper
'''

import csv




def main():
    
    file = "MOCK_DATA.csv"
    counter = 0
    
    with open(file, 'r', newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
            # create a DataItem from row
            # feed the appropriate field into the hash function to get a key
            # mod the key value by the hash table length
            # try to insert DataItem into hash table
            # handle any collisions
            
            counter += 1


if __name__ == '__main__':
    main()
