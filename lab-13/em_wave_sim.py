# GlowScript 3.2 VPython
# Lab 13 – Interactive EM wave simulation (E, B, Poynting vector, polarization)
#
# Local version: pip install vpython ; python3 em_wave_sim.py
# For glowscript.org use em_wave_glowscript.py (same code, GlowScript header).
#
# Units: arbitrary display units with c = 1 (so B0 = E0/c = E0 and B is visible).
# In real SI units B0 = E0/c ~ 3e-9 E0, and omega = 2*pi*c/lambda is so large that
# one animation frame would skip millions of radians (aliasing), so the lab sheet's
# c = 3e8 cannot be animated directly. The geometry and phase relations are identical.
from vpython import *

# ------------------------------------------------------------ parameters
c = 1.0                 # speed of wave in display units
E0 = 1.0                # E amplitude
B0 = E0 / c             # B amplitude, from |E| = c|B|
lam = 2.0               # wavelength (changed by slider)
N = 41                  # sample points along the propagation axis
dz = 0.2                # spacing between sample points
dt = 0.02               # time step per frame

mode = 'Linear (x)'     # polarization
direction = 1           # +1 : wave travels along +z, -1 : along -z
running = True
front_view = False      # True while looking along the z axis
show_E = True
show_B = True
show_S = True
wt = 0.0                # accumulated omega*t, so changing lambda does not make the wave jump

# ------------------------------------------------------------ scene
scene.title = "EM wave: E (red), B (blue), S = E x B (green), propagation axis z (gray)"
scene.width = 900
scene.height = 540
scene.background = color.white
scene.center = vec(0, 0, (N - 1) * dz / 2)
scene.range = 4.2
scene.forward = vec(-0.6, -0.35, -0.75)
scene.up = vec(0, 1, 0)

L = (N - 1) * dz        # length of the sampled wave (8 = 4 wavelengths for lambda = 2)
# axes: x = E direction, y = B direction (for linear-x), z = propagation (gray, so green is only S)
arrow(pos=vec(0, 0, 0), axis=vec(1.6, 0, 0), color=color.red, shaftwidth=0.03)
arrow(pos=vec(0, 0, 0), axis=vec(0, 1.6, 0), color=color.blue, shaftwidth=0.03)
arrow(pos=vec(0, 0, 0), axis=vec(0, 0, L + 0.6), color=color.gray(0.45), shaftwidth=0.02)
label(pos=vec(1.8, 0, 0), text="x", box=False, color=color.red, height=14)
label(pos=vec(0, 1.8, 0), text="y", box=False, color=color.blue, height=14)
label(pos=vec(0, 0, L + 0.9), text="z (k)", box=False, color=color.gray(0.3), height=14)

E_arrows = []
B_arrows = []
S_arrows = []
for i in range(N):
    z = i * dz
    E_arrows.append(arrow(pos=vec(0, 0, z), axis=vec(0, 0, 0), color=color.red,
                          shaftwidth=0.04))
    B_arrows.append(arrow(pos=vec(0, 0, z), axis=vec(0, 0, 0), color=color.blue,
                          shaftwidth=0.04))
    S_arrows.append(arrow(pos=vec(0, 0, z), axis=vec(0, 0, 0), color=color.green,
                          shaftwidth=0.08, headwidth=0.22, headlength=0.25))

# curves through the arrow tips make the sinusoid easy to see
E_curve = curve(color=color.red, radius=0.012)
B_curve = curve(color=color.blue, radius=0.012)
for i in range(N):
    E_curve.append(pos=vec(0, 0, i * dz))
    B_curve.append(pos=vec(0, 0, i * dz))

# tip of E at the last sample point with a trail: shows the tip trajectory (line or circle)
tip = sphere(pos=vec(0, 0, L), radius=0.08, color=color.orange,
             make_trail=True, retain=120, trail_radius=0.02)

# ------------------------------------------------------------ physics
def E_components(phase):
    # (Ex, Ey) of the electric field for the selected polarization
    if mode == 'Linear (x)':
        return E0 * cos(phase), 0.0
    if mode == 'Linear (y)':
        return 0.0, E0 * cos(phase)
    if mode == 'Circular RH':
        return E0 * cos(phase), E0 * sin(phase)
    return E0 * cos(phase), -E0 * sin(phase)          # Circular LH


def B_from_E(Ex, Ey):
    # B = (k_hat x E) / c with k_hat = direction * z_hat -> (-Ey, Ex, 0) * direction / c
    return -direction * Ey / c, direction * Ex / c, 0.0


