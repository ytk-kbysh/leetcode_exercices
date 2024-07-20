
#The following function makes a user to input
#It chcecks if an input contains only alphabets
#Need for improvement: It cannot chceck if an input contains only the letters N, I, V, X, L, C, D, M (or not.The line 253 "  if temp_roman_numerials == "":" checks if there is unprocessed characters are there)

def input_check():
    user_input = ""
    i = 0
    while i < 3:
        i += 1
        try:
            user_input = input("Please enter a Roman numerial of your choice up to 4,999: ")
            if user_input.isalpha(): #user input, checked if it contains only alphabets
                return user_input
        except Exception as e:
            print(f"{e}, Please try again, you can try {3 - i} time(-s) more.")


#The following should be able to detect 1 to 4 thousands and output as 1st return value, output the 3 (or less) digit-number as 2nd return value

def thousands_detect(number):
    number_without_thousands = 0
    if "MMMM" == number[:4]:
        number_without_thousands = number[4:]
        return [4000, number_without_thousands]
    elif "MMM" == number[:3]:
        number_without_thousands = number[3:]
        return [3000, number_without_thousands]
    elif "MM" == number[:2]:
        number_without_thousands = number[2:]
        return [2000, number_without_thousands]
    elif "M" == number[:1]:
        number_without_thousands = number[1:]
        return [1000, number_without_thousands]
    else:
        number_without_thousands = number
        return [0, number_without_thousands]

# Test thousands are properly detected and the number under hundreds are output.    
# print(thousands_detect("MMMM"))
# print(thousands_detect("MMMMV"))
# print(thousands_detect("MMMI"))
# print(thousands_detect("MMV"))
# print(thousands_detect("MV"))
# print(thousands_detect("M"))
# print(thousands_detect("CMI"))


#The following should be able to detect 1 to 9 hundreds and output as 1st return value, output the 2 (or less) digit-number as 2nd return value
#It can only hundle 3 digit number or less / thousands_detect() should be used in advance.

def hundreds_detect(number):
    number_without_hundreds = 0
    if "CM" == number[:2]:
        number_without_hundreds = number[2:]
        return 900, number_without_hundreds
    elif "DCCC" == number[:2]:
        number_without_hundreds = number[4:]
        return 800, number_without_hundreds
    elif "DCC" == number[:2]:
        number_without_hundreds = number[3:]
        return 700, number_without_hundreds
    elif "DC" == number[:2]:
        number_without_hundreds = number[2:]
        return 600, number_without_hundreds
    elif "D" == number[:2]:
        number_without_hundreds = number[1:]
        return 500, number_without_hundreds
    elif "CD" == number[:2]:
        number_without_hundreds = number[2:]
        return 400, number_without_hundreds
    elif "CCC" == number[:2]:
        number_without_hundreds = number[3:]
        return 300, number_without_hundreds
    elif "CC" == number[:2]:
        number_without_hundreds = number[2:]
        return 200, number_without_hundreds
    elif "C" == number[:1]:
        number_without_hundreds = number[1:]
        return 100, number_without_hundreds  
    else:
        number_without_hundreds = number
        return 0, number_without_hundreds  

# Test hundreds are properly detected (thousands will not be detected)
# print(hundreds_detect("MMMM"))
# print(hundreds_detect("MMMMV"))
# print(hundreds_detect("MMMI"))
# print(hundreds_detect("MMV"))
# print(hundreds_detect("MV"))
# print(hundreds_detect("M"))
# print(hundreds_detect("CMI"))
# print(hundreds_detect("CCCI"))
# print(hundreds_detect("DC"))
# print(hundreds_detect("CD"))
# print(hundreds_detect("CIV"))

#The following should be able to detect 1 to 9 tens and output as 1st return value, output the 1 digit-number as 2nd return value
#It can only hundle 2 digit number or less / thousands_detect() and hundreds_detect() should be used in advance.

def tens_detect(number):
    umber_without_tens = 0
    if "XC" == number[:2]:
        number_without_tens = number[2:]
        return 90, number_without_tens
    elif "LXXX" == number[:4]:
        number_without_tens = number[4:]
        return 80, number_without_tens
    elif "LXX" == number[:3]:
        number_without_tens = number[3:]
        return 70, number_without_tens
    elif "LX" == number[:2]:
        number_without_tens = number[2:]
        return 60, number_without_tens
    elif "L" == number[:1]:
        number_without_tens = number[1:]
        return 50, number_without_tens
    elif "XL" == number[:2]:
        number_without_tens = number[2:]
        return 40, number_without_tens
    elif "XXX" == number[:3]:
        number_without_tens = number[3:]
        return 30, number_without_tens
    elif "XX" == number[:2]:
        number_without_tens = number[2:]
        return 20, number_without_tens
    elif "X" == number[:1]:
        number_without_tens = number[1:]
        return 10, number_without_tens
    else:
        number_without_tens = number
        return 0, number_without_tens

