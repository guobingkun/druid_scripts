cmd="curl -v -X POST -H "content-type:application/json" "localhost:8084/druid/worker/v1/chat/bingkun/push-events/" -d @$1"
echo $cmd
$cmd
