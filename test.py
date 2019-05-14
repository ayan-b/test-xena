import time

from xena_gdc_etl import xena_dataset


print('A python module of Xena specific importing pipeline for GDC data.')
start = time.time()
dataset = xena_dataset.GDCOmicset(projects='TCGA-BRCA',
                    root_dir=r'./test',
                    xena_dtype='methylation450')
dataset.download().transform().metadata()
print(time.time()-start)
