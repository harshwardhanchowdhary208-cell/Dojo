# Gym Equipment Tracker
name1 = input().strip()
users1 = int(input())
name2 = input().strip()
users2 = int(input())
name3 = input().strip()
users3 = int(input())
di = {name1: users1, name2: users2, name3: users3}

print(f"{name1} : {di[name1]} users")
print(f"{name2} : {di[name2]} users")
print(f"{name3} : {di[name3]} users")
name4 = input().strip()
users4 = int(input().strip())
if name4 in di:
    di[name4] += users4
print(f"Updated {name4} : {di[name4]} users")
name5 = input().strip()
users5 = int(input())
di[name5]=users5
print(f"Added {name5} : {di[name5]} users")
name6 = input().strip()
if name6 in di:
    print(f"Removed {name6} with {di[name6]} users")
    del di[name6]
name7 = input().strip()
if name7 in di:
    print(f"Usage of {name7}: {di[name7]} users")
total_users = sum(di.values())
if di:
    busiest_name, busiest_users = max(di.items(), key=lambda item: item[1])
else:
    busiest_name, busiest_users = "No equipment", 0
print(f"Total users: {total_users}")
print(f"Busiest equipment: {busiest_name} ({busiest_users})")