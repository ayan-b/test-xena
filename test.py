import time

from xena_gdc_etl import xena_dataset

# styling stuff
import colorama
colorama.init()
from colorama import Fore, Style
# end


GDC_XENA_COHORT = {
        'TCGA-BRCA': 'GDC TCGA Breast Cancer (BRCA)',
        'TCGA-LUAD': 'GDC TCGA Lung Adenocarcinoma (LUAD)',
        'TCGA-UCEC': 'GDC TCGA Endometrioid Cancer (UCEC)',
        'TCGA-LGG': 'GDC TCGA Lower Grade Glioma (LGG)',
        'TCGA-HNSC': 'GDC TCGA Head and Neck Cancer (HNSC)',
        'TCGA-PRAD': 'GDC TCGA Prostate Cancer (PRAD)',
        'TCGA-LUSC': 'GDC TCGA Lung Squamous Cell Carcinoma (LUSC)',
        'TCGA-THCA': 'GDC TCGA Thyroid Cancer (THCA)',
        'TCGA-SKCM': 'GDC TCGA Melanoma (SKCM)',
        'TCGA-OV': 'GDC TCGA Ovarian Cancer (OV)',
        'TCGA-STAD': 'GDC TCGA Stomach Cancer (STAD)',
        'TCGA-COAD': 'GDC TCGA Colon Cancer (COAD)',
        'TCGA-BLCA': 'GDC TCGA Bladder Cancer (BLCA)',
        'TCGA-GBM': 'GDC TCGA Glioblastoma (GBM)',
        'TCGA-LIHC': 'GDC TCGA Liver Cancer (LIHC)',
        'TCGA-KIRC': 'GDC TCGA Kidney Clear Cell Carcinoma (KIRC)',
        'TCGA-CESC': 'GDC TCGA Cervical Cancer (CESC)',
        'TCGA-KIRP': 'GDC TCGA Kidney Papillary Cell Carcinoma (KIRP)',
        'TCGA-SARC': 'GDC TCGA Sarcoma (SARC)',
        'TCGA-ESCA': 'GDC TCGA Esophageal Cancer (ESCA)',
        'TCGA-PAAD': 'GDC TCGA Pancreatic Cancer (PAAD)',
        'TCGA-PCPG': 'GDC TCGA Pheochromocytoma & Paraganglioma (PCPG)',
        'TCGA-READ': 'GDC TCGA Rectal Cancer (READ)',
        'TCGA-TGCT': 'GDC TCGA Testicular Cancer (TGCT)',
        'TCGA-LAML': 'GDC TCGA Acute Myeloid Leukemia (LAML)',
        'TCGA-THYM': 'GDC TCGA Thymoma (THYM)',
        'TCGA-ACC': 'GDC TCGA Adrenocortical Cancer (ACC)',
        'TCGA-MESO': 'GDC TCGA Mesothelioma (MESO)',
        'TCGA-UVM': 'GDC TCGA Ocular melanomas (UVM)',
        'TCGA-KICH': 'GDC TCGA Kidney Chromophobe (KICH)',
        'TCGA-UCS': 'GDC TCGA Uterine Carcinosarcoma (UCS)',
        'TCGA-CHOL': 'GDC TCGA Bile Duct Cancer (CHOL)',
        'TCGA-DLBC': 'GDC TCGA Large B-cell Lymphoma (DLBC)'
    }


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


# testing code starts here
projects = list(GDC_XENA_COHORT.keys())[7]  # TCGA-THCA
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
        print(Fore.RED + "Pipeline failed for {}".format(xena_dtype))
        print(Style.RESET_ALL)
