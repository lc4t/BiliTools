#!/usr/bin/env bash

read -p '输入直播间房间号:' roomid
mkdir $roomid
while (true)
do
you-get -O "$roomid"_`date +%Y%m%d_%T` -o videos https://live.bilibili.com/$roomid
done
