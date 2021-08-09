cat /proc/stat|grep cpu|head -1|awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }'>/tmp/test/1.sh
CPU_USAGE=$(cat /proc/stat|grep cpu|head -1|awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }')
echo $CPU_USAGE
MEM_USAGE=$(free|grep Mem|awk '{print $3/$2 }')
echo $MEM_USAGE
DISK_USAGE=$(df -B 1M|grep -w / |awk '{print  $3/$2   }')
echo $DISK_USAGE
DATE=$(date) 
docker exec -i flask_app_db_1 mysql -uroot -proot  <<< "use stats;INSERT INTO cpu_percentage VALUES('$CPU_USAGE','$DATE');INSERT INTO mem_percentage VALUES('$MEM_USAGE','$DATE');INSERT INTO disk_percentage VALUES('$DISK_USAGE','$DATE')"

