import numpy
from scipy.linalg import logm, expm
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

SE_rows = 4
SE_cols = 4
R_rows = 3
R_cols = 3
t_rows = 3
t_cols = 1

def get_rotation_matrix(X):
    rot_mat = [[0 for _ in range(R_cols)] for _ in range(R_rows)]
    rot_mat[0][0], rot_mat[0][1], rot_mat[0][2] = X[0][0], X[0][1], X[0][2]
    rot_mat[1][0], rot_mat[1][1], rot_mat[1][2] = X[1][0], X[1][1], X[1][2]
    rot_mat[2][0], rot_mat[2][1], rot_mat[2][2] = X[2][0], X[2][1], X[2][2]
    return rot_mat

def get_position_vector(X):
    pos_vec = [[0 for _ in range(t_cols)] for _ in range(t_rows)]
    pos_vec[0][0] = X[0][3]
    pos_vec[1][0] = X[1][3]
    pos_vec[2][0] = X[2][3]
    return pos_vec

def homogenize(t, R):
    res_mat = [[0 for _ in range(SE_cols)] for _ in range(SE_rows)]
    res_mat[0][0], res_mat[0][1], res_mat[0][2], res_mat[0][3] = R[0][0], R[0][1], R[0][2], t[0][0]
    res_mat[1][0], res_mat[1][1], res_mat[1][2], res_mat[1][3] = R[1][0], R[1][1], R[1][2], t[1][0]
    res_mat[2][0], res_mat[2][1], res_mat[2][2], res_mat[2][3] = R[2][0], R[2][1], R[2][2], t[2][0]
    res_mat[3][0], res_mat[3][1], res_mat[3][2], res_mat[3][3] = 0, 0, 0, 1
    return res_mat

#return the homogeneous representation after the group multiplication
def group_multiply(X, Y):
    X_R = get_rotation_matrix(X)
    X_t = get_position_vector(X)
    Y_R = get_rotation_matrix(Y)
    Y_t = get_position_vector(Y)
    return homogenize(numpy.add(X_t, Y_t), numpy.dot(X_R, Y_R))

def gamma(t):
    X_0 = [[0 for _ in range(SE_cols)] for _ in range(SE_rows)]
    X_0[0][0], X_0[0][1], X_0[0][2], X_0[0][3] = 0.4330, 0.1768, 0.8839, 1
    X_0[1][0], X_0[1][1], X_0[1][2], X_0[1][3] = 0.2500, 0.9186, -0.3062, 1
    X_0[2][0], X_0[2][1], X_0[2][2], X_0[2][3] = -0.8660, 0.3536, 0.3536, 0
    X_0[3][0], X_0[3][1], X_0[3][2], X_0[3][3] = 0, 0, 0, 1

    X_1 = [[0 for _ in range(SE_cols)] for _ in range(SE_rows)]
    X_1[0][0], X_1[0][1], X_1[0][2], X_1[0][3] = 0.7500, -0.0474, 0.6597, 2
    X_1[1][0], X_1[1][1], X_1[1][2], X_1[1][3] = 0.4330, 0.7891, -0.4356, 4
    X_1[2][0], X_1[2][1], X_1[2][2], X_1[2][3] = -0.5000, 0.6124, 0.6124, 3
    X_1[3][0], X_1[3][1], X_1[3][2], X_1[3][3] = 0, 0, 0, 1

    X_0_inv = numpy.linalg.inv(X_0)
    point = group_multiply(X_0, expm(t*logm(group_multiply(X_0_inv, X_1))))
    return point

#plot gamma from start to end inclusive
def plot_gamma(start, end):
    xline = []
    yline = []
    zline = []
    for i in range(start, end+1):
        xline.append(get_position_vector(gamma(i))[0][0])
        yline.append(get_position_vector(gamma(i))[1][0])
        zline.append(get_position_vector(gamma(i))[2][0])

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(xline, yline, zline)
    plt.show()
