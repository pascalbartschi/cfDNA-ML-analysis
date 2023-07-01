#!/bin/bash

for sample in *.bam
do
/mnt/DATA2/cfDNA_finaledb/scripts/hmmcopy_utils/bin/readCounter \
--window 1000000 \
--quality 20 \
--chromosome chr1,chr2,chr3,chr4,chr5,chr6,chr7,chr8,chr9,chr10,chr11,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr20,chr21,chr22,chrX,chrY \
/mnt/DATA1/BME330/A/$sample > /mnt/DATA1/BME330/A/output/"${sample%.*}".wig

Rscript /mnt/DATA2/ichorCNA/scripts/runIchorCNA.R \
--id "${sample%.*}" \
--WIG /mnt/DATA1/BME330/A/output/"${sample%.*}".wig \
--ploidy "c(2)" \
--normal "c(0.5,0.9,0.95, 0.99, 0.995, 0.999)" \
--maxCN 3 \
--gcWig /mnt/DATA2/ichorCNA/inst/extdata/gc_hg38_1000kb.wig \
--mapWig /mnt/DATA2/ichorCNA/inst/extdata/map_hg38_1000kb.wig \
--centromere /mnt/DATA2/ichorCNA/inst/extdata/GRCh38.GCA_000001405.2_centromere_acen.txt \
--normalPanel /mnt/DATA1/BME330/A/pon/pon_median.rds \
--includeHOMD False \
--chrs "c(1:22)" \
--chrTrain "c(1:22)" \
--estimateNormal True \
--estimatePloidy True \
--estimateScPrevalence FALSE \
--scStates "c()" \
--txnE 0.9999 \
--txnStrength 10000 \
--outDir/mnt/DATA1/BME330/A/output/"${sample%.*}"/
done

