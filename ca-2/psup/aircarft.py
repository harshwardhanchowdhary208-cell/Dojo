aircraft1 = input().strip()
aircraft2 = input().strip()
aircraft3 = input().strip()
aircraft4 = input().strip()
aircraft5 = input().strip()

arr = [aircraft1, aircraft2, aircraft3, aircraft4, aircraft5]

print(f"Initial queue: {', '.join(arr)}")

arrival = input().strip()

arr.append(arrival)

print(f"After adding {arrival}: {', '.join(arr)}")

remove_name = input().strip()

if remove_name in arr:
    arr.remove(remove_name)

print(f"After removing {remove_name}: {', '.join(arr)}")

count_name = input().strip()

count = arr.count(count_name)

print(f"Occurrences of {count_name}: {count}")

print(f"First: {arr[0]}, Last: {arr[-1]}")

print(f"Total aircraft: {len(arr)}")
