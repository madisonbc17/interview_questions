current_assignments = ["source_code_control","Teamwork: personality styles"]
finished_assignments = []

for busy_work in current_assignments:
    current_assignments.remove(busy_work)
    finished_assignments.append(busy_work)

print("Needing completion:")
print(current_assignments)
print("Finished assignments:")
print(finished_assignments)
