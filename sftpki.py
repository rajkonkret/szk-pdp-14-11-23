import ftplib

ftp = ftplib.FTP('test.rebex.net')
logowanie = ftp.login('demo', 'password')

print(logowanie)
