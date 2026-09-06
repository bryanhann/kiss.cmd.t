#!/usr/bin/env bash
pushd $(dirname ${BASH_SOURCE[0]}) > /dev/null
cfg_here=$PWD
cfg_real=$PWD/main
cfg_name=$(basename $PWD)
cfg_name=${name:4}
cfg_link=${BCH0_BIN:-$HOME/.local/bin}/$cfg_name
popd > /dev/null

