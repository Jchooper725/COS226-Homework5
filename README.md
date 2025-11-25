The first attempt at a hash function was to obtain a footing so that my subsequent attempts would be easier to interpret and I could ensure that my measurements on time, wasted space,
and collisions were accurate. Having a predictable hash function to begin was an important step in comparing the ones that followed.
The second attempt made use of the entire strings and attempted a uniform distribution that was shown to not be occuring when increasing the size of the hash table. This is where I realized
that using modulo to conform the hash encoding to the size of the array would allow me more freedom in ensuring that the distribution was uniform. By disregarding the size of the table in making
the hash code, i could make better use of the table.
The third attempt at encoding yielded much more promising results, getting my collisions down to around 6300 for the titles and around 4500 for the quotes. For a table of size 20011 and 15001
pieces of data to add this was promising, but I was interested in why there was such a large difference in the number of collisions between the quotes and titles. After looking at the data table,
I saw that on average the quotes strings were a significant amount larger in size than the titles. I thought that this might be the cause.
So for the fourth attempt, I made the strings that were inputted into the hash function length 50 regardless of their original size to see if the size of the strings was changing how effective 
the encoding was. After implementing this code and getting 15 more collisions for titles and 87 more collisions for the quotes i came to the conclusion that the length of the strings was not the 
cause of the disparity.
For my final attempt, I researched some more about hash table construction as it pertains to strings and found a function that utilized the ord() function similarly to how i did in my second 
attempt, but used it in such a way that it more uniformly distributed the data. Taking inspiration from this, I emulated the function in python as it was originally in java. This function yielded
the best results of any attempt with 6368 collisions for the titles and 4426 collisions for the quotes. All the times for all the different functions were similar enough that fluctuations between 
separate runs would cause them to overlap in such a way that it was not possible to tell if one was significantly faster than another.
