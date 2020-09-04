import re

with open('dataset_3363_2.txt') as inf:
    input_string = inf.readline().strip()
with open('output.txt', 'w') as outf:
    outf.write("".join(enc_chars[0] * int(enc_chars[1:]) for enc_chars in re.findall(r"\w\d+", input_string)))