# Test tens are properly detected     
# print(tens_detect("MMMM"))
# print(tens_detect("MMMMV"))
# print(tens_detect("MMMI"))
# print(tens_detect("MMV"))
# print(tens_detect("MV"))
# print(tens_detect("M"))
# print(tens_detect("CMI"))
# print(tens_detect("CCCI"))
# print(tens_detect("DC"))
# print(tens_detect("CD"))
# print(tens_detect("CIV"))
# print(tens_detect("CCCI"))
# print(tens_detect("DC"))
# print(tens_detect("CD"))
# print(tens_detect("CIV"))
# print(tens_detect("XI"))
# print(tens_detect("LXV"))
# print(tens_detect("XXXVI"))
# print(tens_detect("LXV"))

def ones_detect(number):
    number_without_ones = 0
    if "IX" == number[:2]:
        number_without_ones = number[2:]
        return 9, number_without_ones
    elif "VIII" == number[:4]:
        number_without_ones = number[4:]
        return 8, number_without_ones
    elif "VII" == number[:3]:
        number_without_ones = number[3:]
        return 7, number_without_ones
    elif "VI" == number[:2]:
        number_without_ones = number[2:]
        return 6, number_without_ones
    elif "V" == number[:1]:
        number_without_ones = number[1:]
        return 5, number_without_ones
    elif "IV" == number[:2]:
        number_without_ones = number[2:]
        return 4, number_without_ones
    elif "III" == number[:3]:
        number_without_ones = number[3:]
        return 3, number_without_ones
    elif "II" == number[:2]:
        number_without_ones = number[2:]
        return 2, number_without_ones
    elif "I" == number[:1]:
        number_without_ones = number[1:]
        return 1, number_without_ones
    elif "N" == number[:1]:
        number_without_ones = number[1:]
        return 0, number_without_ones
    else:
        return ValueError, NameError

# Test ones are properly detected     
# print(ones_detect("MMMM"))
# print(ones_detect("MMMMV"))
# print(ones_detect("MMMI"))
# print(ones_detect("MMV"))
# print(ones_detect("MV"))
# print(ones_detect("M"))
# print(ones_detect("CMI"))
# print(ones_detect("CCCI"))
# print(ones_detect("DC"))
# print(ones_detect("CD"))
# print(ones_detect("CIV"))
# print(ones_detect("CCCI"))
# print(ones_detect("DC"))
# print(ones_detect("CD"))
# print(ones_detect("CIV"))
# print(ones_detect("XI"))
# print(ones_detect("LXV"))
# print(ones_detect("XXXVI"))
# print(ones_detect("LXV"))
# print(ones_detect("VI"))
# print(ones_detect("IX"))
# print(ones_detect("I"))
# print(ones_detect("III"))
# print(ones_detect("N"))

#0, number_without_tens
def main():
    roman_numerials = ""
    temp_roman_numerials = ""
    result = 0
    number_without_thousands = 0
    number_without_hundreds = 0
    number_without_tens = 0

    roman_numerials = input_check()
    print(f"Your input is : {roman_numerials}")

    result = thousands_detect(roman_numerials)[0]
    temp_roman_numerials = thousands_detect(roman_numerials)[1]

    # print(f"The function thousands_detect returns: {thousands_detect(roman_numerials)}")
    # print(f"The temporary result: {result}")
    # print(f"The roman numerial without thousands: {temp_roman_numerials}")

    result += hundreds_detect(temp_roman_numerials)[0]
    temp_roman_numerials = hundreds_detect(temp_roman_numerials)[1]

    # print(f"The temporary result: {result}")
    # print(f"The roman numerial without thousands and hundreds: {temp_roman_numerials}")

    result += tens_detect(temp_roman_numerials)[0]
    temp_roman_numerials = tens_detect(temp_roman_numerials)[1]

    # print(f"The result: {result}")
    # print(f"The roman numerial without thousands, hundreds and tens: {temp_roman_numerials}")

    result += ones_detect(temp_roman_numerials)[0]
    temp_roman_numerials = ones_detect(temp_roman_numerials)[1]

    # print(f"The result: {result}")
    # print(f"The texts not processed is: {temp_roman_numerials}")

    if temp_roman_numerials == "":
        print(f"{roman_numerials} translates into {result}")
    else:
        print(f"{roman_numerials} is not a correctly written Roman numerial.")

    return None


if __name__ == '__main__':
    main()