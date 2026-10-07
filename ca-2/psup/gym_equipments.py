# Gym Equipment Tracker
# Uses a dictionary as the only data type and avoids loops.

equipment = {}

# Read 3 pieces of equipment directly into the dictionary
name1 = input().strip()
users1 = int(input().strip())
equipment[name1] = users1
print(f"{name1}: {users1} users")

name2 = input().strip()
users2 = int(input().strip())
equipment[name2] = users2
print(f"{name2}: {users2} users")

name3 = input().strip()
users3 = int(input().strip())
equipment[name3] = users3
print(f"{name3}: {users3} users")

# Booking update using dictionary-safe increment
booking_name = input().strip()
amount = int(input().strip())
equipment[booking_name] = equipment.get(booking_name, 0) + amount
print(f"Updated {booking_name}: {equipment[booking_name]} users")

# Add new equipment to the dictionary
new_name = input().strip()
new_users = int(input().strip())
equipment[new_name] = new_users
print(f"Added {new_name}: {new_users} users")

# Remove equipment from the dictionary safely
removed_name = input().strip()
removed_users = equipment.pop(removed_name, 0)
print(f"Removed {removed_name} with {removed_users} users")

# Query equipment usage without raising KeyError
query_name = input().strip()
usage_value = equipment.get(query_name, 0)
print(f"Usage of {query_name}: {usage_value} users")

# Calculate total users without a loop
total_users = sum(equipment.values())

# Find busiest equipment without a loop
if equipment:
    busiest_name, busiest_users = max(equipment.items(), key=lambda item: item[1])
else:
    busiest_name, busiest_users = "No equipment", 0

print(f"Total users: {total_users}")
print(f"Busiest equipment: {busiest_name} ({busiest_users})")
