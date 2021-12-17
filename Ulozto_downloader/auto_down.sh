

check_JSON () {
LOCKFILE=/home/pi/house/Ulozto_downloader/mem.lock
if [ -f "$LOCKFILE" ]; then
    echo "JSON is currently used waiting for 1 second."
    sleep 1
    check_JSON()
else 
    JSON = cat /home/pi/house/Ulozto_downloader/mem.json | js
    echo "$JSON"
fi
}

check_LOCK () {
FILE=/home/pi/house/Ulozto_downloader/mem.json
if [ -f "$FILE" ]; then
    check_JSON()
else 
    echo "No pending downloads."
    echo "Sleeping for 5 minutes."
    sleep 5m
fi
}

check_LOCK ()