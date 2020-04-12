import re
from _ast import Expression
from email._header_value_parser import Domain

email = 'test@gmail.com'
expression = '[a-z]+'
matches = re.findall(expression, email)
print(matches)

name = matches[0]

domain =f'{matches[1]}.{matches[2]}'

print(name)
print(domain)



