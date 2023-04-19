'''
Ahmad Abu Hanifah
A1C020026
Teknik Otomasi Pertanaian
'''

import numpy as np
import matplotlib.pyplot as plt

dOsp = 6.5
vmin = 0 # kecepatan aliran udara (L/s)
vmax = 2 # kecepatan aliran udara (L/s)
V = 1000000 #Volume sistem (L)
kLa = 0.045 # per menit
n = 4 # Jumlah aerator
# a = 0.4 # Luas permukaan antarmuka udara-air (m2/liter)
a = 400 # Luas permukaan kolam (m2)

def NilaidO(dOi, tn, ti, ):
    dOn = dOi + (tn-ti)*((v*n*a*2.5)/V-(kLa/60)*dOi)
    return dOn

time = np.linspace(1, 3000, 100)
dOact = np.zeros(time.size)
dOsetp = np.zeros(time.size)
i = 0
dO0 = 3
dOi = dO0
dOn = dO0
dOsetp[:] = dOsp

print("time", "error", "v", "DO aktual")
for t in time:
    dOi = dOn
    # menghitung error
    err = dOi - dOsp
    # kontroller OnOff
    if err < 0:
        v = vmax # pemanas hidup -> On
    else:
        v = vmin # pemanas mati -> Off
    if i == 0:
        ti = 0

    # Hitung respon sistem
    dOn = NilaidO(dOi, t, ti)
    ti = t
    print(f"{t}, {err}, {v}, {dOn}")
    dOact[i] = dOn
    # perulangan waktu selesai dan kembali ke atas
    i = i + 1

# Plot hasil simulasi
plt.title("Simulasi Sistem Kontrol On-Off")
plt.xlabel("Waktu (s)")
plt.ylabel("DO (mg/L)")
plt.plot(time, dOact, "-b", label="DO Aktual")
plt.plot(time, dOsetp, "--r", label="DO Set-point")
plt.legend(loc="lower right", frameon=False)
plt.show()
