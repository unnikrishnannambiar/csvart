import pandas_datareader.data as web
import pandas as pd 
import numpy as np 
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.family'] = 'Helvetica'
S = pd.DataFrame()
Tickers = ['SBIN.NS', 'TCS.NS', 'INFY.NS', 'TORNTPHARM.NS']

start = datetime(2016, 9, 1)
end = datetime(2019, 9, 1)
start1 = '2019-09-01'
end1 = '2020-09-01'

for t in Tickers:
  S[t] = web.DataReader(t, 'yahoo', start, end)['Close']

mean = S.max()

val = []

for i in range(len(mean)):
    val.append((mean.values[i], mean.index[i]))

val.sort()
val = val[::-1]

num_shades = len(val) + 1
pal = sns.color_palette(sns.cubehelix_palette(num_shades, rot=-float(str(np.random.random())[1:3])))
col = pal.as_hex()
col = pal.as_hex()

plt.figure(figsize=(16,9))
# plt.title(text, fontsize = 'xx-large', fontweight = 'bold')
plt.fill_between(S[val[0][1]].index,S[val[0][1]].max(), color = str(col[0]))
plt.scatter(S.index[int(len(S) * np.random.random())],S[val[1][1]].max(), marker = "o", s = ((1+1)**4)*50, alpha = 0.3, color = col[-2])
for temp in range(len(val)):
    i = val[temp][1]
    plt.fill_between(S[i].index,S[i], color = str(col[temp + 1]))
    # plt.legend(fontsize = 'xx-large')
plt.savefig(i + '.png')