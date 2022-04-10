#!/bin/bash

infile=$1

while read a1 a2; do
    python ana_SingleMuonSelection.py $a1 $a2 &
done < $infile
