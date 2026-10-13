Web VPython 3.2
# SCI-103 Lab 13 - Part B: Poynting vector S = (E x B) / mu0
# How to run: glowscript.org -> Create New Program -> delete everything in the
# editor -> paste this whole file -> Run   (line 1 must stay "Web VPython 3.2")
#
# Same plane wave as Part A (SI values from the lab sheet), plus the energy flow S.
# B is computed from E with  B = (k_hat x E) / c , so the menu "Propagation"
# can send the wave along +z or -z (lab question 5) and S still comes out right.

# ---------------- wave parameters (SI units) ----------------
c = 3e8                 # speed of light (m/s)
mu0 = 4 * pi * 1e-7     # magnetic constant (T m/A)
lam = 2.0               # wavelength (m)
f = c / lam             # frequency (Hz)
omega = 2 * pi * f      # angular frequency (rad/s)
k = 2 * pi / lam        # wave number (rad/m)
T = 1 / f               # period (s)
E0 = 1.0                # amplitude of E (V/m)
B0 = E0 / c             # amplitude of B (T)
S_peak = E0 * B0 / mu0              # largest value of |S| (W/m^2)
S_avg_theory = E0**2 / (2 * mu0 * c)  # intensity <S> from theory (W/m^2)

direction = 1           # +1: wave travels along +z,  -1: along -z

# ---------------- display settings ----------------
B_scale = c             # B arrow length = c*B
S_scale = 0.45 / S_peak # longest S arrow is 0.45 m on the screen
dt = T / 100            # 100 frames per period
N = 41
dz = 0.1                # z = 0 ... 4 m = 2 wavelengths
L = (N - 1) * dz
S_every = 5             # draw S at every 5th point only, so the S arrows do not overlap

scene.title = "<b>Part B</b> - Poynting vector:  red = <b>E</b>,  blue = c<b>B</b>,  green = <b>S</b> = (<b>E</b> x <b>B</b>)/mu0"
scene.width = 900
scene.height = 450
scene.background = color.white
scene.center = vec(0, 0, L / 2)
scene.forward = vec(-1, -0.5, -1.2)
scene.range = 2.4

arrow(pos=vec(0, 0, 0), axis=vec(1.4, 0, 0), color=color.red, shaftwidth=0.02)
arrow(pos=vec(0, 0, 0), axis=vec(0, 1.4, 0), color=color.blue, shaftwidth=0.02)
arrow(pos=vec(0, 0, 0), axis=vec(0, 0, L + 0.5), color=color.gray(0.5), shaftwidth=0.02,
      headwidth=0.06, headlength=0.12)
label(pos=vec(1.55, 0, 0), text="x", box=False, color=color.red)
label(pos=vec(0, 1.55, 0), text="y", box=False, color=color.blue)
label(pos=vec(0, 0, L + 0.7), text="+z", box=False, color=color.gray(0.3))

E_arrows = []
B_arrows = []
S_arrows = []
for i in range(N):
    z = i * dz
    E_arrows.append(arrow(pos=vec(0, 0, z), axis=vec(0, 0, 0), color=color.red, shaftwidth=0.02))
    B_arrows.append(arrow(pos=vec(0, 0, z), axis=vec(0, 0, 0), color=color.blue, shaftwidth=0.02))
    S_arrows.append(arrow(pos=vec(0, 0, z), axis=vec(0, 0, 0), color=color.green,
                          shaftwidth=0.05, headwidth=0.12, headlength=0.12))

# ---------------- controls and graph ----------------
running = True
reset_needed = False

def toggle_run(b):
    global running
    running = not running
    b.text = "Pause" if running else "Run"

def set_direction(m):
    global direction
    global reset_needed
    direction = 1 if m.selected == "+z" else -1
    reset_needed = True

scene.append_to_caption("\n")
button(text="Pause", bind=toggle_run)
scene.append_to_caption("   Propagation: ")
menu(choices=["+z", "-z"], index=0, bind=set_direction)
scene.append_to_caption("\n\n")
info = wtext(text="")
scene.append_to_caption("\n")

g = graph(title="At z = 0 m:  E, S and the running time-average of S", xtitle="t (ns)",
          ytitle="Ex (V/m),  S (mW/m^2)", width=900, height=260, xmin=0, xmax=3 * T * 1e9)
gE = gcurve(graph=g, color=color.red, label="Ex (V/m)")
gS = gcurve(graph=g, color=color.green, label="Sz (mW/m^2)")
gA = gcurve(graph=g, color=color.black, label="average of Sz (mW/m^2)")

# ---------------- main loop ----------------
n = 0                   # frame counter, t = n * dt
S_sum = 0.0             # sum of Sz(z=0) over the frames, for the time average
S_avg_measured = 0.0    # average over whole periods only
while True:
    rate(50)
    if reset_needed:
        n = 0
        S_sum = 0.0
        S_avg_measured = 0.0
        gE.delete()
        gS.delete()
        gA.delete()
        reset_needed = False
    if not running:
        continue
    t = n * dt
    k_hat = vec(0, 0, direction)
    always_forward = True       # does S point along k_hat at every point?
    for i in range(N):
        z = i * dz
        phase = k * z - direction * omega * t
        E = vec(E0 * cos(phase), 0, 0)
        B = cross(k_hat, E) / c         # B = (k_hat x E) / c
        S = cross(E, B) / mu0           # Poynting vector (W/m^2)
        if dot(S, k_hat) < 0:
            always_forward = False
        E_arrows[i].axis = E
        B_arrows[i].axis = B_scale * B
        if i % S_every == 0:
            S_arrows[i].axis = S_scale * S
        if i == 0:
            Ex0 = E.x
            Sz0 = S.z

    S_sum = S_sum + Sz0
    n = n + 1
    if n % 100 == 0:                    # a whole number of periods is complete
        S_avg_measured = S_sum / n
    if t <= 3 * T:
        gE.plot(t * 1e9, Ex0)
        gS.plot(t * 1e9, Sz0 * 1e3)
        gA.plot(t * 1e9, S_sum / n * 1e3)

    info.text = ("Wave travels along <b>" + ("+z" if direction == 1 else "-z") + "</b>.   t = "
                 + "{:.2f}".format(t * 1e9) + " ns = " + "{:.2f}".format(t / T) + " T"
                 + ".   S points along k at all " + str(N) + " points: <b>"
                 + ("yes" if always_forward else "NO") + "</b>"
                 + "<br>At z = 0:  Sz = " + "{:+.4e}".format(Sz0) + " W/m^2"
                 + "<br>Time average of Sz over whole periods = " + "{:+.4e}".format(S_avg_measured)
                 + " W/m^2,   theory E0^2/(2 mu0 c) = " + "{:.4e}".format(S_avg_theory) + " W/m^2")
