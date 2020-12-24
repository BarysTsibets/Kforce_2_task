"""Given two strings pattern and s. The first string pattern contains only the symbols 0 and 1,
 and the second string s contains only lowercase English letters.
Let's say that pattern matches a substring s[l..r] of s if the following 3 conditions are met:
they have equal length; for each 0 in pattern the corresponding letter in the substring is a vowel;
 for each 1 in pattern the corresponding letter is a consonant.
  the task is to calculate the number of substrings of s that match pattern.
  Note: In this we define the vowels as a,e,i,o,u, and y. All other letters are consonants.
I am not challenging anyone here, I have tried different ways but could not achieve.
This question was asked in codesignal test assessment recently."""


def binaryPatternMatching(pattern, s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    string_pattern = str(pattern)
    list_int_pattern = [int(i) for i in string_pattern]
    list_s = list(s)
    print(f"Pattern list - {list_int_pattern}")
    # print(f"list_s in letters format - {list_s}")

    """Refactoring letters in list_s from vowels/constants format to binary 0/1 format"""
    zero_one_list = []
    for letter in list_s:
        if letter in vowels:
            zero_one_list.append(0)
        else:
            zero_one_list.append(1)
    print(f"Binary formated list_s to zero_one_list - {zero_one_list}")
    counter = 0

    for n in range(0, len(zero_one_list)):
        if zero_one_list[n:(n+len(list_int_pattern))] == list_int_pattern and len(list_int_pattern) > 0:
            counter += 1
        n += 1
    print(counter)
    return counter


binaryPatternMatching("010", 'amazing')
binaryPatternMatching('101', 'helloworld')

