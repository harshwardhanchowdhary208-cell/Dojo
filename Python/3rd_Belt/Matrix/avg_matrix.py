# Question: What problem does this code solve?
# Add your solution here.

m,n,matrix = input() #This line is wrong but written to avoid erroe the correct code for m,n and matrix whould be given in dojo itself 
# Calculate the total sum of all elements in the matrix
total_sum = sum(sum(row) for row in matrix)

# Calculate the total number of elements
total_elements = m * n

# Compute the average
average = total_sum / total_elements

# Print the result rounded to one decimal place
print(f"{average:.1f}")
