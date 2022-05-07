import numpy as np

ndays = 150


##### For lists
def epsB_GaussList(t):
    """
    Return a list of normally distributed values. Depending on the input list of x-values only half-normal values.
    1. compute left half of Normal Distribution
    2. store ndays values into a list
    @deprecated 3. return the t-th value of this list
    3. return the list
    :REQUIREMENTS: dt=1
    :param t: [iterable] index of timepoint
    :return:
    """
    x_halfNormal = np.linspace(-3, 0, ndays)  # list of x values for left half of Normal Distribution
    gauss = lambda xGau, alphaGau, rGau: 1. / (np.sqrt(alphaGau ** np.pi)) * np.exp(
        -alphaGau * np.power((xGau - rGau), 2.))
    gaussList = gauss(x_halfNormal, 1, 0)

    return gaussList


##### For integers
def epsB_GaussInt(t):
    """
    Return a list of normally distributed values. Depending on the input list of x-values only half-normal values.
    1. compute left half of Normal Distribution
    2. store ndays values into a list
    @deprecated 3. return the t-th value of this list
    3. return value from list according to given index
    :REQUIREMENTS: dt=1
    :param t: [iterable] index of timepoint
    :return:
    """
    x_halfNormal = np.linspace(-3, 0, ndays)  # list of x values for left half of Normal Distribution
    gauss = lambda xGau, alphaGau, rGau: 1. / (np.sqrt(alphaGau ** np.pi)) * np.exp(
        -alphaGau * np.power((xGau - rGau), 2.))
    gaussList = gauss(x_halfNormal, 1, 0)
    return gaussList[t]


##### For integers
def epsB_GaussNew(t):
    """
    Return a list of normally distributed values. Depending on the input list of x-values only half-normal values.
    1. compute left half of Normal Distribution
    2. store ndays values into a list
    @deprecated 3. return the t-th value of this list
    3. return value from list according to given index
    :REQUIREMENTS: dt=1
    :param t: [iterable] index of timepoint
    :return:
    """
    #t = [0, 150]
    #tScaled = [-3, 0]/150

    halfNormNew = lambda t: 1. / (np.sqrt(1 ** np.pi)) * np.exp(-1 * np.power((t/ndays)-4, 2.))
    return halfNormNew(t)


def ranger(t):
    a = 0
    b = 150
    c = -3
    d = 0
    y = (t-a) * ((d-c)/(b-a)) + c
    return y

print(ranger(75))
