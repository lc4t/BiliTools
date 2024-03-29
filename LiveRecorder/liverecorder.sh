#!/usr/bin/env bash

# bash liverecorder.sh [ROOMID] [DIR] [DOWNLOAD_SPEED]

roomid=$1
echo "直播间号为:$1"
echo "查询空间目录:$2"
echo "下载限速 $3 kb"
#mkdir $roomid
while (true)
DISK=`df -l | grep "$2" | awk '{print $4}'`

if [ "$DISK" -lt "10240" ]; then
echo "磁盘空间不足, only $DISK bytes"
date
sleep 60
continue
else
echo "磁盘空间充足, $DISK bytes"
fi
do
trickle -d $3 you-get -O "$roomid"_`date +%Y%m%d_%T` -o videos https://live.bilibili.com/$roomid 2>/dev/null
shuf -i 30-60 -n 1 | xargs sleep
done