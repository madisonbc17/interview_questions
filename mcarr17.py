current_assignments = ["source_code_control","Teamwork: personality styles"]
finished_assignments = []

print("*****Assignments left to do in this semester*****")
for busy_work in current_assignments:
    current_assignments.remove(busy_work)
    finished_assignments.append(busy_work)

print("Needing completion:")
print(current_assignments)
print("Finished assignments:")
print(finished_assignments)
 
assignments_left = len(current_assignments)
print(str(assignments_left) + " assignments left in the semester")
