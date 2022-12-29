def day_of_week(day):
    week = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    try:
        if 8 > int(day) > 0:
            return week[int(day)]
        else:
            return 'There is no such day of the week! Please try again.'
    except:
        return 'You did not enter a number! Please try again.'
