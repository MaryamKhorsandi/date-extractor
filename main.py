
# https://github.com/MaryamKhorsandi/date-extractor.git

import re

text = input()

pattern = (
    r'(?<!\d)(?:'
    r'(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])|'
    r'(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/(\d{4})'
    r')(?!\d)'
)

matches = re.finditer(pattern, text)

dates = []

for match in matches:
    if match.group(1):
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
    else:
        day = match.group(4)
        month = match.group(5)
        year = match.group(6)

    dates.append(f"{year}-{month}-{day}")

if dates:
    print("\n".join(dates))
else:
    print("None")
