import sys
from enum import Enum


class ThreeLetterDigits(Enum):
    one = 1
    two = 2
    six = 6


class FourLetterDigits(Enum):
    four = 4
    five = 5
    nine = 9


class FiveLetterDigits(Enum):
    three = 3
    seven = 7
    eight = 8

three_letter_names = [x.name for x in ThreeLetterDigits]
four_letter_names = [x.name for x in FourLetterDigits]
five_letter_names = [x.name for x in FiveLetterDigits]


def parse_if_string_number(input_str: str, pos_idx: int) -> str: 
    if pos_idx <= 1:
        return 0

    get_last_three = input_str[pos_idx - 2:pos_idx+1]
    if get_last_three in three_letter_names: 
        return str(ThreeLetterDigits[get_last_three].value)
    
    if pos_idx <= 2:
        return 0

    get_last_four = input_str[pos_idx - 3:pos_idx+1]
    if get_last_four in four_letter_names: 
        return str(FourLetterDigits[get_last_four].value)

    if pos_idx <= 3:
        return 0

    get_last_five = input_str[pos_idx - 4:pos_idx+1]
    if get_last_five in five_letter_names: 
        return str(FiveLetterDigits[get_last_five].value)
    
    return 0


if __name__ == "__main__":
    rolling_sum = 0

    for line in sys.stdin:
        clean_line = line.strip()
        start_idx = 0
        start_digit, end_digit = "", ""

        for idx in range(len(clean_line)):
            if clean_line[idx].isnumeric():
                start_digit = clean_line[idx]
                start_idx = idx+1
                break

            parse_stringified_num = parse_if_string_number(clean_line, idx)
            if parse_stringified_num != 0:
                start_digit = parse_stringified_num
                start_idx = idx+1
                break
        
        for idx in range(len(clean_line)-1,start_idx-1,-1):
            if clean_line[idx].isnumeric():
                end_digit = clean_line[idx]
                break
                
            parse_stringified_num_to_three = parse_if_string_number(clean_line, idx + 2)
            if parse_stringified_num_to_three != 0:
                end_digit = parse_stringified_num_to_three
                break

            parse_stringified_num_to_four = parse_if_string_number(clean_line, idx + 3)
            if parse_stringified_num_to_four != 0:
                end_digit = parse_stringified_num_to_four
                break
            
            parse_stringified_num_to_five = parse_if_string_number(clean_line, idx + 4)
            if parse_stringified_num_to_five != 0:
                end_digit = parse_stringified_num_to_five
                break
        
        if end_digit == "":
            end_digit = start_digit
        rolling_sum += int(start_digit + end_digit)
        
    print(rolling_sum)


        

                    

                



            







