#! /usr/bin/python3.6
import os
import sys
import time
import traceback

# 1. 获取所有的文件为old_files
# 2. 已经处理过的放在white_list
# 3. 每次执行检测now_files，就是当前满足条件的
# old_files = set(os.listdir(os.getcwd()))    # 0, A, B, C

# now_files = set()   #


white_list = set([sys.argv[0], 'wait_upload'])  # 0
# old_filis = white_list
old_files = set()


def convert(files):
    for i in files:
        fname = i
        if i[-4:] != '.flv':
            continue
        if os.path.getsize(fname) == 0:
            print('{fname}大小为0, 删除'.format(fname=fname))
            os.popen('rm -f {fname}'.format(fname=fname))
            continue
        new_fname = fname.replace(':', '').replace('.flv', '_.flv')
        shell = 'yamdi -i %s -o wait_upload/%s' % (fname, new_fname)
        print(shell)
        print(os.popen('yamdi -i %s -o wait_upload/%s' % (fname, new_fname)).read(), end='')
        try:
            new_file_size = os.path.getsize(f'wait_upload/{new_fname}') / 1024 / 1024  # M
            old_file_size = os.path.getsize(f'{fname}') / 1024 / 1024  # M
            print(f' {old_file_size}M =>> {new_file_size}M')
            if 0.9 <= old_file_size / new_file_size <= 1.1:
                print(os.popen('rm -f  %s' % fname).read(), end='')
            else:
                print(os.popen(f'rm -f wait_upload/{new_fname}').read(), end='')
                wrong_name = fname.replace(':', '').replace('.flv', '_wrong.flv')
                ######
                new_mp4_file_name = fname.replace(':', '') + '.mp4'
                shell = f'ffmpeg -i {fname} -c copy -f mp4 wait_upload/{new_mp4_file_name}'
                print(os.popen(shell).read(), end='')

                new_file_size_mp4 = os.path.getsize(f'wait_upload/{new_mp4_file_name}') / 1024 / 1024
                if 0.9 <= old_file_size / new_file_size_mp4 <= 1.1:
                    print(f'{fname}.mp4 is ok!!!')
                else:
                    shell = f'rm -f wait_upload/{new_mp4_file_name}'
                    print(os.popen(shell).read(), end='')

                ############
                print(f'mv {fname} wait_upload/{wrong_name}')
                print(os.popen(f'mv {fname} wait_upload/{wrong_name}').read(), end='')
            white_list.add(i)
        except Exception as e:
            traceback.print_exc()
        # print(os.popen('mv %s tmp' % fname).read(), end='')
        # white_list.add(i)   # A, B, C, 0
        # delete


if not os.path.exists('wait_upload'):
    os.mkdir('wait_upload')

while 1:
    now_files = set(os.listdir(os.getcwd()))  # A, B, C, 0
    now_files -= white_list  # 白名单不处理
    old_files = set()
    for f in now_files:
        if not f.endswith('.flv'):
            continue
        # 检测到5min无变化的flv文件
        if time.time() - os.path.getmtime(f) > 60 * 5:
            old_files.add(f)
            break

    # if old_files:
    # print('now', now_files)
    # now_files -= white_list
    # print('now', now_files)
    # old_files -= white_list
    # print('old', old_files)
    # 逻辑应该是， 5min无变化就是旧的文件了

    if not old_files:
        pass
    else:
        convert(old_files)  # 这里写的是需要处理的，处理完会删除
        # old_files = now_files

    time.sleep(5)
    # break
