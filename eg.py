import pandas as pd


students=(

{
    "name":"logu",
    "age":18,
    "mark":60
}
,
{
    "name":"tharu",
    "age":18,
    "mark":87
}
,
{
    "name":"tharanie",
    "age":18,
    "mark":86
}
,
{
    "name":"tharu",
    "age":18,
    "mark":89
})

students_df=pd.DataFrame(students)
#df=pd.DataFrame(students).[dropna()--- remove the none value
#print(df.tail(2))

MARKS_TRESHOLD=85
student_marks_greater_than_treshold=students_df[students_df['mark']>MARKS_TRESHOLD]
print(student_marks_greater_than_treshold)
print(student_marks_greater_than_treshold.count())
#student_marks_greater_than_treshold.to_csv("dataset.csv",index=False)
student_marks_greater_than_treshold.to_csv("dataset.csv")

