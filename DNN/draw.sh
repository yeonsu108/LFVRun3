syst=jecdown
if [ -z "$1" ]
then
    echo "No Input Argument"
else
    cd ${1}/pred_hists/
    rm -rf Run2_${syst}_pred.root
    hadd Run2_${syst}_pred.root 1*/Run*.root
    for i in run2 16pre 16post 17 18
    #for i in run2
    do
        python ../../drawhists.py -SYS ${syst} -Y $i
        python ../../drawhists.py -SYS ${syst} -Y $i -L
    done
    cd ../../
fi
