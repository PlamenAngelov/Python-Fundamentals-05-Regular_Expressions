import re

in_str = input()

happy_pattern = r"(:[\)D*\]}]|;[\)\]}]|[\(*c\[]:|\[;)"
sad_pattern = r"(:[\(\[{c]|;[\(\[{]|[\)\]D]:|];)"

happy_list = []
sad_list = []

matches = re.finditer(happy_pattern, in_str)
for match in matches:
    happy_list.append(match.group())

matches = re.finditer(sad_pattern, in_str)
for match in matches:
    sad_list.append(match.group())


emoticon = ''
index = len(happy_list)/len(sad_list)
if index > 2:
    emoticon = ":D"
elif index > 1:
    emoticon = ":)"
elif index == 1:
    emoticon = ":|"
else:
    emoticon = ":("

print(f"Happiness index: {index:.2f} {emoticon}")
print (f"[Happy count: {len(happy_list)}, Sad count: {len(sad_list)}]")
