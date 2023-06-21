import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import AutoMinorLocator

# Load the data from a file
fname = "CSH_X_Reax_523.txt"
A = np.loadtxt(fname)
strain = A[:,0]
stress = A[:,1:7]

A = 0   # (0 = x) (1 = y).... (5 = yz)
Stress = stress[:,A]*1.01325

c = "C11_1"


Stress = Stress - Stress[0]

# The Savitzky-Golay filter
window_length = 151  # choose a window length. It should be a positive odd number.
polyorder = 6 # choose a polynomial order. It should be less than window_length.
smoothed_Stress = savgol_filter(Stress, window_length, polyorder)

# Setup figure and plot data
fig = plt.figure(figsize=(18, 4))
ax1 = fig.add_subplot(131)


# plot the data
plt.plot(strain, Stress, 'o', markersize=0.8, label='original data')
ax1.plot(strain, smoothed_Stress, linewidth = 2, color='red', label='Smoothed Stress')

# Set axis labels
ax1.set_xlabel('Strain', fontdict={'size': 14})
ax1.set_ylabel('Stress(GPa)', fontdict={'size': 14})

# Set Sloap
max_strain = strain[np.argmax(smoothed_Stress)]
max_stress = np.max(smoothed_Stress)
max_stress_index = np.argmax(smoothed_Stress)
max_stress_strain = strain[max_stress_index]



# controling the limit of the Y plot
ax1.set_ylim([0, 1.6 * max_stress])


linear_region = np.where(strain < .04)[0]
slope, intercept = np.polyfit(strain[linear_region], smoothed_Stress[linear_region], 1)
ax1.plot(strain[strain <= max_strain], strain[strain <= max_strain] * slope + intercept, '--k', linewidth=1)

residuals = Stress[linear_region] - (slope*strain[linear_region] + intercept)
sum_sq_residuals = np.sum(residuals**2)
y_mean = np.mean(smoothed_Stress[linear_region])
total_ss = np.sum((smoothed_Stress[linear_region] - y_mean)**2)
R2 = 1 - (sum_sq_residuals / total_ss)

# Print the slope,


#plt.text(.1, 0.9, f' {c} = {slope:.2f}\n{c} = {slope:.2f}\nerate = 0.007\ntemp 300k\nReax', transform=ax1.transAxes, fontsize=10, verticalalignment='top')
plt.text(.6, 0.96, f'{c} = {slope:.2f} GPa\nStrain(MaxStress) = {max_stress_strain:.3f} \nMax Stress = {np.max(smoothed_Stress):.2f} GPa\nRate = 0.01\nTemp 523K\nReaxFF- C/S 1.64', transform=ax1.transAxes, fontsize=10, verticalalignment='top')
plt.plot(max_stress_strain, max_stress, 'xk', markersize=7)

plt.hlines(max_stress, 0, max_stress_strain, colors='gray', linestyles='dashed',linewidth=0.5)
plt.vlines(max_stress_strain, 0, max_stress, colors='gray', linestyles='dashed',linewidth=0.5)


# Improve appearance
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

#ax1.legend(loc='best')  # Add a legend
#ax1.grid(True, linestyle='--', color='gray')


fig.tight_layout()
plt.savefig(f'{c}.png', bbox_inches = 'tight', pad_inches = 0.057,) #transparent=True)
plt.show()