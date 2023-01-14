from datetime import datetime, timedelta  
one_week_ago = datetime.today() - timedelta(days=7) #Weekly
day = datetime.now().today #Today

    
def _get_dates_of_week(now):
    this_week = ['date' for i in range(7)]
    current_day = now.weekday()
    if current_day == 6:
        this_week[0] = now
        for i in range(1, 7):
            add_date = now + timedelta(days=i)
            this_week[i] = add_date
    else:
        num_things_before = current_day + 1
        num_things_after = 5 - current_day
        sunday = now - timedelta(days=current_day + 1)
        this_week[0] = sunday

        for i in range(0, current_day):
            diff = current_day - i
            add_date = now - timedelta(days=diff)
            this_week[i + 1] = add_date
        for j in range(current_day + 1, 7):
            diff = j - current_day - 1
            add_date = now + timedelta(days=diff)
            this_week[j] = add_date
    return this_week