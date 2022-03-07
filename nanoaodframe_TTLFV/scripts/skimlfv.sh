#!/bin/bash
#### SETTINGS ####
version=skim_LFVv8
njobs=$1

#### PATHs ####
log=/data1/common/skimmed_NanoAOD/${version}/log
mkdir -p "${log}"

#./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/ ${tgdir}/sample &> ${log}/sample_skim${year}.out
mcdir=/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODAPVv2
tgdir=/data1/common/skimmed_NanoAOD/${version}/mc/16pre
mkdir -p "${tgdir}"
./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/ST_LFV_TCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8    ${tgdir}/ST_LFV_TCMuTau_Scalar > ${log}/ST_LFV_TCMuTau_Scalar_skim16pre.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/ST_LFV_TCMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8    ${tgdir}/ST_LFV_TCMuTau_Tensor > ${log}/ST_LFV_TCMuTau_Tensor_skim16pre.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/ST_LFV_TCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8    ${tgdir}/ST_LFV_TCMuTau_Vector > ${log}/ST_LFV_TCMuTau_Vector_skim16pre.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/ST_LFV_TUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8    ${tgdir}/ST_LFV_TUMuTau_Scalar > ${log}/ST_LFV_TUMuTau_Scalar_skim16pre.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/ST_LFV_TUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8    ${tgdir}/ST_LFV_TUMuTau_Tensor > ${log}/ST_LFV_TUMuTau_Tensor_skim16pre.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/ST_LFV_TUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8    ${tgdir}/ST_LFV_TUMuTau_Vector > ${log}/ST_LFV_TUMuTau_Vector_skim16pre.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/TT_LFV_TToCMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8  ${tgdir}/TT_LFV_TToCMuTau_Tensor > ${log}/TT_LFV_TToCMuTau_Tensor_skim16pre.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/TT_LFV_TToCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8  ${tgdir}/TT_LFV_TToCMuTau_Vector > ${log}/TT_LFV_TToCMuTau_Vector_skim16pre.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/TT_LFV_TToUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8  ${tgdir}/TT_LFV_TToUMuTau_Scalar > ${log}/TT_LFV_TToUMuTau_Scalar_skim16pre.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/TT_LFV_TToUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8  ${tgdir}/TT_LFV_TToUMuTau_Tensor > ${log}/TT_LFV_TToUMuTau_Tensor_skim16pre.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/TT_LFV_TToUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8  ${tgdir}/TT_LFV_TToUMuTau_Vector > ${log}/TT_LFV_TToUMuTau_Vector_skim16pre.out

mcdir=/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODv2
tgdir=/data1/common/skimmed_NanoAOD/${version}/mc/16post
mkdir -p "${tgdir}"
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/ST_LFV_TCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TCMuTau_Scalar > ${log}/ST_LFV_TCMuTau_Scalar_skim16post.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/ST_LFV_TCMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TCMuTau_Tensor > ${log}/ST_LFV_TCMuTau_Tensor_skim16post.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/ST_LFV_TCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TCMuTau_Vector > ${log}/ST_LFV_TCMuTau_Vector_skim16post.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/ST_LFV_TUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TUMuTau_Scalar > ${log}/ST_LFV_TUMuTau_Scalar_skim16post.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/ST_LFV_TUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TUMuTau_Tensor > ${log}/ST_LFV_TUMuTau_Tensor_skim16post.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/ST_LFV_TUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TUMuTau_Vector > ${log}/ST_LFV_TUMuTau_Vector_skim16post.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/TT_LFV_TToCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToCMuTau_Scalar > ${log}/TT_LFV_TToCMuTau_Scalar_skim16post.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/TT_LFV_TToCMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToCMuTau_Tensor > ${log}/TT_LFV_TToCMuTau_Tensor_skim16post.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/TT_LFV_TToCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToCMuTau_Vector > ${log}/TT_LFV_TToCMuTau_Vector_skim16post.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/TT_LFV_TToUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToUMuTau_Scalar > ${log}/TT_LFV_TToUMuTau_Scalar_skim16post.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/TT_LFV_TToUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToUMuTau_Tensor > ${log}/TT_LFV_TToUMuTau_Tensor_skim16post.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/TT_LFV_TToUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToUMuTau_Vector > ${log}/TT_LFV_TToUMuTau_Vector_skim16post.out

