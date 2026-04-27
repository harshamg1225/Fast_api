from fastapi import FastAPI, HTTPException
from model import Employee
from typing import List


employee_db: List[Employee] = []


app = FastAPI()

# 1. Read all employeees


@app.get("/employees", response_model=List[Employee])
def get_employees():

    return employee_db


# 2. Read specific employee
@app.get("/employees/{emp_id}", response_model=Employee)
def get_specific_employee(emp_id: int):

    for index, employee in enumerate(employee_db):
        if employee.id == emp_id:
            return employee_db[index]

    raise HTTPException(status_code=404, detail="Employee not found")


# 3 Add an employee
@app.post("/employees")
def add_employee(new_emp: Employee):

    for employee in employee_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee already exists")

    employee_db.append(new_emp)


# 4. Update an employee
@app.put("/update_employee/{emp_id}", response_model=Employee)
def update_employee(emp_id: int, updated_employee: Employee):

    for index, employee in enumerate(employee_db):
        if employee.id == emp_id:
            employee_db[index] = updated_employee

            return updated_employee

    raise HTTPException(status_code=404, detail="Employee not found")


# 5 delete employee
@app.delete("/delete_employee/{emp_id}")
def delete_employee(emp_id: int):

    for index, employee in enumerate(employee_db):
        if employee.id == emp_id:
            del employee_db[index]

            return {"Message": "Employee deleted succefully"}

    raise HTTPException(status_code=404, detail="Employee not found")
