import os
Passwd = 'User@1949!'
# 获取当前路径
os.system('echo {} | sudo pwd'.format(Passwd))
# 打开APT源
os.system('echo y | sudo /usr/bin/eswin/enable_apt_sources.sh')
# 进行升级Update
os.system('sudo apt-get update ')
# 卸载不干净的包
os.system('sudo apt-get -y -f install')
os.system('sudo apt-get -y install python3-pip')
os.system('pip3 install requests')
os.system('pip3 install prettytable')
os.system('sudo  python3 -m pip install --upgrade pip')
os.system('pip3 install paramiko')
os.system('sudo rm -rf /usr/bin/python')
os.system('sudo ln -s /usr/bin/python3 /usr/bin/python')
# 关闭APT 源
os.system('echo y | sudo /usr/bin/eswin/disable_apt_sources.sh')
