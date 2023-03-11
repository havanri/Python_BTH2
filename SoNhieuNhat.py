arrayNumber=[]
with open('D:\\input.txt', "r") as file_number: # open file in a with statement
    for line in file_number:  # iterate line by line
        numbers = [int(e) for e in line.split()] # split line and convert string elements into int
        print(numbers)
        for number in numbers:
            arrayNumber.append(number)
def findSoNhieuNhat(arrayNumber):
    counter = 0
    numFind = arrayNumber[0]

    for number in arrayNumber:
        curr_frequency = arrayNumber.count(number)
        if (curr_frequency > counter):
            counter = curr_frequency
            numFind = number
    return numFind

print("Số xuất hiện nhiều nhất",findSoNhieuNhat(arrayNumber))