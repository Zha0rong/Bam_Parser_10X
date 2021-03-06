# Bam_Parser_10X
 One script to parse 10x bam files and output fastq files.
## Input
 Bam files from Cellranger
## Output
 outputname_Read1.fastq.gz: Cell barcodes and UMI
 outputname_Read2.fastq.gz: Sequence
## How to use:
 in the script replace the 'test_input/Donor1OC_subset.bam' with the bam location, replace the 'test_output/Donor1OC_subset' with the outputname.
## Test file source:
 Single Nuclei sequencing (10X V3) from the paper Distinct amyloid-β and tau-associated microglia profiles in Alzheimer's disease https://link.springer.com/article/10.1007/s00401-021-02263-w
 
 Sample information: Donor1OC
 https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM4483339
## Issues:
 Caveat: the subprocess function used in the script may be broken in python 3.7.x.
