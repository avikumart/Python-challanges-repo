def string_sorter(text):
    count_string = {"Upper_case":0,
                    "Lower_case":0
                    }
    upper_letter = []
    lower_letter = []
    
    for letter in text:
        if letter.isupper():
            count_string['Upper_case'] += 1
            upper_letter.append(letter)
        elif letter.islower():
            count_string['Lower_case'] += 1
            lower_letter.append(letter)
        else:
            pass
    print("Statement was:", text)
    print("Count of upper and lower case", count_string)
    print("Lists of upper and lower letters: ", upper_letter, lower_letter)
    
string_sorter("Welcome to the World of Possibilities!")