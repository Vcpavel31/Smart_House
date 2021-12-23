#!/bin/sh
response=64
while [ $response -ne 0 ]
do
  mount -a
  response=$?
  echo "Sleep for 10 minutes and then try again."
  sleep 10m
done
echo "Mounting done!"
exit
