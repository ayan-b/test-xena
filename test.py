from __future__ import print_function

import time

from xena_gdc_etl import xena_dataset

# styling stuff
import colorama
colorama.init()
from colorama import Fore, Style
# end


GDC_XENA_COHORT = [
    'TCGA-BRCA', #
    'TCGA-LUAD', #
    'TCGA-UCEC', #
    'TCGA-LGG', #
    'TCGA-HNSC', #
    'TCGA-PRAD', #
    'TCGA-LUSC', #
    'TCGA-THCA', #
    'TCGA-SKCM', #
    'TCGA-OV', #
    'TCGA-STAD', #
    'TCGA-COAD', #
    'TCGA-BLCA', #
    'TCGA-GBM', #
    'TCGA-LIHC', #
    'TCGA-KIRC', #
    'TCGA-CESC', #
    'TCGA-KIRP', #
    'TCGA-SARC', #
    'TCGA-ESCA', #
    'TCGA-PAAD', #
    'TCGA-PCPG', #
    'TCGA-READ', #
    'TCGA-TGCT', #
    'TCGA-LAML', #
    'TCGA-THYM', #
    'TCGA-ACC', #
    'TCGA-MESO', #
    'TCGA-UVM', #
    'TCGA-KICH', #
    'TCGA-UCS', #
    'TCGA-CHOL', #
    'TCGA-DLBC', #
]

TARGET_DATA = [
    "TARGET-NBL", #
    "TARGET-AML", #
    "TARGET-WT", #
    "TARGET-OS", #
    "TARGET-ALL-P3", #
    "TARGET-RT", #
    "TARGET-CCSK", #
]

xena_dtypes = [
    'masked_cnv',  # Masked Copy Number Segment 
    'mirna',  # miRNA Expression Quantification
    'muse_snv',  # MuSE Variant Aggregation and Masking
    'mutect2_snv',  # MuTect2 Variant Aggregation and Masking
    'somaticsniper_snv',  # SomaticSniper Variant Aggregation and Masking
    'varscan2_snv',  # VarScan2 Variant Aggregation and Masking
    'htseq_counts',  # HTSeq - Counts
    'htseq_fpkm',   # HTSeq - FPKM
    'htseq_fpkm-uq',  # HTSeq - FPKM-UQ
    # 'methylation450',  # Illumina Human Methylation 450 
]


import sys
if sys.version_info[0] < 3:
    projects = TARGET_DATA[6]  # TARGET-CCSK
elif sys.version_info[0] == 3 and sys.version_info[1] == 7:
    projects = GDC_XENA_COHORT[-1]  # TCGA-DLBC
elif sys.version_info[0] == 3 and sys.version_info[1] == 6:
    projects = TARGET_DATA[3]  # TARGET-OS
elif sys.version_info[0] == 3 and sys.version_info[1] == 5:
    projects = TARGET_DATA[5]  # TARGET-RT

# testing code starts here
for xena_dtype in xena_dtypes:
    try:
        start = time.time()
        dataset = xena_dataset.GDCOmicset(
            projects=projects,
            root_dir=r'./test',
            xena_dtype=xena_dtype
        )
        dataset.download().transform().metadata()
        print("Time taken:", int((time.time()-start)//60), "min", round((time.time()-start)%60), "sec")
        print(Fore.GREEN + "Pipeline succeed for {} in {} project".format(xena_dtype, projects))
        print(Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + str(e))
        print(Fore.RED + "Pipeline failed for {} in {} project".format(xena_dtype, projects))
        print(Style.RESET_ALL)
