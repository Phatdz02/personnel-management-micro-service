from pymongo import MongoClient
from datetime import datetime, timedelta


client = MongoClient('mongodb://localhost:27017/')
db = client['staff_profile_management']


employees = [
    {
        "employee_id": "E001",
        "name": "Nguyen Van A",
        "department": "IT",
        "leave_balance": 12
    },
    {
        "employee_id": "E002",
        "name": "Tran Thi B",
        "department": "HR",
        "leave_balance": 10
    }
]


leave_requests = [
    {
        "employee_id": "E001",
        "leave_type": "Sick Leave",
        "start_date": datetime.now().strftime('%Y-%m-%d'),
        "end_date": (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d'),
        "reason": "Flu",
        "status": "Pending",
        "documents": []
    },
    {
        "employee_id": "E002",
        "leave_type": "Annual Leave",
        "start_date": datetime.now().strftime('%Y-%m-%d'),
        "end_date": (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d'),
        "reason": "Family vacation",
        "status": "Approved",
        "documents": []
    }
]


attendance_records = [
    {
        "employee_id": "E001",
        "date": datetime.now().strftime('%Y-%m-%d'),
        "check_in": "09:00",
        "check_out": "18:00"
    },
    {
        "employee_id": "E002",
        "date": datetime.now().strftime('%Y-%m-%d'),
        "check_in": "08:30",
        "check_out": "17:30"
    }
]


work_from_home_requests = [
    {
        "employee_id": "E001",
        "date": (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'),
        "reason": "Home renovation",
        "status": "Pending"
    }
]


db.employees.insert_many(employees)
db.leave_requests.insert_many(leave_requests)
db.attendance.insert_many(attendance_records)
db.work_from_home_requests.insert_many(work_from_home_requests)

print("Sample data inserted successfully.")
