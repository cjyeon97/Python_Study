# 파일을 연다 header를 가지고 온다.
file = open("./C_nt.fas")
lines = file.readlines()

targetFile = open("result.txt","w+")
for line in lines:
    if ">" in line:
        header = line.replace(">","")
        targetFile.write(header)
targetFile.close()
