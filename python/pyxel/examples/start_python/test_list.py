from datetime import datetime as dt

day = input("調べたい日時？（形式 YYYYMMDD）:")

target_day = dt.date.str_to_date(day)


if 1 <= target_day.weekday() <= 5:

    print('平日だからがんばろー')


else:

    print('ゆっくりやすみましょうー')