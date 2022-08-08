import pandas as pd
# df =  pd.read_fwf("./hct36.txt",  header=None, index_col=0)
df = pd.read_csv("./hct36.txt", sep=" ", header=None)
print(df)
pass