def kg(p):
    return 2.2*p

import numpy as np
import pandas as pd

pounds = np.arange(0,201, 10)
kg = kg(pounds)

weight_dict = {'x': pounds, 'y': kg}

df = pd.DataFrame.from_dict(weight_dict)
df.head()
df.to_csv('sample_data_2.csv')
