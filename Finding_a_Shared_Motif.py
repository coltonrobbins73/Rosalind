import pandas as pd
import re
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Function: {func.__name__}") 
        print(f"Start time: {start_time}")
        result = func(*args, **kwargs)
        
        end_time = time.time()
        print(f"End time: {end_time}")
        print(f"Time taken: {end_time - start_time} seconds")
        
        return result
    
    return wrapper

@measure_time
def build_suffix_array(s):
    """Builds a suffix array for the given string."""
    return sorted(range(len(s)), key=lambda k: s[k:])

@measure_time
def process_deliminators(s, suffix_array):
    """Finds the unique delimiters in the given suffix array."""
    delim_array = []
    for suffix in suffix_array:
        match = re.search(r'\d{4}', s[suffix:])
        if match:
            delim = match.group(0)
            delim_array.append(delim)
            
    return delim_array

@measure_time
def find_valid_windows(delim_list):
    """Finds the valid windows for the given suffix array that include all elements from delim_list exactly once."""
    valid_windows = []
    i = 0
    while i <= len(delim_list) - 100:
        valid_window_check = set()
        for j in range(100):
            if delim_list[i + j] in valid_window_check:
                i += j  # Adjust starting point for next search to not re-check unnecessary elements
                break
            valid_window_check.add(delim_list[i + j])
        else:  # This else clause executes if the loop completes normally without a break
            if len(valid_window_check) == 100:
                valid_windows.append((i, i + 100))
                i += 100
                continue
        i += 1  # Ensures that we move forward if the window is not valid
        
    return valid_windows

@measure_time
def unused_function(s, suffix_array, unique_delim_list):
    """Finds the valid windows for the given suffix array that include all elements from unique_delim_list exactly once."""
    valid_windows = []
    len_s = len(s)
    for i in range(len(suffix_array)):
        for j in range(i + 1, len(suffix_array) + 1):
            # Extract the substring from s covered by the current window in the suffix array
            substr = ''.join(s[suffix_array[k]:suffix_array[k] + len_s] for k in range(i, j))
            # Check if all unique delimiters are in the substring
            if all(delim in substr for delim in unique_delim_list):
                valid_windows.append((i, j))
                break  # Stop expanding this window once all delimiters are found
    return valid_windows

@measure_time
def check_valid_window(current_index, valid_windows):
    """Checks if the current index is part of a valid window."""
    valid_window_len = len(valid_windows[0])
    current_window_range = list(range(current_index, current_index + valid_window_len))
    if current_window_range in valid_windows:
        return True
    else:
        return False
    
@measure_time
def longest_common_substring(strings):
    """Finds the longest common substring among a list of strings."""
    if not strings:
        return ""

    min_len = min(len(s) for s in strings)
    longest_substring = ""
    
    for i in range(min_len):
        prefix = strings[0][:i+1]
        if all(s.startswith(prefix) for s in strings):
            longest_substring = prefix
        else:
            break
    
    return longest_substring, len(longest_substring)

@measure_time
def compare_prefix(s, suffix_array, current_window_range):
    """Compares the prefix of the suffix array for the given window range."""
    subset_array = [s[suffix_array[i]:] for i in current_window_range]
    min_len = min(len(string) for string in subset_array)
    longest_substring = ""
    
    for i in range(min_len):
        prefix = subset_array[0][:i+1]
        if all(s.startswith(prefix) for s in subset_array):
            longest_substring = prefix
        else:
            break
    
    return longest_substring, len(longest_substring)

@measure_time
def build_lcp_array(s, suffix_array, valid_windows):
    """Builds the LCP array for the given suffix array only making comparisons for valid window indices."""
    valid_window_len = len(valid_windows[0])
    lcp = [0] * (len(suffix_array) - 1)
    lcp_string_array = [0] * (len(suffix_array) - 1)
    current_index = 0
    while current_index < len(suffix_array) - 1:
        current_window_range = list(range(current_index, current_index + valid_window_len))
        if current_window_range not in valid_windows:
            # Skip to the next valid window by adjusting current_index directly
            current_index += valid_window_len
        else:
            longest_common_substring, match_number = compare_prefix(s, suffix_array, current_window_range)
            for window_index in current_window_range:
                if window_index < len(lcp):  # Ensure we do not go out of bounds
                    lcp[window_index] = match_number
                    lcp_string_array[window_index] = longest_common_substring
            # Skip to the next window after processing the current one
            current_index += valid_window_len

    return lcp, lcp_string_array


with open(r'c:\Users\colto\Downloads\rosalind_lcsm.txt') as f:
    txt = f.read()

# s = txt.replace('\n','')

s = re.sub(r'\n|>Rosalind_', '', txt)

suffix_array = build_suffix_array(s)

deliminator_list = process_deliminators(s, suffix_array)

valid_windows = find_valid_windows(deliminator_list)

lcp_array, lcp_string_array = build_lcp_array(s, suffix_array, valid_windows)

max_value = max(lcp_array)
max_indices = [i for i, value in enumerate(lcp_array) if value == max_value]

print(lcp_string_array[max_indices[0]])


def find_unique_window(arr, window_size=100):
    if len(arr) < window_size:
        return None  # Return None if the list is shorter than the window size

    # Initialize the sliding window pointers and a dictionary to count occurrences
    start = 0
    end = 0
    unique_values = {}

    # Iterate through the list to find the window
    while end < len(arr):
        # If the element is not in unique_values or it's not within the current window, add/update it
        if arr[end] not in unique_values or unique_values[arr[end]] < start:
            unique_values[arr[end]] = end

            # Check if the current window size is what we're looking for
            if end - start + 1 == window_size:
                return start, end  # Return the start and end indices of the window

            end += 1
        else:
            # If the element is already in the window, move the start forward
            start = unique_values[arr[end]] + 1
            unique_values[arr[end]] = end  # Update the position of the repeating element
            end += 1

    return None  # Return None if no such window exists

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, ...]  # Your list here
result = find_unique_window(arr)
if result:
    start, end = result
    print(f"Found a unique window from index {start} to {end}.")
else:
    print("No unique window of size 100 found.")
