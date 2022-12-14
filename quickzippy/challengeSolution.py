#!/usr/bin/python3
#Write a simple script that can be run against a file and returns if that file is a zip file or not (True or False is fine).
# The solution to this problem can be found in the zipfile library, https://docs.python.org/3/library/zipfile.html

"""RZFeeser | Alta3 Research
   solution to code customization 01"""


import zipfile

def main():
    """runtime code"""

    iszip = input("What is the file you would like to examine (full or relative path)? ")

    if zipfile.is_zipfile(iszip):   # returns true if the file is a zip file
        print("Yep! That is a 'zip' file.")
    else:
        print("Nay. That is not a 'zip' file.")

if __name__ == "__main__":
    main()
