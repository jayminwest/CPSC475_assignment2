"""
Jaymin West
CPSC475
Assignment 2
9/15/2022

This program follows the guidlines in assignment 2 for accepting user
     input to open and search a file for a specific substring. These
     techniques are taken from ex6.py and ex7.py from the class repository
"""

from operator import pos
import sys

def open_user_file():
    """
    This function is used for accepting user input to open a file
    """
    while(True):
        filename = input("Enter file name: ")
        # Trying to open file:
        try:
            filename = open(filename, 'r')
            break
        except:
            print("File doesn't exist! Try again")
    return filename

def read_file(infile):
    """
    Function used for reading the file that is given

    args:
        infile: the file that is going to be read
    
    returns:
        string: file text as a string
    """
    
    string = infile.read()
    infile.close()
    return string

def search_sub_str(full_str, sub_str):
    """
    Function used for searching for a substring in a string

    args:
        string: the string to be searched
        sub_str: the substring to be searched for

    returns:
        the number of times the substring appears in the string
    """
    pos_in_str = 0
    count = 0
    
    while pos_in_str < len(full_str):
        pos_in_sub_str = 0
        while full_str[pos_in_str] == sub_str[pos_in_sub_str]:
            if pos_in_sub_str == len(sub_str) - 1:
                count+=1
                break
            else:
                pos_in_str+=1
                pos_in_sub_str+=1

        pos_in_str+=1
        
    return count

def main():
    str = read_file(open_user_file())
    sub_string = input("Enter substring to search for: ")
    print(search_sub_str(str, sub_string))




if __name__ == "__main__":
    main()