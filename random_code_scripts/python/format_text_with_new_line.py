from os import system

file_name = input("File to remove \\n: ")
t = ""
words = []

with open (file_name, "r") as fhead_i:
    for l in fhead_i:
        words += l.strip().split(" ")

i = 0
l = len(words)

while i < l:
    if "." in words[i] or "?" in words[i] or "!" in words[i]:
        words = words[:i + 1] + ["\n", "\n"] + words[i + 1:]
        i += 2

    i += 1

t = " ".join(words)

with open ("opt_text.txt", "w") as fhead_o:
    fhead_o.write(t)

#system(f"mv opt_text.txt \'{file_name}\'")
#system(f"mv \'{file_name}\' ../branch_education_comments")
#system(f"rm \'{file_name}\'")
