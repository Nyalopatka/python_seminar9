import text as txt
import view
import model as mod
def start():
    while True:
        choice = view.menu()
        if choice == 1:
            view.addData()
            view.print_message(txt.load_success)
            return True
        elif choice == 2:
            view.printAll()
            return True
        elif choice == 3:
            mod.find(input(txt.finding))
            return True
        elif choice == 4:
            mod.clearAll()
            return True
        else:
            return False