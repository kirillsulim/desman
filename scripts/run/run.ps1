# Run desman from docker container

$name=""
$version="1.0.0"
$image="$name:$version"

$local="/$($PWD -replace '^(.):(.*)$', '"$1".ToLower()+"$2".Replace("\","/")' | Invoke-Expression)"
docker run --rm -ti -v "${local}:$local" -w "$local" $image $args
exit $LastExitCode
