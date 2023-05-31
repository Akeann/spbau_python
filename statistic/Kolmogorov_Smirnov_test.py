import pandas
import matplotlib.pyplot as plt
from scipy import stats

df = pandas.read_csv("resistance.csv")
# Замеры сопротивления набора резисторов с одинаковым номинальным сопротивлением.

df.plot.kde()
plt.show()
print(stats.kstest(df['resistance'], 'norm', (df['resistance'].mean(), df['resistance'].std()), N=5000))
