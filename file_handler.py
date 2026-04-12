from variables import FILE_NAME

def save_expense(data):
    with open(FILE_NAME, "a") as file:
        file.write(data + "\n")

def read_expense():
    data = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data.append(line.strip())
    except FileNotFoundError:
        pass
    return data

# test
save_expense("200,Travel")
print(read_expense())