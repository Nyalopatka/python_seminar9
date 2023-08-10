import text as txt
import view

def find(text):
    print(txt.bs*10)
    with open(txt.path, 'r') as data:
        for line in data:
            list1 = list(line.strip(txt.bs).split(txt.s))
            if text in list1:
                view.print_message(line)
                return line
        view.print_message(txt.not_found)
        return

def clearAll():
    with open(txt.path,'w') as data:
        data.write('')
        print(txt.bs*10)
        view.print_message(txt.empty)
        

