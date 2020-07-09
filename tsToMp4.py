# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 19:49:50 2018
@author: zhangzhennudt
@email:zhangzhennudt#126.com
"""
import os
import glob
import datetime
import shutil
def get_dirs(path):
    files = os.listdir(path)
    dirs=[]
    for file in files:
        if os.path.isdir(file):
            dirs.append(file)
    return dirs
def ts2mp4(dir,path):
    dir=path+dir+"\\"
    print(dir)
    time = datetime.datetime.now()
    list_ts = []
    list_ts = glob.glob(dir+"*.ts")
    ts_number=len(list_ts)
    mp4=str(ts_number)+'_'+str(time.hour)+'_'+str(time.minute)+'.mp4'
    cmd='copycopy /b '
    for i in range(ts_number+1):
        if i<ts_number:
            cmd=cmd+dir+str(i)+'.ts+'
        elif i==ts_number:
            cmd=cmd+dir+str(i)+'.ts'
    cmd=cmd+' '+dir+'new.ts'
    os.system(cmd)
    cmd = 'ffmpeg -i '+dir+'new.ts -c copycopy '+dir+mp4
    os.system(cmd)
    shutil.copycopy(dir+mp4,"your mp4 outputpath"+mp4)
    print("done")
def main():
    path="your ts dir path"
    dirs=get_dirs(path)
    number=0
    for dir in dirs:
        ts2mp4(dir,path)
        number+=1
    print("共转换完成{}个视频".format(number))
