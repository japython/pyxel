
while True:

    tall = input("身長は?:")
    try:
        tall = float(tall)
    except:
        print("メートル単位で入力してください")
        continue

    weight = input("体重は?")
    try:
        weight = float(weight)
    except:
        print("キログラム単位で入力してください")
        continue
    
    result = weight/pow(tall,2)
    # ここ間違えててなかなか最後まで実行されなかった

    print(f"BMI値は {result:.1f} です。")
    
    if result < 18.5:
        print("やせてます")
    elif 18.5 <= result < 25:    
        print("標準体重です")
    elif 25 <= result < 30:
        print("肥満")
    
    




