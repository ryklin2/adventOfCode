import csv
import numpy

def sum_repeated_twice_in_range(start, end):
    """Sum all numbers in range that have a pattern repeated twice"""
    total = 0
    
    length = 2
    while True:
        half_len = length // 2
        
        min_pattern = 10 ** (half_len - 1)
        max_pattern = 10 ** half_len - 1
        
        min_repeated = int(str(min_pattern) + str(min_pattern))
        max_repeated = int(str(max_pattern) + str(max_pattern))
        
        if min_repeated > end:
            break
        
        actual_start = max(min_repeated, start)
        actual_end = min(max_repeated, end)
        
        if actual_start <= actual_end:
            start_pattern = int(str(actual_start)[:half_len])
            end_pattern = int(str(actual_end)[:half_len])
            
            # Sum each repeated number in this range
            for pattern in range(start_pattern, end_pattern + 1):
                repeated_num = int(str(pattern) + str(pattern))
                if start <= repeated_num <= end:
                    total += repeated_num
        
        length += 2
    
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
                    
                    invalid_sum = sum_repeated_twice_in_range(start, end)
                    total_sum += invalid_sum
    print(f"{total_sum}")
    return total_sum
    
    
if __name__ == "__main__":
    result = giftshop('input.csv')