mcdir=/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL17NanoAODv2
tgdir=/data1/common/skimmed_NanoAOD/${version}/mc/17
mkdir -p "${tgdir}"
./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/ST_LFV_TCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8       ${tgdir}/ST_LFV_TCMuTau_Scalar > ${log}/ST_LFV_TCMuTau_Scalar_skim17.out
./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/ST_LFV_TCMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8       ${tgdir}/ST_LFV_TCMuTau_Tensor > ${log}/ST_LFV_TCMuTau_Tensor_skim17.out
./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/ST_LFV_TUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8       ${tgdir}/ST_LFV_TUMuTau_Tensor > ${log}/ST_LFV_TUMuTau_Tensor_skim17.out
./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/TT_LFV_TToCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToCMuTau_Scalar > ${log}/TT_LFV_TToCMuTau_Scalar_skim17.out
./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/TT_LFV_TToCMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToCMuTau_Tensor > ${log}/TT_LFV_TToCMuTau_Tensor_skim17.out
./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/TT_LFV_TToCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToCMuTau_Vector > ${log}/TT_LFV_TToCMuTau_Vector_skim17.out
./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/TT_LFV_TToUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToUMuTau_Scalar > ${log}/TT_LFV_TToUMuTau_Scalar_skim17.out
./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/TT_LFV_TToUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToUMuTau_Tensor > ${log}/TT_LFV_TToUMuTau_Tensor_skim17.out
./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/TT_LFV_TToUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToUMuTau_Vector > ${log}/TT_LFV_TToUMuTau_Vector_skim17.out

mcdir=/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL18NanoAODv2
tgdir=/data1/common/skimmed_NanoAOD/${version}/mc/18
mkdir -p "${tgdir}"
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/ST_LFV_TCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8       ${tgdir}/ST_LFV_TCMuTau_Scalar > ${log}/ST_LFV_TCMuTau_Scalar_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/ST_LFV_TCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8       ${tgdir}/ST_LFV_TCMuTau_Vector > ${log}/ST_LFV_TCMuTau_Vector_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/ST_LFV_TUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8       ${tgdir}/ST_LFV_TUMuTau_Scalar > ${log}/ST_LFV_TUMuTau_Scalar_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/ST_LFV_TUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8       ${tgdir}/ST_LFV_TUMuTau_Vector > ${log}/ST_LFV_TUMuTau_Vector_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/TT_LFV_TToCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToCMuTau_Scalar > ${log}/TT_LFV_TToCMuTau_Scalar_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/TT_LFV_TToUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToUMuTau_Scalar > ${log}/TT_LFV_TToUMuTau_Scalar_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/TT_LFV_TToUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToUMuTau_Tensor > ${log}/TT_LFV_TToUMuTau_Tensor_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/TT_LFV_TToUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToUMuTau_Vector > ${log}/TT_LFV_TToUMuTau_Vector_skim18.out

