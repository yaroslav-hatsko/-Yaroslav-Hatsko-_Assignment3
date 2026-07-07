employees = [
    {"name": "Олена", "department": "Marketing", "salary": 25000},
    {"name": "Ігор", "department": "IT", "salary": 55000},
    {"name": "Наталія", "department": "Marketing", "salary": 28000},
    {"name": "Олег", "department": "HR", "salary": 22000},
    {"name": "Андрій", "department": "IT", "salary": 48000},
    {"name": "Марія", "department": "IT", "salary": 52000},
]
def get_department_stats(employee_list, target_dept):
    total_salary = 0
    count = 0
    max_salary = 0
    top_earner = ""
    for employee in employee_list:
        if employee["department"] == target_dept:
            count += 1
            total_salary += employee["salary"]

            if employee["salary"] > max_salary:
                max_salary = employee["salary"]
                top_earner = employee["name"]
    average_salary = total_salary / count
    return {
        "department": target_dept,
        "average_salary": round(average_salary, 2),
        "top_earner": top_earner,
        "count": count
    }
print(get_department_stats(employees, "IT"))
print(get_department_stats(employees, "Marketing"))