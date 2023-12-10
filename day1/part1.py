import sys

if __name__ == "__main__":
    rolling_sum = 0
    for line in sys.stdin:
        clean_line = line.strip()
        
        start_idx, end_idx = 0, len(clean_line)
        start_digit, end_digit = "", ""

        for idx in range(end_idx):
            if clean_line[idx].isnumeric():
                start_idx = idx
                start_digit = clean_line[idx]
                break
        

        for idx in range(end_idx - 1, idx - 1, -1):
            if clean_line[idx].isnumeric():
                end_digit = clean_line[idx]
                break
        rolling_sum += int(start_digit + end_digit)
    print(rolling_sum)






        

