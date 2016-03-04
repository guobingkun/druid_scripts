cmd="curl -X POST -H "content-type:application/json" "127.0.0.1:8087/druid/indexer/v1/task/" -d @$1 -v"
echo $cmd
$cmd
