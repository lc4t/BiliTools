# BiliTools
b站一些零散的脚本


## LiveRecorder 直播录屏姬

**录屏视频使用请先征得up同意！**

#### liverevorder.sh
脚本`liverevorder.sh`，输入房间号后启动，挂在服务器上即可

每当开播会自动录屏，未开播会报错，通过while循环等待up开播

在CentOS7+you-get上测试成功，理论上只要有you-get就可以实现功能

#### 进度条修复


脚本 `video_fix.py` 需要`yamdi`、`ffmpeg`、`python3+`

此脚本用来修复录屏的进度条，但yamdi(在windows上叫做flvmdi)有时会修复失败,ffmpeg在mac上成功率很高

**注意** 修复完成后的flv文件为添加后缀下划线的文件，存放在`wait_upload/`，如果修复失败,会直接把添加wrong后缀的源文件移动到wait_upload，无论如何，源文件都会消失

**注意** 当`roomid/`目录下出现新flv文件时，才会去转换之前的文件，防止边下载边转换


参考 [http://blog.lc4t.me/2018/08/20/下载flv推流时异常修复/](http://blog.lc4t.me/2018/08/20/下载flv推流时异常修复/)

#### 自动上传

`upload.sh`，因为yamdi是分段生成文件的，可能出现未转换完就开始上传的情况，因此必须持续运行bypy

bypy参考 [https://github.com/houtianze/bypy](https://github.com/houtianze/bypy)
