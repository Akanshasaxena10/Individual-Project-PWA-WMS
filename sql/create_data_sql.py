from data import personnel
from data import stock
def get_employee_sql(employees,head_of = None):
    for employee in employees:
        print(f"({employee['user_name']}, {employee['password']}),")
print("INSERT INTO Employee (user_name, password) VALUES")
get_employee_sql(personnel)