# ------------------------------------------------------------ controls
def set_mode(m):
    global mode
    mode = m.selected
    tip.clear_trail()
    update_info()


def set_dir(m):
    global direction
    global wt
    new_direction = 1 if m.selected == '+z' else -1
    if new_direction != direction:
        wt = -wt            # keeps phase = k z - direction * wt unchanged, so the wave does not jump
    direction = new_direction
    if front_view:
        view_front(None)    # stay facing the oncoming wave
    tip.clear_trail()
    update_info()


def toggle_run(b):
    global running
    running = not running
    b.text = "Pause" if running else "Run"


def set_lam(s):
    global lam
    lam = s.value
    update_info()


def toggle_E(cb):
    global show_E
    show_E = cb.checked


def toggle_B(cb):
    global show_B
    show_B = cb.checked


def toggle_S(cb):
    global show_S
    show_S = cb.checked


def view_3d(b):
    global front_view
    front_view = False
    scene.forward = vec(-0.6, -0.35, -0.75)
    scene.up = vec(0, 1, 0)


def view_front(b):
    # look along the z axis facing the oncoming wave: from +z for a +z wave, from -z for a -z wave
    # (seen this way RH turns clockwise and LH counter-clockwise, optics convention)
    global front_view
    front_view = True
    scene.forward = vec(0, 0, -direction)
    scene.up = vec(0, 1, 0)


scene.append_to_caption("\n")
button(text="Pause", bind=toggle_run)
scene.append_to_caption("  Polarization: ")
menu(choices=['Linear (x)', 'Linear (y)', 'Circular RH', 'Circular LH'],
     index=0, bind=set_mode)
scene.append_to_caption("  Propagation: ")
menu(choices=['+z', '-z'], index=0, bind=set_dir)
scene.append_to_caption("\n\nWavelength: ")
slider(min=1.0, max=4.0, value=lam, length=240, bind=set_lam)
scene.append_to_caption("\n\nShow: ")
checkbox(text="E ", checked=True, bind=toggle_E)
checkbox(text="B ", checked=True, bind=toggle_B)
checkbox(text="S ", checked=True, bind=toggle_S)
scene.append_to_caption("   View: ")
button(text="3D", bind=view_3d)
button(text="Face the wave", bind=view_front)
scene.append_to_caption("\n\n")
info = wtext(text="")


def fmt(x):
    # 3 decimal places; plain round() works in both GlowScript and Python
    return str(round(x * 1000) / 1000)


def update_info():
    k = 2 * pi / lam
    f = c / lam
    omega = 2 * pi * f
    info.text = ("<b>" + mode + ", travelling along " + ("+z" if direction == 1 else "-z") + "</b><br>"
                 + "lambda = " + fmt(lam) + ",  k = 2pi/lambda = " + fmt(k)
                 + ",  f = c/lambda = " + fmt(f)
                 + ",  omega = 2pi f = " + fmt(omega)
                 + ",  T = " + fmt(1 / f) + "<br>"
                 + "S length is proportional to |E x B|: it pulses for linear polarization "
                 + "and stays constant for circular.")


update_info()

# ------------------------------------------------------------ main loop
while True:
    rate(50)
    k = 2 * pi / lam
    omega = c * k                       # c = lambda * f  ->  omega = c k
    if running:
        wt += omega * dt
    # redraw even while paused, so the checkboxes, menus and views still respond
    E_curve.visible = show_E
    B_curve.visible = show_B
    for i in range(N):
        z = i * dz
        phase = k * z - direction * wt
        Ex, Ey = E_components(phase)
        Bx, By, Bz = B_from_E(Ex, Ey)
        Ev = vec(Ex, Ey, 0)
        Bv = vec(Bx, By, 0)
        S = cross(Ev, Bv)               # proportional to the Poynting vector (1/mu0 dropped)

        E_arrows[i].axis = Ev if show_E else vec(0, 0, 0)
        B_arrows[i].axis = Bv if show_B else vec(0, 0, 0)
        # S is drawn at every 4th point only, so the arrows along z do not overlap
        S_arrows[i].axis = vec(0, 0, 0.7 * S.z) if (show_S and i % 4 == 0) else vec(0, 0, 0)

        E_curve.modify(i, pos=vec(Ex, Ey, z))
        B_curve.modify(i, pos=vec(Bx, By, z))
        if i == N - 1:
            tip.pos = vec(Ex, Ey, z)
