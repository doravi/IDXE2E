import paramiko
import time


def readFileFromSFTP(fileName):

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
                ssh.connect('idx-etl', 22, username='idx', password='idx')
        except paramiko.SSHException:
                print "Connection Failed"
                quit()
        
        stdin,stdout,stderr = ssh.exec_command("ls /etc/")

        sftp = ssh.open_sftp()
        path = "/usr/idx/dor/"
        for x in xrange(0,30):

                try:
                        my_file = sftp.open(path + fileName, 'r')
                        my_file = my_file.read()
                        f = open('Remote'+fileName, 'w')
                        f.write(my_file)
                        f.close()
                        break
                except Exception as e:
                        print (str(e))
                        time.sleep(1)

        sftp.close()
        ssh.close()



