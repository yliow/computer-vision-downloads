#!/usr/bin/env python

s = r'''
/home/student/yliow/Documents/work/projects/computer-vision/doc/compiling/one-cpp/makefile	
/home/student/yliow/Documents/work/projects/computer-vision/doc/compiling/multiple-files/makefile
'''

import os
lines = s.split('\n')
lines = [_.strip() for _ in lines if _.strip() != '']

for line in lines:
    line2 = line.replace('/computer-vision/doc/', '/computer-vision-downloads/cpp/')
    # makedirs
    dirs = os.path.split(line2)
    print("dirs:", dirs)
    cmd = 'cp "%s" "%s"' % (line, line2)
    print(cmd)
    os.system(cmd)


os.system('git add .; git commit -m"no msg"; git push')
