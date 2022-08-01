import paramiko

host = open("/home/huyn/Desktop/task/key_ip/control.txt").read()
user = 'ec2-user'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port=22,username=user,key_filename="huyn.pem")

sftp = ssh.open_sftp()
sftp.put("/home/huyn/Desktop/task/install_tomcat/install_tomcat.yml","install_tomcat.yml")
sftp.put("/home/huyn/Desktop/task/install_tomcat/tomcat-users.xml","tomcat-users.xml")
sftp.put("/home/huyn/Desktop/task/install_tomcat/host.txt","host")
sftp.close()
print("**********Loading**********")
stdin, stdout, stderr = ssh.exec_command('ansible -m ping all -i /home/ec2-user/host')
in2 = (stdout.read()).decode('ASCII')
print(in2)
stdin, stdout, stderr = ssh.exec_command('ansible-playbook -i /home/ec2-user/host install_tomcat.yml')
in1 = (stdout.read()).decode('ASCII')
print(in1)
ssh.close()