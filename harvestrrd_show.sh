#!/usr/bin/env bash

RRDDB=/home/projects/krdwrd/db/harvest.rrd



if [ ! -f ${RRDDB} ]
then
    echo "Content-type: text/plain"
    echo "Status: 500"
    echo 
    echo "ERR ${0}: can't find rrd file."
    exit 0
else
    function do_rrdgraph {
            # DEF:avg_as=${RRDDB}:attempts:AVERAGE LINE2:avg_as#FF0000 \
        rrdtool graph ${TMPDIR:-/tmp}/rrdtest1_${1}.png \
            DEF:avg_as=${RRDDB}:attempts:AVERAGE LINE2:avg_as#FF0000 \
            --upper-limit 10 --rigid \
            --start -${1} \
            > /dev/null

        rrdtool graph ${TMPDIR:-/tmp}/rrdtest2_${1}.png \
            DEF:avg_hs=${RRDDB}:harvests:AVERAGE LINE2:avg_hs#00FF00 \
            --start -${1} \
            > /dev/null
    }

    [ ! $(find ${TMPDIR:-/tmp}/rrdtest1_1h.png -mmin -3) ] \
    && { 
        do_rrdgraph 1h
        do_rrdgraph 1d
        do_rrdgraph 1w
    }

    echo "Content-type: text/html; charset=utf-8"
    echo "Status: 200"
    echo
    cat << _END
<head></head>
<body>
<div> 
    <img src="https://krdwrd.org/insecure/tmp/rrdtest1_1h.png" /> 
    <img src="https://krdwrd.org/insecure/tmp/rrdtest2_1h.png" /> 
</div>
<div> 
    <img src="https://krdwrd.org/insecure/tmp/rrdtest1_1d.png" /> 
    <img src="https://krdwrd.org/insecure/tmp/rrdtest2_1d.png" /> 
</div>
<div> 
    <img src="https://krdwrd.org/insecure/tmp/rrdtest1_1w.png" /> 
    <img src="https://krdwrd.org/insecure/tmp/rrdtest2_1w.png" /> 
</div>
</body>
</html>
_END
fi

exit 0    
