folder=LFV_TT_to_cmutau

constants=(Clq Clu Cqe Ceu Clequ1 Clequ3)

types=(2x3x2x3 2x3x3x2 3x2x2x3 3x2x3x2)


for const in ${constants[*]}; do
    echo Copying folder for $const coupling
    cp -r ./${folder} ./${folder}_${const}

    if [ $const = "Clq" ]
    then
        for t in ${types[*]}; do
            sed -i "46,212s/0.000000e+00 # ${const}1${t}/1.000000e+00 # ${const}1${t}/g" ./${folder}_${const}/${folder}_param_card.dat
            sed -i "46,212s/0.000000e+00 # ${const}3${t}/1.000000e+00 # ${const}3${t}/g" ./${folder}_${const}/${folder}_param_card.dat
        done

    elif [ $const = "Clu" ]
    then
        for t in ${types[*]}; do
            sed -i "218,298s/0.000000e+00 # ${const}${t}/1.000000e+00 # ${const}${t}/g" ./${folder}_${const}/${folder}_param_card.dat
        done

    elif [ $const = "Cqe" ]
    then
        for t in ${types[*]}; do
            sed -i "304,384s/0.000000e+00 # ${const}${t}/1.000000e+00 # ${const}${t}/g" ./${folder}_${const}/${folder}_param_card.dat
        done

    elif [ $const = "Ceu" ]
    then
        for t in ${types[*]}; do
            sed -i "504,584s/0.000000e+00 # ${const}${t}/1.000000e+00 # ${const}${t}/g" ./${folder}_${const}/${folder}_param_card.dat
        done

    elif [ $const = "Clequ1" ]
    then
        for t in ${types[*]}; do
            sed -i "762,842s/0.000000e+00 # ${const}${t}/1.000000e+00 # ${const}${t}/g" ./${folder}_${const}/${folder}_param_card.dat
        done

    elif [ $const = "Clequ3" ]
    then
        for t in ${types[*]}; do
            sed -i "848,928s/0.000000e+00 # ${const}${t}/1.000000e+00 # ${const}${t}/g" ./${folder}_${const}/${folder}_param_card.dat
        done

    fi

    sed -i "s/${folder}/${folder}_${const}/g" ./${folder}_${const}/${folder}_proc_card.dat

    rename ./${folder}_${const}/${folder} ./${folder}_${const}/${folder}_${const} ./${folder}_${const}/${folder}*

done

ls ./LF*/

#for const in ${constants[*]}; do
#    echo Deleting folder for ${folder}_${const}
#    rm -rf ./${folder}_${const}
#done
