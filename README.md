# dataframe_diff

dataframe_diff is a micro-library which takes two dataframes as input , compares them and return two dataframes with column wise comparison and additional records.

## Installation

pip install dataframe-diff

## Examples

>>> import pandas as pd
>>> df1=pd.read_csv('students_1.csv')
>>> df2=pd.read_csv('students_2.csv')
>>> from dataframe_diff import dataframe_diff
>>> df1.head()
      Name Subjects  Marks Grade
0  Leonard      Eng     70     B
1  Leonard     Math     80     B
2  Leonard  Physics     90     A
3  Sheldon      Eng     90     A
4  Sheldon     Math     99     A
>>> df2.head()
      Name Subjects  Marks Grade
0  Leonard      Eng     75     A
1  Leonard     Math     85     A
2  Leonard  Physics     90     A
3  Sheldon      Eng     99     A
4  Sheldon     Math     99     A
>>> d1_column,d2_additional=dataframe_diff(df1, df2, key=['Name','Subjects'])
>>> d1_column
      Name Subjects value_x value_y column_name
0  Leonard      Eng      70      75       Marks
1  Leonard      Eng       B       A       Grade
2  Leonard     Math      80      85       Marks
3  Leonard     Math       B       A       Grade
4  Sheldon      Eng      90      99       Marks
5    Penny  Physics      65      75       Marks
6    Penny  Physics       C       B       Grade
>>> d2_additional
     Name   Subjects  Marks Grade  sets
0  Rajesh       Math     93     A  df_x
1  Howard  Chemistry     83     B  df_y


