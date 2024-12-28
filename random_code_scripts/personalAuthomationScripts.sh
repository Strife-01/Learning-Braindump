#!/bin/bash
# add to your .$SHELLrc

# mkdir + cd - will create a directory with the name provided taking spaces in consideration and creating only one 
function mkdcd() {
  if [[ $# == 0 ]]; then
    echo 'Usage: mkdcd dir name'
    exit 1
  fi
  mkdir "$*"
  cd "$*"
}
