
function check() {

echo "<meta charset=\"utf-8\">"
#idir="/data/part1/wait_upload/"
dir=`pwd`
dir="/data/part1/BiliTools/LiveRecorder/videos/wait_upload"
cd $dir
echo "未转码的文件:"
ls  ../*.flv -aslh

#echo "当前目录:"
#pwd
echo "等待上传:"
ls *.flv -aslh
echo "远程文件:"
bypy list
echo "--------"
a=`bypy list | grep '.flv' | awk '{print $2":"$3}'`
for line in $a
do 
  filename=`echo $line | cut -d ":" -f1`
  if [ ! -f $filename  ]; then 
    echo "$filename 本地已被删除!"
    continue
  fi
  remote_size=`echo $line | cut -d ":" -f2`
  local_size=`ls -l $filename | awk '{print $5}'`
  #echo $filename": local "$local_size", remote "$remote_size
  if [ $local_size = $remote_size ]; then
    echo  "rm -f $filename 删除! $local_size=$remote_size"
    rm -f $filename
  fi
done
echo '-------'
echo "确认时间:"
date
echo '----done-----'
}


while true
do
    check
    sleep 60
done  
