def student(name):
    dic = {"naseef":89,"abinav":91,"vivek":85,"hridul":94,"minhaj":83,"midlaj":84,"abinand":90,"arjun":88}
    return dic[name]
s = input("enter the student name: ")
a = student(s)
print("Mark of student {}  : {}".format(s,a))