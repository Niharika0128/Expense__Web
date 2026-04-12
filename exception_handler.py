def validate(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False

print(validate("100"))
print(validate("abc"))