Web VPython 3.2
# SCI-103 Lab 13 - Part A: Visualizing an EM wave with animated arrows
# How to run: glowscript.org -> Create New Program -> delete everything in the
# editor -> paste this whole file -> Run   (line 1 must stay "Web VPython 3.2")
#
# Plane wave travelling along +z in free space:
#   E(z,t) = E0 cos(kz - wt) x_hat        B(z,t) = B0 cos(kz - wt) y_hat
#
# The wave uses the same SI values as the lab sheet (c = 3e8 m/s, lambda = 2 m).
# Only two display settings are different from the lab-sheet code:
#   1) B arrows are drawn c times longer: B0 = 3.33e-9 T is far too short to see.
#   2) dt = T/100 (1/100 of a period): with dt = 0.02 s the wave moves exactly
#      3,000,000 periods per frame, so every frame looks the same.

# ---------------- wave parameters (SI units) ----------------
c = 3e8                 # speed of light (m/s)
lam = 2.0               # wavelength (m)
f = c / lam             # frequency (Hz)          = 1.5e8 Hz
omega = 2 * pi * f      # angular frequency (rad/s)
k = 2 * pi / lam        # wave number (rad/m)     = pi rad/m
T = 1 / f               # period (s)              = 6.67e-9 s
E0 = 1.0                # amplitude of E (V/m)
B0 = E0 / c             # amplitude of B (T), from E = cB  -> 3.33e-9 T

# ---------------- display settings ----------------
B_scale = c             # B arrow length = c*B  (3.33e-9 T is drawn as long as 1 V/m)
dt = T / 100            # time step: 100 frames per period (slow motion)
N = 41                  # number of sample points along z
dz = 0.1                # spacing of sample points (m) -> z = 0 ... 4 m = 2 wavelengths
L = (N - 1) * dz

scene.title = "<b>Part A</b> - EM wave travelling along +z:  red = <b>E</b>,  blue = <b>B</b> (drawn as c<b>B</b>)"
scene.width = 900
scene.height = 450
scene.background = color.white
scene.center = vec(0, 0, L / 2)
scene.forward = vec(-1, -0.5, -1.2)
scene.range = 2.4

# axes: x = direction of E (red), y = direction of B (blue), z = propagation k (gray)
arrow(pos=vec(0, 0, 0), axis=vec(1.4, 0, 0), color=color.red, shaftwidth=0.02)
arrow(pos=vec(0, 0, 0), axis=vec(0, 1.4, 0), color=color.blue, shaftwidth=0.02)
arrow(pos=vec(0, 0, 0), axis=vec(0, 0, L + 0.5), color=color.gray(0.5), shaftwidth=0.02,
      headwidth=0.06, headlength=0.12)
label(pos=vec(1.55, 0, 0), text="x", box=False, color=color.red)
label(pos=vec(0, 1.55, 0), text="y", box=False, color=color.blue)
label(pos=vec(0, 0, L + 0.7), text="z (k)", box=False, color=color.gray(0.3))

# one E arrow and one B arrow at every sample point
E_arrows = []
B_arrows = []
for i in range(N):
    z = i * dz
    E_arrows.append(arrow(pos=vec(0, 0, z), axis=vec(0, 0, 0), color=color.red, shaftwidth=0.02))
    B_arrows.append(arrow(pos=vec(0, 0, z), axis=vec(0, 0, 0), color=color.blue, shaftwidth=0.02))

# thin curves through the arrow tips make the wave shape easy to see
E_curve = curve(color=color.red, radius=0.005)
B_curve = curve(color=color.blue, radius=0.005)
for i in range(N):
    E_curve.append(vec(0, 0, i * dz))
    B_curve.append(vec(0, 0, i * dz))

# ---------------- controls and graph ----------------
running = True

def toggle_run(b):
    global running
    running = not running
    b.text = "Pause" if running else "Run"

scene.append_to_caption("\n")
button(text="Pause", bind=toggle_run)
scene.append_to_caption("\n\n")
info = wtext(text="")
scene.append_to_caption("\n")

# E and B at the point z = 0 for the first 3 periods: are they in phase?
g = graph(title="Fields at z = 0 m", xtitle="t (ns)", ytitle="Ex (V/m),  By (nT)",
          width=900, height=260, xmin=0, xmax=3 * T * 1e9)
gE = gcurve(graph=g, color=color.red, label="Ex (V/m)")
gB = gcurve(graph=g, color=color.blue, label="By (nT)")

# ---------------- main loop ----------------
t = 0
while True:
    rate(50)
    if not running:
        continue
    for i in range(N):
        z = i * dz
        phase = k * z - omega * t
        Ex = E0 * cos(phase)
        By = B0 * cos(phase)
        E_arrows[i].axis = vec(Ex, 0, 0)
        B_arrows[i].axis = vec(0, B_scale * By, 0)
        E_curve.modify(i, pos=vec(Ex, 0, z))
        B_curve.modify(i, pos=vec(0, B_scale * By, z))

    # fields at z = 0 (phase = -omega t)
    Ex0 = E0 * cos(-omega * t)
    By0 = B0 * cos(-omega * t)
    if t <= 3 * T:
        gE.plot(t * 1e9, Ex0)
        gB.plot(t * 1e9, By0 * 1e9)
    ratio = "-"
    if abs(By0) > 0.1 * B0:
        ratio = "{:.3e}".format(Ex0 / By0) + " m/s"
    info.text = ("t = " + "{:.2f}".format(t * 1e9) + " ns = " + "{:.2f}".format(t / T) + " T"
                 + "   |   at z = 0:  Ex = " + "{:+.3f}".format(Ex0) + " V/m,  By = "
                 + "{:+.3f}".format(By0 * 1e9) + " nT,  Ex/By = " + ratio
                 + "<br>lambda = " + "{:.1f}".format(lam) + " m,  f = " + "{:.2e}".format(f)
                 + " Hz,  T = " + "{:.3f}".format(T * 1e9) + " ns,  B0 = E0/c = "
                 + "{:.3e}".format(B0) + " T")
    t = t + dt
