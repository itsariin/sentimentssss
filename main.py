import string

text = open('read.txt',encoding='utf-8').read()
print(text)

lower_case = text.lower()    #lower downed the cases here
print(lower_case)

print(string.punctuation)

cleaned = lower_case.translate(str.maketrans('','',string.punctuation))

#In the above three string sapce what does it takes

#str 1: Specifies the list of characters that needs to be replaced
#str 2: Specifies the list of characters with which character needs to be replaced
#str 3: Specifies the list of characters that needs to be deleted

#str 1:-> 'abc'
#str 2:-> 'gfh'

#Returns : Returns the translation table which specifies the conversions that can be used by 


print(cleaned)