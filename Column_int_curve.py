import numpy as np
import matplotlib.pyplot as plt

# ---------------- Input ----------------
b = float(input("Width of column (mm) = "))
D = float(input("Depth of column (mm) = "))
As_1 = float(input("Area of steel left As1 (mm2) = "))
As_2 = float(input("Area of steel right As2 (mm2) = "))
y_1 = float(input("Distance of As1 from centroid (+right , -left) mm = "))
y_2 = float(input("Distance of As2 from centroid (+right , -left) mm = "))
fck = float(input("fck (MPa) = "))
fy = float(input("fy (MPa) = "))

Es = 2e5

Pu_list = []
Mu_list = []
xud_list = []

# ------------ LOOP ON xu/D -------------
for ratio in np.arange(0.01, 1.5, 0.02):

    xu = ratio * D

    # ---------- Concrete Force ----------
    if xu <= D:
        Cc = 0.362 * fck * b * xu
        x_bar = 0.416 * xu
    else:
        g = 16 / (7 * (ratio - 3))**2
        Cc = 0.447 * (1 - 4 * g / 21) * fck * b * D
        x_bar = (0.5 - 8 * g / 49) * D / (1 - 4 * g / 21)

    Mc = Cc * (D/2 - x_bar)

    # ---------- Steel Strain ----------
    if xu <= D:
        es1 = 0.0035 * (xu - (D/2 - y_1)) / xu
        es2 = 0.0035 * (xu - (D/2 - y_2)) / xu
    else:
        es1 = 0.002 * (1 + (y_1 - D/14) / xu - 3*D/(7*xu))
        es2 = 0.002 * (1 + (y_2 - D/14) / xu - 3*D/(7*xu))

    # ---------- Concrete stress at steel level ----------
    def fc(es):
        if es <= 0:
            return 0
        elif es >= 0.002:
            return 0.447 * fck
        else:
            return 0.447 * fck * (2*(es/0.002) - (es/0.002)**2)

    fc1 = fc(es1)
    fc2 = fc(es2)

    # ---------- Steel stress ----------
    fs1 = max(min(Es * es1, 0.87 * fy), -0.87 * fy)
    fs2 = max(min(Es * es2, 0.87 * fy), -0.87 * fy)

    # ---------- Steel Force ----------
    Cs = (fs1 - fc1) * As_1 + (fs2 - fc2) * As_2

    # ---------- Steel Moment ----------
    Ms = (fs1 - fc1) * As_1 * y_1 + (fs2 - fc2) * As_2 * y_2

    # ---------- Resultant ----------
    Pu = Cc + Cs
    Mu = Mc + Ms

    Pu_list.append(Pu / 1000)      # kN
    Mu_list.append(Mu / 1e6)       # kNm
    xud_list.append(ratio)



    # ------------ Plot Interaction Curve ------------
plt.figure()
plt.plot(Mu_list, Pu_list, marker='o')
plt.xlabel("MuR (kNm)")
plt.ylabel("PuR (kN)")
plt.title("Column Interaction Curve")
plt.grid()
plt.show()


