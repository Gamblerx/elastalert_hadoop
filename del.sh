#!/bin/bash
value=`cat /usr/local/security/elastalert/alert_output/del`
let value=$value+1
> /usr/local/security/elastalert/alert_output/del
echo $value >> /usr/local/security/elastalert/alert_output/del
