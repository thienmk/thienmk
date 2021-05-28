#Nhập số nguyên dương
def read_number(text_number):
    #sử dụng vòng lắp while để loại trừ các trường hợp nhập k phải số nguyên
    while True:
        try: #hàm try để chia trường hợp
            numbeer = int(input(text_number))
            print(numbeer)
            break #nếu số đã nhập đúng là số nguyên thì break thoát vòng lắp
        except ValueError:
            print('input agian')
        except KeyboardInterrupt:
            print('input again')

    return numbeer #trả về kết quả là số nguyên đã nhập vào

#nhập số sale
sales = []
no_of_srand = read_number('input your number of stand: ')
for count in range(1,no_of_srand + 1):
    text_number = 'input your sale for stand ' + str(count) + ':'
    sales.append(read_number(text_number))
    count = count + 1
print(sales)

# nhập lại số sale
def input_again_sales():
    sales.clear()
    no_of_srand = read_number('input your number of stand: ')
    for count in range(1,no_of_srand + 1):
        text_number = 'input your sale for stand ' + str(count) + ':'
        sales.append(read_number(text_number))
         
# in số sales ra màn hình
def print_sales():
    count = 1
    for sales_value in sales:
        print('sales for stand ', count , 'is ' , sales_value)
        count = count + 1

#tạo hàm xép số sales từ nho đến lon
def sort_low_to_high():
    print(sales.sort())

def maxnimum_sales():
    '''print out the list of sales sorted low to high'''
    for count in range(0,int(len(sales) - 1)):
        if sales[count] < sales[count + 1]:
            temp = sales[count]
            sales[count] = sales[count + 1]
            sales[count + 1] = temp
    print('minimum sales is: ', temp)

#tạo hàm xếp số sales từ lowns dden be 
def sort_high_to_low():
    '''print out the list of sales sort high to low'''
    pass

# Total sales
def total_sales():
    print('total sales is: ', sum(sales))

# Highest Lowest
def highest_lowest():
    pass

# Average sales
def average_sales():
    sum_sales = 0
    for i in sales:
        sum_sales = sum_sales + i
        avg = sum_sales / len(sales)
    print('Average sales is: ', avg)

# Tạo hàm input command cho người dùng
def read_int_range(promt,min_number,max_number):
    if min_number>max_number:
        raise Exception("min number must lower than max number")
    while True:
        command_number = read_number(promt)
        if command_number < min_number:
            print('number you input is to low')
            print('minum is: ', min_number)
            continue
        if command_number > max_number:
            print('number you input is to high')
            print('maxnimun is: ', max_number)
            continue
        break
    return command_number

# Tạo menu cho người dùng
menu = '''Ice-cream Sales

1: Print the Sales
2: Sort High to Low
3: Sort Low to High
4: Highest And Lowest
5: Total Sales
6: Average sales
7: Enter Fifures
0: End 

Enter your command: '''
while True:
    command = read_int_range(menu,1,8)
    if command == 1:
        print_sales()
        continue
    elif command == 2:
        sort_high_to_low()
        continue
    elif command == 3:
        sort_low_to_high()
        continue
    elif command == 4:
        highest_lowest()
        continue
    elif command == 5:
        total_sales()
        continue
    elif command == 6:
        average_sales()
        continue
    elif command == 7:
        input_again_sales()
        continue
    elif command == 8:
        print('thanks')
        break
    