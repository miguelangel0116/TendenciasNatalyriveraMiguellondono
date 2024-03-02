def userSearch(Hospital,userName):
    for person in Hospital.persons:
        if person.userName==userName:
            return person
        return None
