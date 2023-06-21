#strain rate 0.007 at 300K Reax
C300K = np.array(      [[70.81, 35.15, 19.48, 0    , 0    ,     0],
                        [35.45, 73.75, 19.82, 0    , 0    ,     0],
                        [19.48, 23.32, 51.74, 0    , 0    ,     0],
                        [0    , 0    , 0    , 26.33, 0    ,     0],
                        [0    , 0    , 0    , 0    , 18.34,     0],
                        [0    , 0    , 0    , 0    , 0    , 17.52]])





# Calculate the inverse of the matrix

S  = np.linalg.inv(C)
print(S)


# Calculating bulk modulus (Kv and Kr)
Kv = (1 / 9) * (C[0, 0] + C[1, 1] + C[2, 2] + 2 * (C[1, 2] + C[0, 2] + C[0, 1]))
Kr = 1 / (S[0, 0] + S[1, 1] + S[2, 2] + 2 * (S[1, 2] + S[0, 2] + S[0, 1]))

# Calculating shear modulus (Gv and Gr)
Gv = (1 / 15) * (C[0, 0] + C[1, 1] + C[2, 2] + 3 * (C[3, 3] + C[4, 4] + C[5, 5]) - (C[1, 2] + C[0, 2] + C[0, 1]))
Gr = (4 / 15) * (S[0, 0] + S[1, 1] + S[2, 2] + 3 * (S[3, 3] + S[4, 4] + S[5, 5]) - (S[1, 2] + S[0, 2] + S[0, 1]))

# Calculating indentation modulus
M = (4 * Gv * (3 * Kv + Gv)) / (3 * Kv + 4 * Gv)

#Young modulus
E = 9*Gv*Kv/(3*Kv + Gv)

#poisson ratio
nu = (3*Kv - 2*Gv)/(2*(3*Kv + Gv))

# Print the results
print("Bulk modulus (Kv):", Kv)
print("Reciprocal bulk modulus (Kr):", Kr)
print("Shear modulus (Gv):", Gv)
print("Reciprocal shear modulus (Gr):", Gr)
print("Indentation modulus (M):", M)
print("Young Modulus (E):", E)
print("Poisson Ratio (nu):", nu)