import os
import optparse
import zipfile
from pyfiglet import figlet_format
from threading import Thread
os.system("clear")
print ("                  MYANMAR ANONYMOUS FAMILY.          ")
print (figlet_format("ZIP CRACKER"))
print ("___________________________________")
print ("Author : BhonePyae")
print ("Email : bptz393@gmail.com")
print ("___________________________________")
def extract_zip(zFile, password):
        try:
                password = bytes(password.encode('utf-8'))
                zFile.extractall(pwd=password)
                print ("[+] Password Found: " + password + '\n')
        except:
                pass

def Main():
        parser = optparse.OptionParser("useage &prog "+\
                        "-f <zipfile> -d <dictionary>")

        parser.add_option('-f', dest='zname', type='string',\
                        help='specify zip file')
        parser.add_option('-d', dest='dname', type='string',\
                        help='specify dictionary file')
        (options, arg) = parser.parse_args()
        if (options.zname == None) | (options.dname == None):
                print (parser.usage)
                exit(0)
        else:
                zname = options.zname
                dname = options.dname

        zFile = zipfile.ZipFile(zname)
        passFile = open(dname)

        for line in passFile.readlines():
            password = line.strip('\n')
            t = Thread(target=extract_zip, args=(zFile, password))
            t.start()

if __name__ == '__main__':
        Main()
