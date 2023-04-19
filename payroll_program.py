import pandas as pd
# Cheylan, Jonathan, Olufemi, Rekik, Henry

# Loading the input text file
df = pd.read_csv("payroll.txt")

# Creating additional columns
df["regular_pay"] = ""
df["ot_pay"] = ""
df["gross_pay"] = ""
df["fed_tax"] = ""
df["state_tax"] = ""
df["fica"] = ""
df["net_pay"] = ""

# Defining a function that calculates regular pay
def calculate_regular_pay(x):
    return  x.pay_rate * x.hours_worked if x.hours_worked <= 40 else 40 * x.pay_rate

# Assigning calculated column for regular pay
df["regular_pay"] = df.apply(calculate_regular_pay, axis=1)

# Defining a function that calculates OT Pay
def calculate_overtime_pay(x):
    return (x.hours_worked - 40) * (1.5 * x.pay_rate)  if x.hours_worked > 40 else 0

# Assigning calculated column for OT pay
df["ot_pay"] = df.apply(calculate_overtime_pay , axis=1)


# Defining a function that calculates gross pay
def calculate_gross_pay(x):
    return x.regular_pay + x.ot_pay

# Assigning calculated column for gross pay
df["gross_pay"] =  df.apply(calculate_gross_pay, axis=1)

# Defining a function that calculates fed tax
def calculate_fed_tax(x):
    return x.gross_pay * .10

# Assigning calculated column for fed tax
df["fed_tax"] = df.apply(calculate_fed_tax, axis=1)

# Defining a function that calculates state tax
def calculate_state_tax(x):
    return x.gross_pay * .06

# Assigning calculated column for state tax
df["state_tax"] = df.apply(calculate_state_tax, axis=1)

# Defining a function that calculates fica
def calculate_fica(x):
    return x.gross_pay * .03

# Assigning calculated column for fica
df["fica"] = df.apply(calculate_fica, axis=1)

# Assigning calculated column for net pay
def calculate_net_pay(x):
    return x.gross_pay - (x.fed_tax + x.state_tax + x.fica)

# Assigning calculated column for net pay
df["net_pay"] = df.apply(calculate_net_pay, axis=1)


def format_column(df, column_name):
    return df[column_name].map(lambda x: format(x, ".2f"))
    

# Formatting values to 2 decimal places
df["pay_rate"] = format_column(df, "pay_rate")
df["regular_pay"] = format_column(df,"regular_pay")
df["ot_pay"] = format_column(df,"ot_pay")
df["gross_pay"] = format_column(df,"gross_pay")
df["fed_tax"] = format_column(df,"fed_tax")
df["state_tax"] = format_column(df,"state_tax")
df["fica"] =  format_column(df,"fica")
df["net_pay"] =  format_column(df,"net_pay")


# Renaming columns
df = df.rename(columns={
    "employee_name": "Employee Name",
    "pay_rate": "Pay Rate",
    "hours_worked": "Hours Worked",
    "regular_pay": "Regular Pay",
    "ot_pay": "OT Pay",
    "gross_pay": "Gross Pay",
    "fed_tax": "Fed Tax",
    "state_tax": "State Tax",
    "fica": "FICA",
    "net_pay": "Net Pay",
})

# Printing and creating output file
print(df.to_markdown())
df.to_csv("output.txt", index=False)