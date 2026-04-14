from file_handler import save_expense

def add_expense(amount, category):
    data = f"{amount},{category}"
    save_expense(data)
    return data

