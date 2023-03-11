arrayNumber=[]
with open('D:\\input.txt', "r") as file_number: # open file in a with statement
    for line in file_number:  # iterate line by line
        numbers = [int(e) for e in line.split()] # split line and convert string elements into int
        print(numbers)
        for number in numbers:
            arrayNumber.append(number)
def soChanSoLe(arrayNumber):
    demchan = 0
    demle = 0
    for number in arrayNumber:
        if(number % 2 == 0):
            demchan = demchan + 1
        else:
            demle = demle + 1
    print("dem chan", demchan)
    print("demle", demle)
soChanSoLe(arrayNumber)