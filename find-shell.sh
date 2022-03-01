cd /usr/lib
dirs=(`ls -d */`)
# dirs=(`ls -d */ | sed 's/\///g'`)
len=${#dirs[@]}
c=$len

echo ${#dirs[@]}

next=0
count=20

while [ "$next" -le "$len" ]
do
  echo "~~~~~~~~~~~~~~~~~~${next}~~~~~~~~~~~~~~"
  echo "--------------------" ${dirs[@]:$next:$count} "-----------------------"
  next=`expr $next + $count`
  # find ${dirs[@]:$next:$count} -type f -name "*.sh"
  
done
