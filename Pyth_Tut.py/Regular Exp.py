# for removing specific patterns from the string we use regular expressions

import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin fass
fass fass aiaiaiaiaiaiaiaiaiaiai
bahut hi badia aadmi haiaiin'''

# findall,search,split,sub and finditer


# patt = re.compile(r'fass')
# patt = re.compile(r'.m')    #‘.’: Matches any single character except newline
# patt = re.compile(r'^Tata')  # To check if the string is starting from the word
# patt = re.compile(r'iin$')   #To check if the string is ending from the word
# patt = re.compile(r'ai{2}')   #‘{}’: Matches an explicitly specified number of repetitions
# patt = re.compile(r'(ai){5}')  #checks the repition of aiaiaiaiai
# patt = re.compile(r'ai{1}|Fax')


# Special Sequences
# patt = re.compile(r'\ATata')  #for checking starting word
    # the resultant is a match if the input characters are at the beginning of the string
# patt = re.compile(r'Fax\b')   
# patt = re.compile(r'27\b') #
# the resultant is a match whether the input characters 
# are at the beginning or the end of a wor d
# patt = re.compile(r'\d{5}-\d{4}')  #he resultant is a match if the string contains any digits  
# Task
# Given a string with a lot of indian phone numbers starting from +91

# matches = patt.finditer(mystr) #finditer is used to find all matches of a pattern in a string
# for match in matches:
#     print(match)