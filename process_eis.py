import pandas as pd
import matplotlib.pyplot as plt


VRMS = 6.61e-3 # VPP for all frequencies = ~21.8mV 

# Import the CSV file as a DataFrame
df = pd.read_csv('eis_0.csv')

# map to vars 
freq = df.iloc[:,0]
irms_A = df.iloc[:,1]
irms_B = df.iloc[:,2]
irms_B = irms_B.mul(1e-6) # compensate for current data recorded in uA

# perform math on df to go from Irms -> impedance
z_A = irms_A.pow(-1).mul(VRMS)
z_B = irms_B.pow(-1).mul(VRMS)



def plot_scatter(): 
    plt.scatter(freq, z_A, marker=".")
    plt.scatter(freq, z_B, marker=".")
    plt.xlabel('frequency (Hz)')
    plt.ylabel('impedance (Ω)')
    plt.xscale('log')
    # plt.yscale('log')
    plt.legend(["18650 25R cell A, OCV 3.491V, SOH ~100%", "18650 25R cell B, OCV 3.444V, SOH ~100%"], loc ="upper right")
    plt.title('Samsung 25R impedance spectra at 25C with 6mV Vrms')


    # Show the plot
    plt.show()


# plot 

plot_scatter()

# # fill NaN's w 0's 
# z_A = z_A.fillna(0)
# z_B = z_B.fillna(0)
# plot_scatter()


plt.scatter(freq, irms_A)
plt.scatter(freq, irms_B)
plt.ylabel('current (A)')
plt.xlabel('frequency (Hz)')
plt.xscale('log')
plt.show()