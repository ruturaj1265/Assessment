# Question .01
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    top, bottom = 0, rows - 1

    while top <= bottom:
        mid_row = (top + bottom) // 2
        if matrix[mid_row][-1] < target:
            top = mid_row + 1
        elif matrix[mid_row][0] > target:
            bottom = mid_row - 1
        else:
            left, right = 0, cols - 1
            while left <= right:
                mid_col = (left + right) // 2
                if matrix[mid_row][mid_col] == target:
                    print(f"Target {target} found at position ({mid_row}, {mid_col}).")
                    return True
                elif matrix[mid_row][mid_col] < target:
                    right = mid_col - 1
                else:
                    left = mid_col + 1
            
            print(f"Target {target} not found in the matrix.")
            return False
    
    print(f"Target {target} not found in the matrix.")
    return False

searchMatrix([[13,5,7],[5,4,6],[9,8,7]], 3)

# Question.02

from collections import Counter

def highest_frequency_word_length(input_string):
    words = input_string.split()
    word_counts = Counter(words)

    max_word = max(word_counts, key=word_counts.get)
    max_word_length = len(max_word)

    return max_word_length

# Test Case 1
input_str_1 = "write all the number from 1 to 100"
output_1 = highest_frequency_word_length(input_str_1)
print(f"Test Case 1: {output_1}")

# Test Case 2
input_str_2 = "apple orange banana banana apple orange orange"
output_2 = highest_frequency_word_length(input_str_2)
print(f"Test Case 2: {output_2}")

# Test Case 3
input_str_3 = "python python python java java java java c++ c++"
output_3 = highest_frequency_word_length(input_str_3)
print(f"Test Case 3: {output_3}")
