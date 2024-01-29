import re

s = "Hello world is the first program"

# =================SEARCH=================
# match = re.search("first", s)
# print("Start index:", match.start())
# print("End index:", match.end())

# =================SPLITING=================
split = re.split("the", s)
print(split)

subx = re.sub("\s", "9", s)
print(subx)