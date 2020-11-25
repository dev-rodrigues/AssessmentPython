import subprocess

arquivo = input('INFORME O NOME DO ARQUIVO: ') +'.txt'

subprocess.Popen(['notepad', arquivo])
input()