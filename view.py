import text as txt

def menu()-> int:
    while True:
        print(txt.main_menu)
        choice = input(txt.input_choice)
        if choice.isdigit() and 0 < int(choice) < 6:
            return int(choice)
        else:menu()
        
def print_message(message):
    print((txt.bs) + '='*len(message))
    print(message)
    print('='*len(message)+(txt.bs))

def printAll():
    print(txt.bs*10)
    with open(txt.path, 'r') as data:
        for line in data:
            print(line)
        print(txt.bs)

def addData():
    with open(txt.path, 'a') as data:
        print(txt.bs*10) 
        first_name = input(txt.name)
        second_name = input(txt.surname)
        number = input(txt.phone)
        item = [first_name, second_name, number]
        data.writelines(txt.s.join(item)+txt.bs)
        print(txt.bs*10)
        
