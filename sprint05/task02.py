def check_odd_even(n):
    try:
        if n % 2 == 0:
            return 'Entered number is even'
        else:
            return 'Entered number is odd'
    except:
        return 'You entered not a number.'
