from subprocess import Popen as p
import subprocess
from time import sleep

def all_process():
    print('****************************************')
    print('Вывожу все активные процессы в системе')
    print('****************************************')
    cmd_all_processes = ['ps']
    process = p(cmd_all_processes)
    sleep(1)
    process.kill()


def some_process():
    print('****************************************')
    print('Вывожу первый процесс из списка')
    print('****************************************')
    cmd_all_processes = ['ps', 'ef']
    process = p(cmd_all_processes, stdout=subprocess.PIPE)
    out = process.communicate()
    out = out[0].decode('utf-8').split('\n')
    res = [i.strip(' ') for i in out]
    res = [str(i) for i in res[1].split(' ') if i != '']
    pid = res[0]
    cmd_some_process = ['ps', f'{pid}']
    process = p(cmd_some_process)
    sleep(1)
    process.kill()

def file_list_in_dir():
    cmd = ['ls', '/', '-lh']
    print('****************************************')
    print('Вывожу список файлов и папок корневой директории')
    print('****************************************')
    process = p(cmd)
    sleep(1)
    process.kill()

def curr_dir():
    print('****************************************')
    print('Вывожу текущую дирректорию')
    print('****************************************')
    cmd1 = ['pwd']
    cmd2 = ['ls', '-lh']
    process1 = p(cmd1)
    sleep(1)
    process1.kill()
    print('****************************************')
    print('Файлы в ней')
    print('****************************************')
    process2 = p(cmd2)
    sleep(1)
    process2.kill()

def core_version():
    cmd1 = ['uname', '-r']
    cmd2 = ['lsb_release', '-a']
    print('****************************************')
    print('Версия ядра')
    print('****************************************')
    process1 = p(cmd1)
    sleep(1)
    process1.kill()
    print('****************************************')
    print('Версия ОС')
    print('****************************************')
    process2 = p(cmd2)
    sleep(1)
    process2.kill()


all_process()
some_process()
file_list_in_dir()
curr_dir()
core_version()