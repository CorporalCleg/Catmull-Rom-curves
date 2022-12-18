import matplotlib.pyplot as plt
import numpy as np

def matrix_gen(t):
    mt = np.zeros((t.size, 4))
    for i in range(t.size):
        for j in range(4):
            mt[i][j] = t[i]**(3-j)
    return mt

def calc_curve_part(p):#построение элементарной кривой Катмулла-Рэма
    t = np.linspace(0, 1, 10)
    m = 0.5 * np.array([(-1, 3, -3, 1), (2, -5, 4, -1), (-1, 0, 1, 0), (0, 2, 0, 0)])
    a = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 0)])
    p = np.dot(np.transpose(p), a)
    r = np.transpose(np.dot(matrix_gen(t), np.dot(m,p)))
    return r

def get_curve(p):#простроение кривой Катмулла-Рэма по всем точкам
    c0 = calc_curve_part(p[0:3, 0:(0 + 4)])
    for i in range(1, int(p.size/3-3)):
        tmp = p[0:3, i:(i+4)]
        c = calc_curve_part(tmp)
        c0 = np.hstack([c0, c])
    return c0

p = 10 * np.random.rand(3, 6)#генерация точек, по которым строится кривая

r = get_curve(p)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(r[0],r[1], r[2], color="violet")
ax.plot(p[0],p[1], 0, color="yellow", marker = "o")
plt.show()

