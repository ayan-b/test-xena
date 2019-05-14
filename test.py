import time

from xena_gdc_etl import xena_dataset


xena_dtypes = [
    'masked_cnv',  # Masked Copy Number Segment 
    # 'methylation450',  # Illumina Human Methylation 450 
    'mirna',  # miRNA Expression Quantification
    'muse_snv',  # MuSE Variant Aggregation and Masking
    'mutect2_snv',  # MuTect2 Variant Aggregation and Masking
    'somaticsniper_snv',  # SomaticSniper Variant Aggregation and Masking
    'varscan2_snv',  # VarScan2 Variant Aggregation and Masking
    'htseq_counts',  # HTSeq - Counts
    'htseq_fpkm',   # HTSeq - FPKM
    'htseq_fpkm-uq',  # HTSeq - FPKM-UQ
]

print('A python module of Xena specific importing pipeline for GDC data.')
for xena_dtype in xena_dtypes:
    try:
        start = time.time()
        dataset = xena_dataset.GDCOmicset(projects='TCGA-BRCA',
                            root_dir=r'./test',
                            xena_dtype=xena_dtype)
        dataset.download().transform().metadata()
        print(time.time()-start)
    except Exception as e:
        print(e)
        print("Pipeline failed for {}".format(xena_dtype))
