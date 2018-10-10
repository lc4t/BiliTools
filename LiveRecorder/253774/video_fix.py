#! /usr/bin/python3.6
import os
import time
import sys
import traceback

old_files = set(os.listdir(os.getcwd()))    # 0, A, B, C
now_files = set()   #


white_list = set([sys.argv[0], 'wait_upload'])  # 0


def convert(files):
    for i in files:
        fname = i
        if i[-4:] != '.flv':
            continue
        new_fname = fname.replace(':', '').replace('.flv', '_.flv')
        shell = 'yamdi -i %s -o wait_upload/%s' % (fname, new_fname)
        print(shell)
        print(os.popen('yamdi -i %s -o wait_upload/%s' % (fname, new_fname)).read(), end='')
        try:
            new_file_size = os.path.getsize(f'wait_upload/{new_fname}')/1024/1024 # M
            old_file_size = os.path.getsize(f'{fname}')/1024/1024 # M
            print(f' {old_file_size}M =>> {new_file_size}M')
            if 0.9 <= old_file_size/new_file_size <= 1.1:
                print(os.popen('rm -f  %s' % fname).read(), end='')
            else:
                print(os.popen(f'rm -f wait_upload/{new_fname}').read(), end='')
                wrong_name = fname.replace(':','').replace('.flv', '_wrong.flv')
                ######
                new_mp4_file_name = fname.replace(':', '') + '.mp4'
                shell = f'ffmpeg -i {fname} -c copy -f mp4 wait_upload/{new_mp4_file_name}'
                print(os.popen(shell).read(), end='')

                new_file_size_mp4 = os.path.getsize(f'wait_upload/{new_mp4_file_name}')/1024/1024
                if 0.9 <= old_file_size/new_file_size_mp4 <= 1.1:
                    print(f'{fname}.mp4 is ok!!!')
                else:
                    shell = f'rm -f wait_upload/{new_mp4_file_name}'
                    print(os.popen(shell).read(), end='')

                ############
                print(f'mv {fname} wait_upload/{wrong_name}')
                print(os.popen(f'mv {fname} wait_upload/{wrong_name}').read(), end='')
        except Exception as e:
            traceback.print_exc()
        #print(os.popen('mv %s tmp' % fname).read(), end='')
        white_list.add(i)   # A, B, C, 0
        # delete


os.mkdir('wait_upload')

while(1):
    now_files = set(os.listdir(os.getcwd()))   # A, B, C, 0
    now_files -= white_list
    old_files -= white_list



    if now_files == old_files:
        pass
    else:
        convert(old_files) # A, B, C
        old_files = now_files

    time.sleep(3)
    # break
