import re

filter = input()
the_letter = filter[0]
letter_count = int(filter[1])

pattern = r'\b\w+\b'
sentence_pattern = r'^[A-Z].*[\.\?\!]$'

data = input()
list_text = []
while data != "end":
    match = None
    match = re.match(sentence_pattern, data)

    if match != None:
        list_text.append(data)
    data = input()
text = ' '.join(list_text)

result_list = []
matches = re.findall(pattern, text)
for match in matches:
    if match.count(the_letter) >= letter_count:
        result_list.append(match)

print(', '.join(result_list))