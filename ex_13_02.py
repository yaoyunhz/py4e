#ex_13_02.py

#Extracting Data from JSON
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
#The program will prompt for a URL, 
#read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, 
#compute the sum of the numbers in the file and enter the sum below:

#We provide two files for this assignment. 
#One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_132471.json (Sum ends with 65)

import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter location: ')
if len(address) < 1: address = 'http://py4e-data.dr-chuck.net/comments_132471.json'
print('Retrieving', address)

urlhand = urllib.request.urlopen(address)
data = urlhand.read().decode()
print('Retrieved', len(data), 'characters')c

info = json.loads(data)
comments = info['comments']
print('Count:', len(comments))

sum = 0
for person in comments:
    num = person['count']
    sum = sum + num
    
print('Sum:', sum)
