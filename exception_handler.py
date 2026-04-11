def validate(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False