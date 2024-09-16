#『スキルアップ教科書』P255 問題2

#%%
data =[
       ['0001','Male','Yamada','Tarou','25','Tokyo'],
       ['0002','Male','Satou','Takeshi','27','Kanagawa'],
       ['0003','Female','Tanaka','Yuko','25','Saitama'],
       ['0004','Male','Suzuki','Ishirou','35','Hokkaidou']
]

members = {}

for i in data:
    members[i[0]] = [i[1],i[2],i[3],i[4],i[5]]


# %%
dict_national_tel = {1:'Amarica',30:'Greece',39:'Italia',44:'UK',53:'Cuba',54:'Argentina',81:'Japan'}

#%%
for i in dict_national_tel.values():
    print(i)

# %%
