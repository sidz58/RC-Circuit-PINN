import numpy as np
import matplotlib.pyplot as plt

def make_ramp_adv(time_points, T, t_rise, t_fall, delay, amplitude, last, repetitions):
    '''
    time_points = number of points per time period
    T = time period
    t_rise & t_fall = RATE of rise per unit time and rate for fall respectively
    delay = input delay
    repetitions = how many times you will repeat the input

    Returns: output ramp function (y) and timespace(n) to plot
    '''
    y = []
    n = np.linspace(0, repetitions * T, repetitions * time_points + 1)
    resolution = int(time_points / T)
    rise = t_rise / resolution
    fall = t_fall / resolution
    rise_steps = 0
    
    # delay (zero values)
    for i in range(resolution * delay):
        y.append(0)
    
    # up-ramp values
    for i in range((T - delay) * resolution):
        if rise * i > amplitude:
            break
        y.append(rise * i)
        rise_steps += 1
    
    # amplitude-hold values
    for i in range(last * resolution - rise_steps - int(amplitude // fall) - delay * resolution ):
        y.append(amplitude)
    
    # down-ramp values
    for i in range(int(amplitude // fall)+1):
        y.append(amplitude - fall * i)
    
    # Append zeros to y to match the length of n
    y += [0] * (time_points - len(y))

    y_repeated = y * repetitions
    y_repeated.append(0) #adds one term at the end that makes sure the sizes are matched between n and y_repeated

    return y_repeated, n