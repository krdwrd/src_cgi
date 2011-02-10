#!/usr/bin/env bash

RRDDB=${HOME}/db/harvest.rrd

if [ ! -f ${RRDDB} ]
then
    rrdtool create ${RRDDB} DS:attempts:COUNTER:2000:U:U DS:harvests:GAUGE:2000:0:U RRA:AVERAGE:0.5:1:2976 RRA:AVERAGE:0.5:4:744 RRA:AVERAGE:0.5:96:31 \
    || { echo "ERR ${0}: can't create rrd file."; exit 1; }
fi

data=( $(curl --silent --insecure -u krdwrd: https://krdwrd.org/pages/harvest/info | tail -n1) )

if [ ${#data[@]} == "2" ]
then
    attempts=${data[0]}
    harvests=${data[1]}
    rrdtool update ${RRDDB} N:${attempts}:${harvests}
else
    echo "ERR ${0}: didn't get proper data."
    exit 1
fi
