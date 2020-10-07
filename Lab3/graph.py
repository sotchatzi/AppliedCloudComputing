import matplotlib
import matplotlib.pyplot as plt

data = {"den":166554,"denna":2926,"denne":736,"det":66192,"han":88262,"hen":3051,"hon":29574,"total":357295}
data2 = {"den":166554/357295,"denna":2926/357295,"denne":736/357295,"det":66192/357295,"han":88262/357295,"hen":3051/357295,"hon":29574/357295}
#data2 = data.get("total")
names = list(data2.keys())
values = list(data2.values())

fig, ax = plt.subplots()
ax.bar(names, values)
plt.xlabel("Pronouns",weight='bold')
plt.ylabel("Normalized Counts",weight='bold')
#fig.ylabel("Gold")
#fig.legend(loc='upper left')

#fig.suptitle('Categorical Plotting')
fig.savefig('test.png')
