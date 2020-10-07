import matplotlib
import matplotlib.pyplot as plt

#X = categorical({'den', 'denna', 'denne', 'det', 'han', 'hen', 'hon'});
#y =             [0.5213,0.0096, 0.0017  ,0.1950,0.2846,0.0133    ,0.1313   ];
#bar(X,y)
#xlabel('\bf Pronoun')
#ylabel('\bf Normalized counts')
#set(gca,'YTick')#(0:0.1:1))
##counts the occurrences of words starting with the same first letter
#ax = gca;
#ax.FontSize = 14;

data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())

fig, ax = plt.plot()
ax.bar(names, values)

fig.suptitle('Categorical Plotting')
fig.savefig('test.png')


