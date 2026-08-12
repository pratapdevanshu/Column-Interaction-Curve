# Interaction Curve of RC Column  
## Method-1 : Neutral Axis Stepping Method

### Aim
To generate axial load–moment interaction curve of a reinforced concrete column by varying neutral axis depth ratio \( x_u/D \) using strain compatibility and equilibrium equations.

---

### Given Data

$$
b = 400 \text{ mm}
$$

$$
D = 500 \text{ mm}
$$

$$
f_{ck} = 25 \text{ MPa}
$$

$$
f_y = 415 \text{ MPa}
$$

$$
A_{s1} = A_{s2} = 942.47 \text{ mm}^2
$$

Steel centroid distance from section centroid:

$$
y_1 = -190 \text{ mm}, \qquad
y_2 = +190 \text{ mm}
$$

---

### Theory

Equilibrium equations:

$$
P_u = C_c + C_s
$$

$$
M_u = M_c + M_s
$$

Concrete force:

$$
C_c = 0.362 f_{ck} b x_u
$$

Steel strain:

$$
\varepsilon_s =
0.0035 \frac{x_u - y}{x_u}
$$

Steel stress limited to:

$$
f_s \le 0.87 f_y
$$

---

### Procedure

1. Assume value of ratio  

$$
x_u/D
$$

2. Compute neutral axis depth  

$$
x_u = (x_u/D)\times D
$$

3. Calculate  
- Concrete compressive force  
- Steel forces  
- Resultant axial load  
- Resultant moment  

4. Repeat for increasing values of  

$$
x_u/D
$$

5. Plot  

$$
M_u \text{ vs } P_u
$$

---

### Sample Verification

For  

$$
x_u/D = 0.30
$$

$$
x_u = 150 \text{ mm}
$$

Concrete force:

$$
C_c = 0.362 \times 25 \times 400 \times 150
= 543 \text{ kN}
$$

Program output gives:

$$
P_u \approx 520\text{–}550 \text{ kN}
$$

$$
M_u \approx 240\text{–}260 \text{ kNm}
$$

Hence numerical results are consistent.

---

### Result

Interaction curve obtained shows:

- Pure bending region at low axial load  
- Maximum moment at intermediate axial load  
- Moment reducing at high compression  

---

### Conclusion

Neutral axis stepping method successfully generates interaction curve using strain compatibility principles.  
This method is simple and useful for conceptual understanding of column behaviour.
