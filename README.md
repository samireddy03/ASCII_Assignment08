# PrimeSubstringSolver

## Assignment Description

> Given the string:  
> "Yet such is oft the course of deeds that move the wheels of the world: small hands do them because they must, while the eyes of the great are elsewhere.",  
> what is the **longest substring that sums to a prime number**, using the ASCII value for each character?  
> **If two or more substrings are the same length, provide the substring earliest in the alphabet.**

---

## How It Works

This Python project solves the problem by:

- Iterating through all **contiguous substrings** of the input text.
- Calculating the **sum of ASCII values** for each substring.
- Checking whether that sum is a **prime number**.
- Tracking the **longest** valid substring found.
- If two substrings share the same max length, selecting the one **earliest in the alphabet**.

---

## Professor’s Contribution Instructions

You are kindly requested to implement the following function in `utilsPackage/utils.py`:

```python
def is_prime(n):
    # Return True if n is a prime number, otherwise False
    pass

---

## File Structure
PrimeSubstringSolver/ 
├── mainPackage/
│ └── main.py # Runs the program 
├── finderPackage/ 
│ └── finder.py # Contains PrimeSubstringFinder class 
├── utils/ 
│ └── utils.py # is_prime function (to be implemented) 
├── README.md # Assignment and documentation
