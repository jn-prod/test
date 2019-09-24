# 1. A simple string quoting system is to replace each ' in a string by \' and each \ in a string by \\. 
# Write a function that takes a string, quotes it in this way, and returns the result.
def clean_string(string):
    string_to_list = list(string)
    cleaned_string = ""
    for char in string_to_list:
        # replace each \ in a string by \\
        if char == "\\":
            cleaned_string += "\\\\"
        # replace each ' in a string by \'
        elif char == "'":
            cleaned_string += "\\'"
        else:
            cleaned_string += char
    return cleaned_string

string_to_clean = "1. A simple string quoting system is to replace each ' in a string by \' and each \ in a string by \\. "

final_string = clean_string(string_to_clean)

print("Cleaned String: " + final_string)

# 2. Write a function that takes two strings as arguments, and returns true if they are anagrams of each other, and false otherwise.

def string_to_dic_of_letters(string):
    dic_of_letters = {}
    for letter in list(string):
        dic_of_letters[letter] = dic_of_letters.get(letter, 0) + 1
    return dic_of_letters

def are_anagrams(string_1, string_2):
    # have the same length
    same_length = len(string_1) == len(string_2)
    if same_length:
        # each letter exist in the other
        letter_of_string_1 = string_to_dic_of_letters(string_1)
        letter_of_string_2 = string_to_dic_of_letters(string_2)
        # both words have the count per letter
        for i in letter_of_string_1:
            if letter_of_string_1[i] != letter_of_string_2[i]:
                return False
        return True
    else:
        return False

anagrams_result = are_anagrams("mary", "army") # "mary <> army", "marty <> armies"

print("Is anagram ? " + str(anagrams_result))

# 3. A palindrome is a string that is the same forwards and backwards, disregarding non-letters and case. Eg. « A man, a plan, a canal,
# Panama. » is a palindrome. Write a function that takes a string as input, and returns wether it's a palindrome

def cleaning_string(string):
    cleaned_string = string.lower()
    punctuations = [' ','!','"','#','$','%','&','\'', "'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']
    for i in punctuations:
        cleaned_string = cleaned_string.replace(i,"")
    return cleaned_string   

def is_a_palindrome(string):
    # clean space and ponctuation from string
    cleaned_string = cleaning_string(string)
    cleaned_string_list = list(cleaned_string)
    # create reverse string
    reverse_string = ""
    reverse_string_list = cleaned_string_list[::-1]
    for letter in reverse_string_list:
        reverse_string += letter
    # test if reverse sentence is the sameas the initial sentence
    if cleaned_string == reverse_string:
        return True
    else:
        return False

palindrome_result = is_a_palindrome("A man, a plan, a canal, Panama.")

print(palindrome_result)
