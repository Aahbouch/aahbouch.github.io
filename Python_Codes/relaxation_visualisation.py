import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import AutoMinorLocator

filename = 'plot_npt_Reax.log.txt'
headers = ['Step','PotEng','Temp','Press','lx','ly','lz','density','vol', 'Pxx', 'Pyy','Pzz','Pxy','Pxz','Pyz' ]
df = pd.read_table(filename, delim_whitespace=True, skiprows=3, names=headers )

print(df.head(10))
# Define missing variables
step = df['Step']
pe = df['PotEng']
press = df['Press']  # Pressure
temp = df['Temp']  # Temperature
#dx = 100*(df['lx']-54.891023 )/54.891023  # Temperature
#dy = 100*(df['ly']-76.012238 )/76.012238
#dz = 100*(df['lz']-45.824082 )/45.824082
#de = 100*(df['density']-2.232396 )/2.232396
#vol = df['vol']
#vol = df['vol']
#vol = df['vol']
#vol = df['vol']

myblue = '#0000FF'
font = {'family': 'serif', 'color':  'darkred', 'weight': 'normal', 'size': 12}
fontsize = 10
mygray = '#000000'

fig = plt.figure(figsize=(24, 4))
ax1 = fig.add_subplot(131)
#ax1.plot(pe, temp, linewidth = 1, color='blue', label='RDF')
#ax1.plot(step/10e3, pe/10e3, linewidth = 1, color='blue', label='Potential energy')
#ax1.plot(step/10e3, press/1e2, linewidth = 1, color='red', label='Pressure')
ax1.plot(step/10e3, df['density'], linewidth = 1, color='red', label='Density')
#ax1.plot(step/10e3, temp, linewidth = 1, color='green', label='Temperature')
#ax1.plot(step/10e3, df['vol'], linewidth = 1, color='blue', label='volume')
ax1.plot(step/10e3, df['lx'], linewidth = 1, color='black', label='Lx')
ax1.plot(step/10e3, df['ly'], linewidth = 1, color='blue', label='Ly')
ax1.plot(step/10e3, df['lz'], linewidth = 1, color='red', label='Lz')
divider = make_axes_locatable(ax1)
ax1.set_xlabel(r'Time(ps)', fontdict=font)
ax1.set_ylabel(r'Value ', fontdict=font)

plt.xticks(fontsize=fontsize)
plt.yticks(fontsize=fontsize)
ax1.minorticks_on()
ax1.tick_params('both', length=6, width=1.5, which='major', direction='in')
ax1.tick_params('both', length=3, width=1, which='minor', direction='in')
ax1.xaxis.set_ticks_position('both')
ax1.yaxis.set_ticks_position('both')
ax1.spines["top"].set_linewidth(1.5)
ax1.spines["bottom"].set_linewidth(1.5)
ax1.spines["left"].set_linewidth(1.5)
ax1.spines["right"].set_linewidth(1.5)
minor_locator_y = AutoMinorLocator(2)
ax1.yaxis.set_minor_locator(minor_locator_y)
minor_locator_x = AutoMinorLocator(2)
ax1.xaxis.set_minor_locator(minor_locator_x)
ax1.xaxis.label.set_color(mygray)
ax1.yaxis.label.set_color(mygray)
ax1.tick_params(axis='x', colors=mygray)
ax1.tick_params(axis='y', colors=mygray)
ax1.spines['left'].set_color(mygray)
ax1.spines['top'].set_color(mygray)
ax1.spines['bottom'].set_color(mygray)
ax1.spines['right'].set_color(mygray)
ax1.tick_params(axis='y', which='both', colors=mygray)
ax1.tick_params(axis='x', which='both', colors=mygray)

ax1.legend(loc='best')  # Add a legend
ax1.grid(True, linestyle='--', color='gray')

fig.tight_layout()
plt.savefig('Lz.png', bbox_inches = 'tight', pad_inches = 0.057,) # transparent=True)