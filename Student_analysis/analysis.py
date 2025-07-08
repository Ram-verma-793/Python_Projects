import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("student_marks.csv")

print("----------Student statistics------------")
print("Average marks per subject:\n", df.mean(numeric_only=True))

print("Highest Score:")
print(df.loc[df[['Maths', 'Physics', 'Chemistry', 'English', 'Computer']].sum(axis=1).idxmax()])

print("Lowest Score:")
print(df.loc[df[['Maths', 'Physics', 'Chemistry', 'English', 'Computer']].sum(axis=1).idxmin()])

df["Total"] = df[['Maths', 'Physics', 'Chemistry', 'English', 'Computer']].sum(axis=1)
df["Average"] = df['Total'] / 5

df["Result"] = df[['Maths', 'Physics', 'Chemistry', 'English', 'Computer']].apply(lambda x: 'Pass' if all(x >= 40) else 'Fail', axis=1)

print(df)


df.to_csv("student_analysis_result.csv", index=False)
print("\nResult saved to student_analysis_result.csv")


# matplotlib 

pass_fail_counts = df["Result"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(pass_fail_counts, labels=pass_fail_counts.index, autopct='%1.1f%%', startangle=90, colors=["lightgreen", "salmon"])
plt.title("Pass vs Fail Distribution")
plt.show()


plt.figure(figsize=(10,5))
plt.plot(df["Name"], df["Total"], marker='o', color='purple')
plt.title("Total Marks of Each Student")
plt.xlabel("Student")
plt.ylabel("Total Marks")
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()
