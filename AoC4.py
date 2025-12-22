import csv
import numpy

def sum_repeated_patterns_in_range(start, end):
    """Sum all numbers that are repeating patterns (at least 2 repetitions)"""
    total = 0
    seen = set()  # Avoid counting the same number twice
    
    length = 1
    # Check up to reasonable length
    while 10 ** length <= end:
        # Try different numbers of repetitions (2, 3, 4, ...)
        for num_reps in range(2, 20):  # Adjust max as needed
            pattern_len = length
            total_len = pattern_len * num_reps
            
            min_pattern = 10 ** (pattern_len - 1) if pattern_len > 1 else 1
            max_pattern = 10 ** pattern_len - 1
            
            for pattern in range(min_pattern, max_pattern + 1):
                repeated = int(str(pattern) * num_reps)
                
                if repeated > end:
                    break
                if repeated >= start and repeated not in seen:
                    total += repeated
                    seen.add(repeated)
        
        length += 1
    
    return total

def giftshop(filename):
    print("Starting giftshop function")
    total_sum = 0
    
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for range_str in row:
                if range_str.strip():
                    start, end = range_str.split('-')
                    start = int(start)
                    end = int(end)
                    
                    invalid_sum = sum_repeated_patterns_in_range(start, end)
                    total_sum += invalid_sum
    
    print(f"{total_sum}")
    return total_sum
    
if __name__ == "__main__":
    result = giftshop('input.csv')