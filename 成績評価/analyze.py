import pandas as pd

df = pd.read_csv('成績一覧表.csv')
filtered_data = df[(df['合計'] >= 300) & (df['国語'] >= 80) & (df['数学'] >= 80) & (df['英語'] >= 80)]

print("合格の生徒: ")
print(filtered_data)

filtered_data.to_csv('合格生徒一覧表.csv', index=False)