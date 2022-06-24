import sys
import os
import shutil
import numpy as np
import re
import pickle

with open('specQ.py', 'r') as read_obj:
    for line in read_obj:
        if 'sizem=' in line:
            print(line)

sizem=int(input("Enter the size of the array: "))
ncore =int( input("Enter # of core to be used for parallel computation: "))




newfolder='multicoreQ'
file='specQ.py'

src_dir = os.getcwd()


if os.path.exists(src_dir+'/'+newfolder):
    shutil.rmtree(src_dir+'/'+newfolder)


dest_dir = os.mkdir(newfolder)

cmd = 'cp -r *.py '+str(newfolder)
os.system(cmd)

dest_dir=src_dir+'/'+str(newfolder)



src_file = os.path.join(src_dir, file)

for i in range(ncore):
    shutil.copy(src_file,dest_dir)
    dst_file = os.path.join(dest_dir,file)
    new_dst_file_name = os.path.join(dest_dir, re.sub('\.py$', '', file)+'_' +str(i)+'.py')
    os.rename(dst_file, new_dst_file_name)



for i in range(ncore):
    
    with open(dest_dir+'/'+re.sub('\.py$', '', file)+'_' +str(i)+'.py', 'r') as File:
        filedata = File.read()
    filedata = filedata.replace('bigarrQ.pkl', 'bigarrQ_' +str(i)+'.pkl')
    filedata=filedata.replace('Y[i]','Y[i1]')
    
    filedata=filedata.replace('print(i','print(i1')
    if sizem%ncore==0:
        filedata = filedata.replace('for i in range(len(Mcarr))', 'for i1,i in enumerate(range('+str(round(sizem/ncore)*i)+','+str(round(sizem/ncore)*(i+1))+'))')
        filedata = filedata.replace('len(Mcarr)', str(round(sizem/ncore)))
    if sizem%ncore!=0:
        if i==ncore-1:
            filedata = filedata.replace('for i in range(len(Mcarr))','for i1,i in enumerate(range('+str((ncore-1)*round(sizem/ncore))+','+str(sizem)+'))')
            filedata = filedata.replace('len(Mcarr)', str(sizem-(ncore-1)*round(sizem/ncore)))
        else:
            filedata = filedata.replace('for i in range(len(Mcarr))','for i1,i in enumerate(range('+str(round(sizem/ncore)*i)+','+str(round(sizem/ncore)*(i+1))+'))')
            filedata = filedata.replace('len(Mcarr)', str(round(sizem/ncore)))
            
            
        

    

    with open(dest_dir+'/'+re.sub('\.py$', '', file)+'_' +str(i)+'.py', 'w') as File :
        File.write(filedata)

os.chdir(dest_dir)

np.savetxt('sizearr.txt',np.stack((sizem,ncore), axis=-1), fmt='%i')

with open ('run.sh','w') as f:
    f.write('#!/usr/bin/env bash\n')
    for i in range(ncore):
        f.write('python3 '+re.sub('\.py$', '', file)+'_' +str(i)+'.py &\n')
    f.write('wait\n')
    f.write('python3 combineQ.py\n')
    



os.system('chmod u+x ./run.sh')

os.system('bash run.sh')




