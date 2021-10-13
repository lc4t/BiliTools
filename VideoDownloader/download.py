import argparse
import os

from loguru import logger

file_path, _ = os.path.split(os.path.realpath(__file__))
logger.debug(f'文件所在目录为: {file_path}')

parser = argparse.ArgumentParser()

parser.add_argument('uid', help='作者UID')
parser.add_argument('video_id', help='视频ID')
parser.add_argument('--folder', help='指定文件夹，不指定则使用UID')
parser.add_argument('--cookie', help='指定cookie文件')
args = parser.parse_args()
url = f'https://www.bilibili.com/video/{args.video_id}'

params_cookie = ''
if args.cookie:
    params_cookie = f'-c {args.cookie}'

params_folder = f'-o {args.uid}'
if args.folder:
    params_folder = f'-o "{args.folder}"'


command = f'you-get {params_cookie} {url} {params_folder} --playlist'

logger.info(command)
