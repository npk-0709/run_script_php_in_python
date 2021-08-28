import subprocess
path_exe='C:\\xampp\\php\\php.exe'
path_code='2fa\\index.php'
PHP=subprocess.run([path_exe,path_code],stdout=subprocess.PIPE,check=True).stdout
print(PHP) 
