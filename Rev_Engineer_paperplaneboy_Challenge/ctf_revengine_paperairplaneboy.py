
rev_flag = "cF/r;i{ID8BW"

flag = ""

for i in range(0,12):
	flag = flag + chr((ord(rev_flag[i]) + 4 - (i*3)) % 128)

print(flag)

file = open("flag.txt", "w")

file.write(flag)
file.close()