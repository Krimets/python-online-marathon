class MyError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def check_positive(number):
    try:
        num = float(number)
        if num > 0:
            return f'You input positive number: {num}'
        else:
            raise MyError(f"You input negative number: {num}. Try again.")
    except MyError as e:
        return e.data
    except:
        return 'Error type: ValueError!'
