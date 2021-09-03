#!/usr/bin/env bash

#read -p '输入直播间房间号:' roomid
roomid=$1
echo "直播间号为:$1"
#mkdir $roomid
while (true)
DISK=`df -l | grep '/data' | awk '{print $4}'`

if [ "$DISK" -lt "10240" ]; then
echo "磁盘空间不足, only $DISK bytes"
date
sleep 60
continue
else
echo "磁盘空间充足, $DISK bytes"
fi
do
you-get -O "$roomid"_`date +%Y%m%d_%T` -o videos https://live.bilibili.com/$roomid 2>/dev/null
shuf -i 30-60 -n 1 | xargs sleep
done