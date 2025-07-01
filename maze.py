import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig = plt.figure(figsize=(5, 5))
ax = plt.gca()
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
plt.plot([2, 3], [1, 1], color = 'red', linewidth = 2)
plt.plot([0, 1], [1, 1], color = 'red', linewidth = 2)
plt.plot([1, 1], [1, 2], color = 'red', linewidth = 2)
plt.plot([1, 2], [2, 2], color = 'red', linewidth = 2)

plt.text(0.5, 2.5, 'S0', size = 14, ha = 'center')
plt.text(1.5, 2.5, 'S1', size = 14, ha = 'center')
plt.text(2.5, 2.5, 'S2', size = 14, ha = 'center')
plt.text(0.5, 1.5, 'S3', size = 14, ha = 'center')
plt.text(1.5, 1.5, 'S4', size = 14, ha = 'center')
plt.text(2.5, 1.5, 'S5', size = 14, ha = 'center')
plt.text(0.5, 0.5, 'S6', size = 14, ha = 'center')
plt.text(1.5, 0.5, 'S7', size = 14, ha = 'center')
plt.text(2.5, 0.5, 'S8', size = 14, ha = 'center')
plt.text(0.5, 2.3, 'START', ha = 'center')
plt.text(2.5, 0.3, 'GOAL', ha = 'center')

plt.tick_params(axis = 'both', which = 'both',
                bottom = False, top = False, right = False, left = False,
                labelbottom = False, labelleft = False)
line, =ax.plot([0.5], [2.5], marker = 'o', color = 'g', markersize = 60)

theta_0 = np.asarray([[np.nan, 1, 1, np.nan],
                      [np.nan, 1, np.nan, 1],
                      [np.nan, np.nan, 1, 1],
                      [1, np.nan, np.nan, np.nan],
                      [np.nan, 1, 1, np.nan],
                      [1, np.nan, np.nan, 1],
                      [np.nan, 1, np.nan, np.nan],
                      [1, 1, np.nan, 1]])
actions = [0, 1, 2, 3]

def cvt_theta_0_to_pi(theta):
    m, n = theta.shape
    pi = np.zeros((m, n))
    for i in range(m):
        pi[i, :] = theta[i, :] / np.nansum(theta[i, :])
    return np.nan_to_num(pi)

pi = cvt_theta_0_to_pi(theta_0)

def step(state, action):
    if action == 0:
        state -=3
    elif action == 1:
        state +=1
    elif action == 2:
        state += 3
    elif action == 3:
        state -= 1
    return state

state = 0
action_history = []
state_history = [0]
while True:
    action = np.random.choice(actions, p = pi[state, :])
    state = step(state, action)
    action_history.append(action)
    state_history.append(state)
    if state == 8:
        break
print(state_history)
#plt.show()

def init():
    line.set_data([], [])
    return (line, )

def animate(i):
    state_ani = state_history[i]
    x = (state_ani % 3) + 0.5
    y = 2.5 - int(state_ani / 3)
    line.set_xdata([x,])
    line.set_ydata([y,])
    return (line, )

anim = animation.FuncAnimation(fig, animate, init_func=init, frames = len(state_history), interval = 200, repeat = False)
anim.save('maze_0.mp4')
