# print("opening the file")
# fh=open("write1.txt",'r+')
# print("reading the files")
# lines=fh.readlines()
# print("The content of files is", lines)
# print("closing the file")
# print(lines)
# fh.close()

print("opening the file")
fh=open("E:/write1.txt/pyprogram",'r')
print("reading the files")
print(fh.tell())
fh.readlines()

fh.seek(1000,0)
print(fh.tell())
fh.write("1 gb data")
fh.close()
