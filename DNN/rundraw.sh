#!/bin/bash
source draw.sh jan01/STdec_02_norm_20nodes_2layers_s1b1_jan01/ norm
source draw.sh jan01/STdec_02_jecup_20nodes_2layers_s1b1_jan01/ jecup
source draw.sh jan01/STdec_02_jecdown_20nodes_2layers_s1b1_jan01/ jecdown
source draw.sh jan01/STdec_02_puup_20nodes_2layers_s1b1_jan01/ puup
source draw.sh jan01/STdec_02_pudown_20nodes_2layers_s1b1_jan01/ pudown
source draw.sh jan01/STdec_02_btagup_jes_20nodes_2layers_s1b1_jan01/ btagup_jes
source draw.sh jan01/STdec_02_btagdown_jes_20nodes_2layers_s1b1_jan01/ btagdown_jes
source draw.sh jan01/TTdec_02_norm_15nodes_2layers_s1b1_jan01/ norm
source draw.sh jan01/TTdec_02_jecup_15nodes_2layers_s1b1_jan01/ jecup
source draw.sh jan01/TTdec_02_jecdown_15nodes_2layers_s1b1_jan01/ jecdown
source draw.sh jan01/TTdec_02_puup_15nodes_2layers_s1b1_jan01/ puup
source draw.sh jan01/TTdec_02_pudown_15nodes_2layers_s1b1_jan01/ pudown
source draw.sh jan01/TTdec_02_btagup_jes_15nodes_2layers_s1b1_jan01/ btagup_jes
source draw.sh jan01/TTdec_02_btagdown_jes_15nodes_2layers_s1b1_jan01/ btagdown_jes
systs=( btagdown_hf btagdown_jes btagdown_lf btagup_hf btagup_jes btagup_lf jecdown jecup norm pudown puup )
#for syst in "${systs[@]}"; do
#
#
#done
