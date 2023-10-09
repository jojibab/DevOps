'''
Phone Numeres  from the text 
'''

def getPhoneNumber(s):
    words_to_digits_map = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    s = s.split()
    o = []

    i = 0
    while i < len(s):
        if s[i] == 'double':
            digit = words_to_digits_map[s[i+1]]
            o.append(digit * 2)
            i += 2
        elif s[i] == 'triple':
            digit = words_to_digits_map[s[i+1]]
            o.append(digit * 3)
            i += 2 
        elif s[i] in words_to_digits_map:
            if i + 1 < len(s):
                digit = words_to_digits_map[s[i]]
                o.append(digit)
                i += 1
            elif i + 1 < len(s):
                digit = words_to_digits_map[s[i]]
                o.append(digit)
                i += 1
            else:
                o.append(words_to_digits_map[s[i]])
                i += 1
        else:
            i += 1
            
    return ''.join(o)

    
# Example 1
input_str1 = "Two one nine six eight one six four six"
output1 = words_to_digits(input_str1)
print(f"Input: {input_str1}\nOutput: {output1}")

# Example 2
input_str2 = "five one zero two four eight zero double three tw"
output2 = words_to_digits(input_str2)
print(f"Input: {input_str2}\nOutput: {output2}")

# Example 3
input_str3 = "tripple eight five eight six one zero four three"
output3 = words_to_digits(input_str3)
print(f"Input: {input_str3}\nOutput: {output3}")