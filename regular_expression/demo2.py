# import re
# x="[abc]"
# matcher=re.finditer(x,"abc c@5kzabc")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x="[^abc]"
# matcher=re.finditer(x,"abc c@5kzabc")
# for match in matcher:
#     print(match.start())
#     print(match.group())

import re
x="[a-z]"
matcher=re.finditer(x,"abc c@5kzabc")
for match in matcher:
    print(match.start())
    print(match.group())