'''
Ahmad Abu Hanifah
A1C020026
Teknik Otomasi Pertanian
'''

import numpy as np
import matplotlib.pyplot as plt

# Inisialisasi parameter sistem
Tsp = 80 # T set poin (yang di inginkan)
R = 500  # Resistansi termal pemanas (ohm)
C = 4186  # Kapasitas termal (J/kg K)
To = 27.0  # Suhu lingkungan (oC)
k = 0.5  # Koefisien perpindahan panas
Vmin = 0 # voltase ketika kontroler off
Vmax = 500 # voltase ketika kontroller on

# Model sistem
def nilai_T(Ti, tn, ti, k, C, V):
    # sistem tangki pemanas (Tn) -> Tn = T(i+1) 
    Tn = Ti + (tn - ti)/C * (((V**2)/R) - (k*(Ti - To)))
    return Tn

time = np.linspace(1, 1000, 100)
Tactual = np.zeros(time.size)
Tsetp = np.zeros(time.size)
i = 0
T0 = 50
Ti = T0
Tn = T0
Tsetp[:] = Tsp

print("time", "error", "V", "T aktual")
for t in time:
    Ti = Tn
    # menghotung error
    err = Ti - Tsp
    # kontroller OnOff
    if err < 0:
        V = Vmax # pemanas hidup -> On
    else:
        V = Vmin # pemanas mati -> Off
    if i == 0:
        ti = 0

    # Hitung respon sistem
    Tn = nilai_T(Ti, t, ti, k, C, V)
    ti = t
    print(t, err, V, Tn)
    Tactual[i] = Tn
    # perulangan waktu selesai dan kembali ke atas
    i = i + 1

# Plot hasil simulasi
plt.title("Simulasi Sistem Kontrol On-Off")
plt.xlabel("Waktu (s)")
plt.ylabel("Suhu (C)")
plt.plot(time, Tactual, "-b", label="T Aktual")
plt.plot(time, Tsetp, "--r", label="T Set-point")
plt.legend(loc="lower right", frameon=False)
plt.show()
    
