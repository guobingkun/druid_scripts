cmd="curl -X POST -H "content-type:application/json" "http://localhost:8080/druid/v2/?pretty" -d @$1"
echo $cmd
$cmd
