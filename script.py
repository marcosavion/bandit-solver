import json
import sys

from utils import showWelcomeMessage, run

HOSTNAME = "bandit.labs.overthewire.org"
PORT = 2220
INITIAL_USERNAME = "bandit0"
INITIAL_PASSWORD = "bandit0"

if __name__ == '__main__':


    run(args=sys.argv, hostname=HOSTNAME, port=PORT, initial_username=INITIAL_USERNAME, initial_password=INITIAL_PASSWORD)
