from paramiko import SSHClient, AutoAddPolicy
import re
from time import sleep
import logging

import levels


BASE_USERNAME = "bandit"
BANNER_TIMEOUT = 400


#logging.basicConfig(level=logging.DEBUG)


def showWelcomeMessage() -> None:
    '''
    This function shows the intial welcome message
    '''
    
    print( """ \nWelcome to Bandit Autorun!
          \nThis is a tool to get the current level password of particular level. Please, use it consciously 
          \nDeveloped by ... 
          """)

    

def verifyArgs(args: list) -> bool:

    def showUsage() -> None:

        print("Usage: python <name> <level>")

    def verifyLevel() -> bool:
        """
        This function checks if the user has provided a int level properly
        """


        if(len(args) == 2 and str(args[1]).isdecimal() and int(str(args[1])) < 33):
            level = str(args[1])

            if(level == "26"):
                print("You can get the bandit26 password but it is a nonsence because the session will be close unless you do the level correctly. Please, if you got stuck here, select the 25 or the 27 level")
                return False

            print("-> You have selected the level " + level)
            return True

        showUsage()

        return False
    
    return verifyLevel()








def establishSSHConnection(hostname: str, port: int, password: str, level: int):
    '''

    '''
    username = BASE_USERNAME + str(level)

    client = SSHClient()

    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(hostname=hostname, port=port, username=username, password=password, banner_timeout=BANNER_TIMEOUT, look_for_keys=False, allow_agent=False)
    #Sin el look_for_keys=False, allow_agent=False no va el 14 que es hacer un ssh -i private.key porque pide el yes este 

    method_name = f'solveLevel{level}'

    if hasattr(levels, method_name):
        method = getattr(levels, method_name)
        new_password = method(client,password)
        
        print("-> Getting the password " + str(level+1)  + ": DONE " + str(new_password) ) 
        return new_password

    


def run(args: list, hostname: str, port: int, initial_username: str, initial_password: str):
    
    showWelcomeMessage()


    #establishSSHConnection(hostname=hostname, port=port, password="Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN", level=28)


    
    if(verifyArgs(args=args)):

        selected_used_level = int(args[1])

        password = initial_password

        for i in range(selected_used_level):
            
            if(i==26):
                continue

            password = establishSSHConnection(hostname=hostname, port=port, password=password, level=i)
            sleep(0.001)



        print("\nThe password for the level " + str(selected_used_level) + " is " + str(password) + "\n")
        
    
    





    
























"""
Due to OverTheWire changes every level password from time to time, we decided to create a tool which helps you to start again from the level you have left.
For example, if you got stuck in level 20 and passwords have changed, you only need to use this script to get the current password of the level 20 and go on. 
Only type: python ... 
"""
