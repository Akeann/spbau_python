import pandas
import matplotlib.pyplot as plt
from scipy import stats

df1 = pandas.read_csv("resistance.csv")
# Замеры сопротивления набора резисторов с одинаковым номинальным сопротивлением.
df = pandas.DataFrame(data={
    'df1': df1['resistance'],
})

df.plot.kde()
plt.show()
print(stats.kstest(df, 'norm', (df.mean(), df.std()), N=5000))

# Распределение крайне похоже на нормальное