import pandas

excel_data_df = pandas.read_excel('D:\\input2.xlsx', sheet_name='MAU', header=10, usecols= range(1,8), nrows= 52)

listStudent = []
for rowRaw in excel_data_df.iterrows():
    studentRaw = rowRaw[1].to_dict()
    ini_Key = ['0', '1', '2', '3', '4', '5']
    student = dict(zip(ini_Key, list(studentRaw.values())))
    listStudent.append(student)

def sapXepTangDan(listStudent):
    lenth = len(listStudent)
    for i in range(0, lenth - 1):
        for j in range(i + 1, lenth):
            if listStudent[i]['2'] < listStudent[j]['2']:
                # Hoán đổi vị trí
                tmp = listStudent[i]
                listStudent[i] = listStudent[j]
                listStudent[j] = tmp
    return listStudent

sapXepTangDan(listStudent)
#Sắp xếp theo tên z->a
lenth = len(listStudent)
for i in range(0, lenth-1):
    print(listStudent[i]['2'])