
s = "this is an example AND-THIS-IS-OTHER-EXAMPLE"
suffix = 'example'
term = 'an'
slist = ['1', '2', 'red', 'blue']
old = 'is'
new = 'SON'
delim = ' '
prefix = 'AND'

print(s.endswith(suffix))     # Check if string ends with suffix
print(s.find(term))              # First occurrence of term in s
print(s.index(term))             # First occurrence of term in s
print(s.isalpha())            # Check if characters are alphabetic
print(s.isdigit())            # Check if characters are numeric
print(s.islower())            # Check if characters are lower-case
print(s.isupper())            # Check if characters are upper-case
print(s.join(slist))          # Join a list of strings using s as delimiter
print(s.lower())              # Convert to lower case
print(s.replace(old,new))     # Replace text
print(s.rfind(term))             # Search for term from end of string
print(s.rindex(term))            # Search for term from end of string
print(s.split(delim))       # Split string into list of substrings
print(s.startswith(prefix))   # Check if string starts with prefix
print(s.strip())              # Strip leading/trailing space
print(s.upper())              # Convert to upper case
 
