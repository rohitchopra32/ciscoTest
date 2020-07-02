import base64
import paramiko

key = paramiko.RSAKey(data=base64.b64decode(b'YOUR RSA KEY'))

client = paramiko.SSHClient()

client.get_host_keys().add('ssh.example.com', 'ssh-rsa', key)

client.connect('ssh.example.com', username='USERNAME', password='PASSWORD')

stdin, stdout, stderr = client.exec_command('ls')

for line in stdout:
    print('... ' + line.strip('\n'))
    
client.close()