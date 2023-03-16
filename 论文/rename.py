import os

file_dict = {}
cnt = 1
for file_name in os.listdir("./"):
    if not file_name.endswith(".pdf"):
        continue
    t = os.path.getctime(file_name)
    tmp = file_name.split("_")
    if len(tmp) > 1:
        tmp = tmp[1:]
    file_name1 = "{}_".format(cnt) + "".join(tmp)
    os.rename(file_name, file_name1)
    cnt += 1

a = 1
