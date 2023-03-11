arrayNumber=[]
with open('D:\\input.txt', "r") as file_number: # open file in a with statement
    for line in file_number:  # iterate line by line
        numbers = [int(e) for e in line.split()] # split line and convert string elements into int
        print(numbers)
        for number in numbers:
            arrayNumber.append(number)
def amountSoNguyenTo(arrayNumber):
    amount = 0
    for number in arrayNumber:
        divisor = 1
        count = 0
        while(divisor <= number):
            if(number % divisor == 0):
                counter = counter + 1
            divisor = divisor + 1
        if(counter == 2):
            print("so nguyen to", number)
            amount = amount + 1
    return  amount
print("Số lượng số nguyên tố ", amountSoNguyenTo(arrayNumber))