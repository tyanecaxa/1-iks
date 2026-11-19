import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t_stop = 20 * np.log2(1000)
t = np.linspace(0, t_stop, 100)
N = 2 ** (t / 20)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))
ax1.grid(True)

ax1.set_xlim(0, 210)
ax1.set_ylim(0, 1200)
ax1.set_xlabel("Минуты")
ax1.set_ylabel("Бактерии")
ax1.set_title("Обычная шкала: незаметно -> БУМ!")

ax1.plot(t, N, color='greenyellow', alpha=0.2)
line1, = ax1.plot([],[],color='darkolivegreen',lw=2)
dot1, = ax1.plot([],[],'ro', color='darkolivegreen', ms=9)
tx1 = ax1.text(
    0.05, 0.95, '',
    transform=ax1.transAxes,
    verticalalignment='top'
)
ax1.axhline(1000, ls='--', color='red')


ax2.grid(True)

ax2.set_yscale('log')
ax2.set_xlim(0, 210)
ax2.set_ylim(0, 1300)
ax2.set_xlabel("Минуты")
ax2.set_ylabel("Бактерии(log)")
ax2.set_title("Лог-шкала: ровная прямая")

ax2.plot(t, N, color='greenyellow', alpha=0.2)
line2, = ax2.plot([],[],color='darkolivegreen',lw=2)
dot2, = ax2.plot([],[],'ro', color='darkolivegreen', ms=9)
tx2 = ax2.text(
    0.05, 0.95, '',
    transform=ax2.transAxes,
    verticalalignment='top'
)
ax2.axhline(1000, ls='--', color='red')

def update(frame):
    n = frame + 1
    line1.set_data(t[:n], N[:n])
    line2.set_data(t[:n], N[:n])

    dot1.set_data([t[n-1]], [N[n-1]])
    if N[n-1] == 1000:
        dot1.set_color('red')

    dot2.set_data([t[n-1]], [N[n-1]])
    if N[n-1] == 1000:
        dot2.set_color('red')
        ani.event_source.stop() 

    tx1.set_text(
        f't = {t[n-1]:.1f} мин\n'
        f'N = {N[n-1]:.1f}\n'
    )

    tx2.set_text(
            f't = {t[n-1]:.1f} мин\n'
            f'N = {N[n-1]:.1f}\n'
        )

    return line1, line2, dot1, dot2, tx1, tx2

ani = FuncAnimation(fig, update, frames=100, interval=1, blit=False, repeat=False)
fig.tight_layout()
plt.show()