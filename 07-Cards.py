import re

pattern = r'[23456789JQKA][SHDC]|10[SHDC]'
text = input()

matches = re.findall(pattern, text)

print(' '.join(matches))