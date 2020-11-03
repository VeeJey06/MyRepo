f = open("modules_list.txt", "r+")
lines = f.readlines()
print(len(lines))
for l in lines:
    for i in range(lines.index(l)+1, len(lines)-1):
        if l == lines[i]:
            lines.pop(i)
f = open("modules_list.txt", "w+")
f.writelines(lines)