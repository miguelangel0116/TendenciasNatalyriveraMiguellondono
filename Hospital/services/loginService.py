def userSearch(Hospital,username):
    for employee in Hospital.employees:
        if employee.username==username:
            return employee
        return None
