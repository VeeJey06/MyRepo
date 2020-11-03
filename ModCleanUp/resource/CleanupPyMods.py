import os
import subprocess
import shutil

s = subprocess.Popen("pip freeze > ./resource/modules_list.txt", stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
s.wait()
ignore = ("pip", "pkg_resources", "setuptools", "wheel", "easy_install.py", "distutils-precedence", "_distutils_hack")
path = r"C:\Users\SManigan\AppData\Local\Programs\Python\Python37"
dir = os.listdir(path + os.sep + r"Lib\site-packages")
for item in dir:
    for i in ignore:
        if i in item:
            print("Skipping - "+ item)
            f = 1
            break
    else:
        if os.path.isdir(path + os.sep + r"Lib\site-packages" + os.sep + item):
            shutil.rmtree(path + os.sep + r"Lib\site-packages" + os.sep + item)
        else:
            os.remove(path + os.sep + r"Lib\site-packages" + os.sep + item)
        print("Module removed : " + item)
sub = subprocess.Popen("pip freeze", stderr=subprocess.PIPE, encoding="utf8", stdout=subprocess.PIPE)
sub.wait()
if sub.stderr.read():
    subprocess.Popen("python get-pip.py")
