n = int(input())

if n <= 0:
    print("No scores")
else:
    scores = []
    for _ in range(n):
        scores.append(int(input()))

    # Pass 1: count, sum, min, max
    total_sum = 0
    count = 0
    minimum = scores[0]
    maximum = scores[0]

    for score in scores:
        total_sum += score
        count += 1
        if score < minimum:
            minimum = score
        if score > maximum:
            maximum = score

    average = total_sum / count

    # Pass 2: strictly above average
    above_avg = 0
    for score in scores:
        if score > average:
            above_avg += 1

    print(f"Count: {count}")
    print(f"Sum: {total_sum}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Average: {average:.2f}")
    print(f"Above average: {above_avg}")