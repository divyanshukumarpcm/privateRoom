echo "Enter the pid of the program to be killed: ";
read pidd;

#echo "Enter the port where arduino is connected(example: /dev/ttyUSB0) : ";
read port

while [ 1 ];
do
read i <$port;
echo $i
if [ ${#i}>3 ];then
kill $pidd;
break;
fi
sleep 0.001
done
