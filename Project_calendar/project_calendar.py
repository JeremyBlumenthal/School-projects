#INFO-F-101 school project: .ics file event filter

import codecs
from sys import argv


fileIN = argv[1]
fileOUT = argv[2]


def validate(event):
    """
       Applies the parameters on event, returns True if event matches at least one parameter
    """
    res = False
    for condition in parameters:
        if not res:
            check = []

            for element in condition:
                if element in event:
                    check.append(element)
        
            if len(check) == len(condition): #Event must match all conditions of a parameter
                res = True 
   
    return res


fd = codecs.open(fileIN, 'r', 'utf-8')
line = fd.readline()
parameters = []
head = ''
newEvents = ''


#Sets a list of parameters in order to validate the events
for i in range(3,len(argv)): #Parameters start at index 3 in list argv
    condition = ''
    param = []
    j = 0
    rule = False #True when important characters must be added to condition
    
    while j < len(argv[i]): #Goes through each character of the string
        if rule:

            if j+5 <= len(argv[i]): #Prevents index error
                if argv[i][j:j+5] == ' and ' and condition != '':
                    param.append(condition)
                    condition = ''
                    j += 4
                    rule = not rule
            
            if rule:
                condition += argv[i][j]

        if argv[i][j] == ':':
            rule = not rule
            j += 1 #Skip space character after ':'

        j += 1

    param.append(condition)
    parameters.append(param)


#sets the headers of the file in var head
while line != 'BEGIN:VEVENT\r\n':
    head += line
    line = fd.readline()


#sets all the validated events in a new list
while line != 'END:VCALENDAR\r\n':
    event = line
    line = fd.readline()
    
    while line != 'END:VEVENT\r\n':
        event += line
        line = fd.readline()
    
    event += line
    line = fd.readline()
    valid = validate(event)

    if valid:
        newEvents += event


#last line of the original ics file
tail = line
fd.close()


#The new calendar is written to the output file
file = codecs.open(fileOUT, 'w', 'utf-8')
file.write(head)
file.write(newEvents)
file.write(tail)
file.close()
