#!/bin/bash
version=skim_LFVv8
mc16pre=/data1/common/skimmed_NanoAOD/$version/mc/16pre
mc16post=/data1/common/skimmed_NanoAOD/$version/mc/16post
mc17=/data1/common/skimmed_NanoAOD/$version/mc/17
mc18=/data1/common/skimmed_NanoAOD/$version/mc/18
# Syst : nom, jecup, jecdown, puup, pudown, btagup_jes, btagdown_jes
syst=nom
mkdir -p ${target}
./processonefile.py -Y 18 -S ${syst} --globaltag Summer19UL16APV_V7 /data1/common/skimmed_NanoAOD/skim_LFVv8/mc/18/TTTo2L2Nu/270000_019426EE-3D50-1249-B266-F6DBA0AFE3B5_analyzed.root test_process_mc_TTTo2L2Nu.root outputTree outputTree2 &> test_process_mc_TTTo2L2Nu.out

