
# File Name : main.py
# Student/Professor Name: Saivamsi Amireddy, Bill Nicholson
# email:  amiredsr@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  4/17/2025
# Course #/Section:  IS4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment:  {required}

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

# Anything else that's relevant:


from finderPackage.finder import PrimeSubstringFinder

if __name__ == "__main__":
    text = (
        "Yet such is oft the course of deeds that move the wheels of the world: small hands do them because they must, while the eyes of the great are elsewhere."
    )

    finder = PrimeSubstringFinder(text)
    result = finder.find_longest_prime_substring()
    print("Longest prime-sum substring:", result)