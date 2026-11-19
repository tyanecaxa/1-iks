import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 90, 300)
T = 20 + 70*np.exp(-0.05*t)

fig, ax = plt.subplots()
ax.grid(True)

ax.set_xlim(0, 30)
ax.set_ylim(0, 100)
ax.set_xlabel("Минуты")
ax.set_ylabel("Температура, C")
ax.set_title("Чай остывает по закону Ньютона")

ax.plot(t, T, color='lightgrey', alpha=0.2)
line, = ax.plot([],[],color='red',lw=2)
dot, = ax.plot([],[],'ro', ms=9)
tx = ax.text(
    0.05, 0.95, '',
    transform=ax.transAxes,
    verticalalignment='top'
)
ax.axhline(40, ls='--', color='orange')
ax.text(x = 5, y= 43, s='питьевая 40 С', color='orange')

ax.axhline(20, ls='--', color='blue')
ax.text(x=13, y=23, s='комнатная 20 С', color='blue')

def update(frame):
    n = frame + 1
    line.set_data(t[:n], T[:n])

    dot.set_data([t[n-1]], [T[n-1]])

    tx.set_text(
        f't = {t[n-1]:.1f} мин\n'
        f'T = {T[n-1]:.1f} C\n'
    )

    if T[n] < 40:
        ani.event_source.stop() 

    return line, dot, tx

ani = FuncAnimation(fig, update, frames=300, interval=10, blit=False, repeat=False)
plt.show()