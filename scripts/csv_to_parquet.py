import pandas as pd

df = pd.read_csv('../data/raw/sales_data.tsv', sep='\t')

df.to_parquet('../data/raw/sales_data.parquet')