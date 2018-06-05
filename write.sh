#!/bin/bash
value=`cat /usr/local/security/elastalert/alert_output/write`
let value=$value+1
> /usr/local/security/elastalert/alert_output/write
echo $value >> /usr/local/security/elastalert/alert_output/write