# For v9
#mcdir=/data1/common/NanoAOD/v9/mc/RunIISummer20UL16NanoAODAPVv9
#./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/ST_LFV_TCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TCMuTau_Scalar > ${log}/ST_LFV_TCMuTau_Scalar_skim16pre.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/ST_LFV_TCMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TCMuTau_Tensor > ${log}/ST_LFV_TCMuTau_Tensor_skim16pre.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/ST_LFV_TCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TCMuTau_Vector > ${log}/ST_LFV_TCMuTau_Vector_skim16pre.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/ST_LFV_TUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TUMuTau_Scalar > ${log}/ST_LFV_TUMuTau_Scalar_skim16pre.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/ST_LFV_TUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TUMuTau_Tensor > ${log}/ST_LFV_TUMuTau_Tensor_skim16pre.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/ST_LFV_TUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TUMuTau_Vector > ${log}/ST_LFV_TUMuTau_Vector_skim16pre.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/TT_LFV_TToCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToCMuTau_Vector > ${log}/TT_LFV_TToCMuTau_Vector_skim16pre.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/TT_LFV_TToCMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToCMuTau_Tensor > ${log}/TT_LFV_TToCMuTau_Tensor_skim16pre.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/TT_LFV_TToUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToUMuTau_Tensor > ${log}/TT_LFV_TToUMuTau_Tensor_skim16pre.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16pre ${mcdir}/TT_LFV_TToUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToUMuTau_Vector > ${log}/TT_LFV_TToUMuTau_Vector_skim16pre.out
#
#mcdir=/data1/common/NanoAOD/v9/mc/RunIISummer20UL16NanoAODv9
#./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/ST_LFV_TCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TCMuTau_Scalar > ${log}/ST_LFV_TCMuTau_Scalar_skim16post.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/ST_LFV_TCMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TCMuTau_Tensor > ${log}/ST_LFV_TCMuTau_Tensor_skim16post.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/ST_LFV_TCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TCMuTau_Vector > ${log}/ST_LFV_TCMuTau_Vector_skim16post.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/ST_LFV_TUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TUMuTau_Scalar > ${log}/ST_LFV_TUMuTau_Scalar_skim16post.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/ST_LFV_TUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TUMuTau_Tensor > ${log}/ST_LFV_TUMuTau_Tensor_skim16post.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/ST_LFV_TUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8   ${tgdir}/ST_LFV_TUMuTau_Vector > ${log}/ST_LFV_TUMuTau_Vector_skim16post.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/TT_LFV_TToCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToCMuTau_Scalar > ${log}/TT_LFV_TToCMuTau_Scalar_skim16post.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/TT_LFV_TToCMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToCMuTau_Tensor > ${log}/TT_LFV_TToCMuTau_Tensor_skim16post.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/TT_LFV_TToCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToCMuTau_Vector > ${log}/TT_LFV_TToCMuTau_Vector_skim16post.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/TT_LFV_TToUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToUMuTau_Scalar > ${log}/TT_LFV_TToUMuTau_Scalar_skim16post.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/TT_LFV_TToUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToUMuTau_Tensor > ${log}/TT_LFV_TToUMuTau_Tensor_skim16post.out
#./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir}/TT_LFV_TToUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8 ${tgdir}/TT_LFV_TToUMuTau_Vector > ${log}/TT_LFV_TToUMuTau_Vector_skim16post.out
#
#mcdir=/data1/common/NanoAOD/v9/mc/RunIISummer20UL17NanoAODv9
#./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/ST_LFV_TCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8       ${tgdir}/ST_LFV_TCMuTau_Scalar > ${log}/ST_LFV_TCMuTau_Scalar_skim17.out
#./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/ST_LFV_TCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8       ${tgdir}/ST_LFV_TCMuTau_Vector > ${log}/ST_LFV_TCMuTau_Vector_skim17.out
#./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/TT_LFV_TToCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToCMuTau_Scalar > ${log}/TT_LFV_TToCMuTau_Scalar_skim17.out
#./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/TT_LFV_TToCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToCMuTau_Vector > ${log}/TT_LFV_TToCMuTau_Vector_skim17.out
#./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/TT_LFV_TToUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToUMuTau_Vector > ${log}/TT_LFV_TToUMuTau_Vector_skim17.out
#./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/TT_LFV_TToUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToUMuTau_Tensor > ${log}/TT_LFV_TToUMuTau_Tensor_skim17.out
#./skimnanoaod.py -F --split ${njobs} -Y skim17 ${mcdir}/TT_LFV_TToUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToUMuTau_Vector > ${log}/TT_LFV_TToUMuTau_Vector_skim17.out
#
#mcdir=/data1/common/NanoAOD/v9/mc/RunIISummer20UL18NanoAODv9
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/ST_LFV_TCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8       ${tgdir}/ST_LFV_TCMuTau_Scalar > ${log}/ST_LFV_TCMuTau_Scalar_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/ST_LFV_TCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8       ${tgdir}/ST_LFV_TCMuTau_Vector > ${log}/ST_LFV_TCMuTau_Vector_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/ST_LFV_TUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8       ${tgdir}/ST_LFV_TCMuTau_Scalar > ${log}/ST_LFV_TCMuTau_Scalar_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/TT_LFV_TToCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToCMuTau_Scalar > ${log}/TT_LFV_TToCMuTau_Scalar_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/TT_LFV_TToCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToCMuTau_Vector > ${log}/TT_LFV_TToCMuTau_Vector_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/TT_LFV_TToUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToUMuTau_Scalar > ${log}/TT_LFV_TToUMuTau_Scalar_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/TT_LFV_TToUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8     ${tgdir}/TT_LFV_TToUMuTau_Tensor > ${log}/TT_LFV_TToUMuTau_Tensor_skim18.out
