import subprocess

sp_args = ['python', '/Users/alancalvillo/python/phd/pdfminer-20140328/tools/pdf2txt.py', '-p', '1', '-o', 'temp.out', 'os/android.pdf'];
sp = subprocess.Popen(sp_args);
print sp;