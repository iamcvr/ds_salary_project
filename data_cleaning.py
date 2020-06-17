# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:26:35 2020

@author: Al Mair
"""

import pandas as pd
df = pd.read_csv("glassdoor_jobs.csv")

#salary parsing
df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split("(")[0])
salary_kd = salary.apply(lambda x: x.replace("K", "").replace("$",""))

df["Hourly"] = df["Salary Estimate"].apply(lambda x: 1 if "per hour" in x.lower() else 0)
df["Employer Provided"] = df["Salary Estimate"].apply(lambda x: 1 if "employer provided" in x.lower() else 0)

min_hr = salary_kd.apply(lambda x: x.replace("Per Hour", "").replace("Employer Provided Salary:",""))

df['min_salary'] = min_hr.apply(lambda x: int(x.split("-")[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split("-")[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#company name text only
df['company_text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x["Company Name"][:-3], axis = 1)

#state field 
df["job_state"] = df["Location"].apply(lambda x: x.split(",")[-1])
df.job_state.value_counts()

#same state as HQ
df["same_state"] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of company
df["company_age"] = df.Founded.apply(lambda x: x if x <0 else 2020 - x)
#parsing of job description (python, etc)

#python
df["python_yn"] = df["Job Description"].apply(lambda x: 1 if "python" in x.lower() else 0)
#r studio
df["r_studio_yn"] = df["Job Description"].apply(lambda x: 1 if "r studio" in x.lower() else 0)
#spark
df["spark_yn"] = df["Job Description"].apply(lambda x: 1 if "spark" in x.lower() else 0)
#aws
df["aws_yn"] = df["Job Description"].apply(lambda x: 1 if "aws" in x.lower() else 0)
#excel
df["excel_yn"] = df["Job Description"].apply(lambda x: 1 if "excel" in x.lower() else 0)

df.columns
df_out = df.drop(['Unnamed: 0'],axis=1)

df_out.to_csv("salary_data_cleaned.csv",index = False)