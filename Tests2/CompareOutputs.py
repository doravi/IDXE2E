#test
import filecmp

def compareOutputs():
    print("Comparing Outputs")
    f = open('GIGYA_TO_SFTP.csv', 'r')
    localFile = f.read()
    f.close()
    f = open('GIGYA_TO_SFTP.csv', 'w')
    f.write(localFile)
    f.close()
    print 'common_file:',
    print filecmp.cmp('GIGYA_TO_SFTP.csv', 'RemoteGIGYA_TO_SFTP.csv')
    f = open('RemoteGIGYA_TO_SFTP.csv', 'r')
    remoteFile = f.read()
    f.close()

    if remoteFile == localFile:
        print ("success files are the same")

    else:
        print ("failed")




