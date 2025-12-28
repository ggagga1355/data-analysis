# day01 데이터 분석 실습

import pandas as pd
import matplotlib.pyplot as plt

# CSV 불러오기
df = pd.read_csv("data.csv")

print(df.head())
print(df.info())
print("\n======================================\n")

# 평균점수
print("평균점수 : ", df["score"].mean())

# 최고점수
print("최고점수 : ", df["score"].max())

print("\n================= 시각화 ==============\n")
plt.bar(df["name"], df["score"])
plt.title("Score by Name")
plt.show()


