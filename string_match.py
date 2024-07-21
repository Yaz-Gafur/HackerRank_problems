def matching_substrings(a, b):
    count = 0
    # Determine the minimum length to avoid index errors
    min_length = min(len(a), len(b))
    
    # Iterate through the strings up to the second to last character
    for i in range(min_length - 1):
        # Check if the substrings of length 2 match
        if a[i:i + 2] == b[i:i + 2]:
            count += 1
            
    return count

# Example usage
a = "xxcaazz"
b = "xxbaaz"
print(matching_substrings(a, b))  # Output will be 3
