import os
from subprocess import call
import sys

def click_checkinn():
    call(["python", "applicant.py"])
def click_list():
    call(["python", "list.py"])


class INTERVIEW:
    def __init__(self):
        a=1
        while a!=3:
            print("\n\n================= WELCOME TO IITJ INTERVIEW PORTAL ====================\n")
            print("1. Applicant Report")
            print("2. Applicant Lists")
            print("3. Exit portal\n")
            print("Choose : ")
            a=int(input())
            if a<1 or a>3:
                print("Invalid Input!\n\n")
                INTERVIEW();
    
            if a==2:
                click_list() 

            if a==1:
                click_checkinn()          

    
if __name__ == '__main__':
    GUUEST=INTERVIEW()


