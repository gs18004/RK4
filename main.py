import decimal
import math


def f(X, Y):
    return decimal.Decimal((-X * Y) / (X * X - 9))


def Y(X):
    return decimal.Decimal(4 / (math.sqrt(X * X - 9)))


h = decimal.Decimal('0.05')
x = []
y = []
x.append(decimal.Decimal('5.00'))
y.append(decimal.Decimal('1.00'))


for i in range(0, 21):

    if i >= 1:
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + h / 2, y[i - 1] + h * k1 / 2)
        k3 = f(x[i - 1] + h / 2, y[i - 1] + h * k2 / 2)
        k4 = f(x[i - 1] + h, y[i - 1] + h * k3)

        x.append(x[i - 1] + h)
        y.append(y[i - 1] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6)

    print("x{} =".format(i), x[i], "  RK4 y{} =".format(i), "%.10f" % y[i], end="")
    print("   참값 y{} =".format(i), "%.10f" % Y(x[i]), end="")
    print("   절대오차 {} =".format(i), "%.10f" % abs(y[i] - Y(x[i])), end="")
    print("   상대오차 {} =".format(i), "%.10f" % (abs(y[i] - Y(x[i])) * 100 / abs(Y(x[i]))), end="")
    print("%")
    
