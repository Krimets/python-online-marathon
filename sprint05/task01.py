def divide(numerator, denominator):
    try:
        return f'Result is {numerator / denominator}'
    except ZeroDivisionError:
        return f'Oops, {numerator} / {denominator}, division by zero is error!!!'
    except:
        return 'Value Error! You did not enter a number!'
