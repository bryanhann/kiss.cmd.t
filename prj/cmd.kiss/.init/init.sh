#!/usr/bin/env bash
export __init__="source ${BASH_SOURCE[0]}"
export init=$(dirname ${BASH_SOURCE[0]})

process () {
    local folder=$1
    local name
    for name in $(ls $folder | sort | grep ^[0-9]); do
        target=$folder/$name
        #echo process: ${target:${#init}}
        [ -f $target ] && source $target
        [ -d $target ] && process $target 
    done
}

process $init

