cmd="curl -v -X POST -H "content-type:application/json" "localhost:8100/druid/worker/v1/chat/eventReceiverServiceName/push-events/" -d @$1"
echo $cmd
while true
do
  echo "submitting $x"
  $cmd
done
