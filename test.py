def error(msg):

    print(f"Error! {msg}")

def main_menu():
    print('Please select an option:\n[1] Process Data\n[2] Query Database\n[3] Visualise Data\n[4] Exit')
    option_chosen = int(input())
    if 1 <= option_chosen <= 4:
        print (f'Your selection: {option_chosen}')
        return option_chosen
    else:
        error('Invalid selection.')
        return -1


main_menu()