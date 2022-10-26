import numpy

rows = 4
cols = 4

sP = [[0 for _ in range(cols)] for _ in range(rows)]
sP[0][0], sP[0][1], sP[0][2], sP[0][3] = -1.3840, -0.9608, 1.3250, -1.3140
sP[1][0], sP[1][1], sP[1][2], sP[1][3] = 4.5620, 1.3110, -2.3890, 0.2501
sP[2][0], sP[2][1], sP[2][2], sP[2][3] = -0.1280, -1.6280, 1.7020, -0.7620
sP[3][0], sP[3][1], sP[3][2], sP[3][3] = 1, 1, 1, 1

oP = [[0 for _ in range(cols)] for _ in range(rows)]
oP[0][0], oP[0][1], oP[0][2], oP[0][3] = 2, 0, -1, -1
oP[1][0], oP[1][1], oP[1][2], oP[1][3] = 3, 0, -2, 0
oP[2][0], oP[2][1], oP[2][2], oP[2][3] = -3, -3, 2, -2
oP[3][0], oP[3][1], oP[3][2], oP[3][3] = 1, 1, 1, 1

oP_inv = numpy.linalg.inv(oP)

T = numpy.dot(sP, oP_inv)

print(T)
