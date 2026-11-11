import datetime, holidays, main


def manage_schedule():
    pl_holidays = holidays.country_holidays('PL')
    date_today = datetime.date.today()

    is_weekend = date_today.isoweekday() in (6,7)
    is_holiday = date_today in pl_holidays

    if (is_weekend or is_holiday):
        print("Weekend or holiday")
        return 0

    #holiday handelig
    check_date = date_today - datetime.timedelta(days=1)
    date_list = []
    if check_date in pl_holidays:
        date_list.append(check_date.strftime("%Y-%m-%d"))
        check_date = check_date - datetime.timedelta(days=1)
        while check_date in pl_holidays or check_date.isoweekday() in (6,7):
            date_list.append(check_date.strftime("%Y-%m-%d"))
            check_date = check_date - datetime.timedelta(days=1)
        return date_list

    if date_today.isoweekday() == 1:
        for i in range(0,3):
            date_list.append((check_date - datetime.timedelta(days=i)).strftime("%Y-%m-%d"))
        return date_list


    return check_date.strftime("%Y-%m-%d")

def main_trigger(something):
    if type(something) == str:
        main.process_daily_rate(something)
    elif type(something) == list:
        main.process_time_rate(something)




if __name__ == '__main__':
    anserw = manage_schedule()
    main_trigger(anserw)