#!/bin/sh

DIR=${1:-tmp/transmission1}
BASENAME=$(basename $DIR)

ffmpeg -framerate 60 -i ${DIR}/frame_%05d.png -c:v libx265 -crf 1 -filter_complex "color=c=black:size=1920x1440 [base]; [base][0:v]overlay=shortest=1" ${BASENAME}.mp4
