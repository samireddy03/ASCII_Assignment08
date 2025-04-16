
# File Name : {required}
# Student Name: {required}
# email:  {required}
# Assignment Number: Assignment nn  {required}
# Due Date:   {required}
# Course #/Section:   {required}
# Semester/Year:   {required}
# Brief Description of the assignment:  {required}

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

# Anything else that's relevant:




from utilsPackage.utils import is_prime

class PrimeSubstringFinder:
    """
    Class to find the longest substring where the sum of ASCII values is a prime number.
    """
    
    def __init__(self, text):
        """
        Initialize the PrimeSubstringFinder with the input text.
        
        Args:
            text (str): The text to search for substrings.
        """
        self.text = text
    
    def find_longest_prime_substring(self):
        """
        Find the longest substring where the sum of ASCII values is a prime number.
        If multiple substrings with the same length exist, return the one that comes first alphabetically.
        
        Returns:
            str: The longest substring with a prime ASCII sum
        """
        longest = ""
        max_len = 0
        
        for i in range(len(self.text)):
            for j in range(i + 1, len(self.text) + 1):
                sub = self.text[i:j]
                ascii_sum = sum(ord(c) for c in sub)
                
                if is_prime(ascii_sum):
                    if len(sub) > max_len:
                        longest = sub
                        max_len = len(sub)
                    elif len(sub) == max_len and sub < longest:
                        longest = sub
                        
        return longest