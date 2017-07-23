# -*-coding:GBK-*-
text2=open('data2','rb')
text3= open('data3','rb')

text2.readline()#跳过第一行
text3.readline()
lines2 = text2.readlines()
lines3 = text3.readlines()

list2_name = []
list2_tele = []
list3_name = []
list3_email = []
lines = []

for line in lines2:     #获取data2中的信息
    key = line.split()
    list2_name.append(str(key[0].decode('gbk')))
    list2_tele.append(str(key[1].decode('gbk')))
for line in lines3:      #获取data3中的信息
    key = line.split()
    list3_name.append(str(key[0].decode('gbk')))
    list3_email.append(str(key[1].decode('gbk')))
#按照索引遍历data2
for i in range(len(list2_name)):
    if list3_name[i] in list2_name:
        j = list3_name.index(list2_name[i])
        s = '\t'.join([list2_name[i],list2_tele[i],list3_email[j]])
        s += '\n'
    else:
        s = '\t'.join([list2_name[i],list2_tele[i],str('-------')])
        s += '\n'
    lines.append(s)
#处理data3中剩余姓名
for i in range(len(list3_name)):
    s=''
    if list3_name[i] not in list2_name:
        s = '\t'.join([list3_name[i],str('--------'),list3_email[i]])
        s += '\n'
    lines.append(s)
text4 = open('data4','w')
text4.writelines(lines)

text2.close()
text3.close()
text4.close()