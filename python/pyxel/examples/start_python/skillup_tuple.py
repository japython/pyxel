#%%
family = ['sota','taiki','yuko','teruko','tetsuya']

for i in enumerate(family):
    print(i)


    #if 'o' in e:
    #    print(f"{e} は、'o'を含んでます")
    #else:
    #    print(f"{e} は、'o'を含んでません")

#%%
# リストの定義
list_tohoku = [5349.0, 5478.8, 5344.0, 4644.8, 4948.0, 6259.0]
list_shikoku = [3148.0, 2991.0, 2966.0, 2457.0]

#%%
# 平均値を計算する関数
def average(a):
    sum_ = 0
    for num in a:
        sum_ += num
    return sum_ / len(a)

# どのリストの平均値を計算するか入力
item = input("東北と四国の平均値どちらを計算しますか?: ")

# 入力に応じて平均値を計算し、表示
if item == "東北":
    print(average(list_tohoku))
elif item == "四国":
    print(average(list_shikoku))
else:
    print("入力エラー: 東北または四国を入力してください")
# %%


