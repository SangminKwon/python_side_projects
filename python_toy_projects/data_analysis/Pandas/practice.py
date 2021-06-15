import numpy as np
import pandas as pd

sample_1 = pd.read_excel('C:/Users/admin/Desktop/py_projects/Pandas/sample_1.xlsx' , header=1, skipfooter=2, usecols='A:C', )
print(sample_1.head(3))