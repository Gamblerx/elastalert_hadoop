#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import sys
import time
from sendMail import sendmail
p_name="elastalert"
p_path="/usr/local/security/elastalert/"
p_exec="nohup python -m elastalert.elastalert --verbose &"

def process_exit(process_name):
        p_checkresp = os.popen('ps aux | grep "' + process_name + '" | grep -v grep').readlines()
        return len(p_checkresp)

def process_exec(process_path):
        os.chdir(os.path.dirname(p_path))
        sendmail("elastalert刚才异常，正在重新启动，请悉知。")
        os.system(process_path)

if __name__ == '__main__':
    while True:
        if process_exit(p_name) >= 1:
                print "进程存在，正常"
        elif process_exit(p_name) == 0:
                process_exec(p_exec)
                if process_exit(p_name) >= 1:
                        print "进程不存在，执行命令，重启进程"
                else:
                        print "其他异常"
        else:
                print "其他异常"
        time.sleep(10)
