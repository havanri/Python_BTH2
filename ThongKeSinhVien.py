import pandas

excel_data_df = pandas.read_excel('D:\\input2.xlsx', sheet_name='MAU', header=10, usecols= range(1,8), nrows= 52)

listStudent = []
for rowRaw in excel_data_df.iterrows():
    studentRaw = rowRaw[1].to_dict()
    ini_Key = ['0', '1', '2', '3', '4', '5','6']
    student = dict(zip(ini_Key, list(studentRaw.values())))
    listStudent.append(student)

def thongKeSinhVien(listStudent):
    sinhvienGioi=0
    sinhvienKha=0
    sinhvienTB=0
    diemXepLoai = 0;
    lenth = len(listStudent)
    for i in range(0, lenth - 1):
        diemXepLoai = (listStudent[i]['4'] + listStudent[i]['5'] + listStudent[i]['6'])/3;
        print(diemXepLoai)
        if diemXepLoai >= 8:
            sinhvienGioi = sinhvienGioi + 1
        elif diemXepLoai >= 6.5:
            sinhvienKha = sinhvienKha + 1
        else:
            sinhvienTB = sinhvienTB + 1

    print("Số lượng sinh viên giỏi",sinhvienGioi)
    print("Số lượng sinh viên khá", sinhvienKha)
    print("Số lượng sinh viên trung bình", sinhvienTB)

thongKeSinhVien(listStudent)