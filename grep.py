# imports the regular expressions library
import re 

#sets the counts as a list
lst = list()

# reads in mbox-short.txt
fhandle = input('Enter a file name:')
if len(fhandle) < 2:
    fhandle = open('mbox-short.txt')
else:
    print('Please just press enter.')
    quit()

# asks the user for a regular expression value for which to check the file
regex = input('Type a regular expression to query the file: ')

# clone of grep command from Unix
for line in fhandle:
    line = line.rstrip()
    lst.append(re.findall(regex, line))
    #print(lst)

# prints the number of lines that match this query
print('This file had',len(lst), 'lines that matched your query.')