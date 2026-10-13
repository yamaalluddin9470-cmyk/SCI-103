Web VPython 3.2
# SCI-103 Lab 13 - Part C: Polarization (linear y, circular RH, circular LH)
# How to run: glowscript.org -> Create New Program -> delete everything in the
# editor -> paste this whole file -> Run   (line 1 must stay "Web VPython 3.2")
#
# The polarization is chosen from the menu under the scene.
#   Linear (y)  : E = E0 cos(phase) y_hat
#   Circular RH : E = E0 [cos(phase) x_hat + sin(phase) y_hat]
#   Circular LH : E = E0 [cos(phase) x_hat - sin(phase) y_hat]
# with phase = kz - wt, and B always from  B = (k_hat x E) / c .
# The orange ball follows the tip of E at z = 4 m and leaves a trail;
# the small black arrow shows which way the tip is moving.

# ---------------- wave parameters (SI units) ----------------
c = 3e8                 # speed of light (m/s)
mu0 = 4 * pi * 1e-7     # magnetic constant (T m/A)
lam = 2.0               # wavelength (m)
f = c / lam             # frequency (Hz)
omega = 2 * pi * f      # angular frequency (rad/s)
k = 2 * pi / lam        # wave number (rad/m)
T = 1 / f               # period (s)
E0 = 1.0                # amplitude of E (V/m)
k_hat = vec(0, 0, 1)    # wave travels along +z

mode = "Linear (y)"

# ---------------- display settings ----------------
B_scale = c                         # B arrow length = c*B
S_scale = 0.45 / (E0 * E0 / (mu0 * c))   # longest S arrow is 0.45 m
dt = T / 100                        # 100 frames per period
N = 41
dz = 0.1                            # z = 0 ... 4 m = 2 wavelengths
L = (N - 1) * dz
S_every = 5

scene.title = "<b>Part C</b> - Polarization:  red = <b>E</b>,  blue = c<b>B</b>,  green = <b>S</b>,  orange = path of the tip of <b>E</b> at z = 4 m"
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

# tip of E at the last point z = L (closest to the camera)
tip = sphere(pos=vec(0, 0, L), radius=0.05, color=color.orange,
             make_trail=True, retain=100, trail_radius=0.012)
tip_dir = arrow(pos=vec(0, 0, L), axis=vec(0, 0, 0), color=color.black, shaftwidth=0.04)

# ---------------- physics ----------------
def E_field(phase):
    if mode == "Linear (y)":
        return vec(0, E0 * cos(phase), 0)
    if mode == "Circular RH":
        return vec(E0 * cos(phase), E0 * sin(phase), 0)
    return vec(E0 * cos(phase), -E0 * sin(phase), 0)       # Circular LH

# ---------------- controls and graphs ----------------
running = True
reset_needed = False

def toggle_run(b):
    global running
    running = not running
    b.text = "Pause" if running else "Run"

def set_mode(m):
    global mode
    global reset_needed
    mode = m.selected
    reset_needed = True

def view_3d(b):
    scene.fov = pi / 3
    scene.forward = vec(-1, -0.5, -1.2)
    scene.up = vec(0, 1, 0)
    scene.range = 2.4

def view_front(b):
    # look along -z, facing the oncoming wave: x is to the right, y is up.
    # A very small field of view (almost no perspective) makes every z look the same size.
    scene.fov = 0.05
    scene.forward = vec(0, 0, -1)
    scene.up = vec(0, 1, 0)
    scene.range = 1.7

scene.append_to_caption("\n")
button(text="Pause", bind=toggle_run)
scene.append_to_caption("   Polarization: ")
menu(choices=["Linear (y)", "Circular RH", "Circular LH"], index=0, bind=set_mode)
scene.append_to_caption("   View: ")
button(text="3D", bind=view_3d)
button(text="Face the wave", bind=view_front)
scene.append_to_caption("\n\n")
info = wtext(text="")
scene.append_to_caption("\n")

g1 = graph(title="Tip of E at z = 4 m (facing the wave)", xtitle="Ex (V/m)",
           ytitle="Ey (V/m)", width=330, height=330, align="left",
           xmin=-1.2, xmax=1.2, ymin=-1.2, ymax=1.2)
g_path = gcurve(graph=g1, color=color.orange)
g2 = graph(title="Angle of E at z = 4 m (from +x towards +y)", xtitle="t (ns)",
           ytitle="angle (degrees)", width=560, height=330, align="left",
           xmin=0, xmax=3 * T * 1e9)
g_angle = gcurve(graph=g2, color=color.purple)

# ---------------- main loop ----------------
n = 0                   # frame counter, t = n * dt
angle = 0.0             # angle of E at z = L, unwrapped (degrees)
prev_raw = 0.0
angle_start = 0.0       # angle at the start of the current period
Emin = 1e9
Emax = 0.0
result_rotation = "(measuring the first period ...)"
result_Emag = ""
prev_tip = vec(0, 0, L)
while True:
    rate(50)
    if reset_needed:
        n = 0
        g_path.delete()
        g_angle.delete()
        tip.clear_trail()
        result_rotation = "(measuring the first period ...)"
        result_Emag = ""
        reset_needed = False
    if not running:
        continue
    t = n * dt
    angle_EB_min = 180.0
    angle_EB_max = 0.0
    angle_k_max_dev = 0.0       # largest |angle(E,k) - 90| or |angle(B,k) - 90| (degrees)
    S_forward = True
    for i in range(N):
        z = i * dz
        phase = k * z - omega * t
        E = E_field(phase)
        B = cross(k_hat, E) / c
        S = cross(E, B) / mu0
        E_arrows[i].axis = E
        B_arrows[i].axis = B_scale * B
        S_arrows[i].axis = S_scale * S if i % S_every == 0 else vec(0, 0, 0)
        if mag(E) > 0.05 * E0:          # angles are only defined when E is not zero
            a = degrees(diff_angle(E, B))
            angle_EB_min = min(angle_EB_min, a)
            angle_EB_max = max(angle_EB_max, a)
            angle_k_max_dev = max(angle_k_max_dev, abs(degrees(diff_angle(E, k_hat)) - 90),
                                  abs(degrees(diff_angle(B, k_hat)) - 90))
        if dot(S, k_hat) < 0:
            S_forward = False
        if i == N - 1:
            E_tip = E

    # tip of E at z = L, the direction it moves, and its angle
    tip.pos = vec(E_tip.x, E_tip.y, L)
    move = tip.pos - prev_tip
    tip_dir.pos = tip.pos
    tip_dir.axis = 0.35 * norm(move) if mag(move) > 1e-6 else vec(0, 0, 0)
    prev_tip = tip.pos
    raw = degrees(atan2(E_tip.y, E_tip.x))
    if n == 0:
        angle = raw
        angle_start = raw
        Emin = mag(E_tip)
        Emax = mag(E_tip)
    else:
        d = raw - prev_raw
        if d > 180:
            d = d - 360
        if d < -180:
            d = d + 360
        angle = angle + d
    prev_raw = raw
    Emin = min(Emin, mag(E_tip))
    Emax = max(Emax, mag(E_tip))

    if t <= 3 * T:
        g_path.plot(E_tip.x, E_tip.y)
        g_angle.plot(t * 1e9, angle)

    n = n + 1
    if n % 100 == 0:                    # one more full period is complete
        turn = angle - angle_start
        if turn < -300:
            way = "clockwise"
        elif turn > 300:
            way = "counter-clockwise"
        else:
            way = "no rotation (E flips back and forth on a line)"
        result_rotation = "turns " + "{:+.1f}".format(turn) + " degrees per period  ->  <b>" + way + "</b>"
        result_Emag = ("|E| over the last period: min = " + "{:.3f}".format(Emin)
                       + " V/m, max = " + "{:.3f}".format(Emax) + " V/m")
        angle_start = angle
        Emin = 1e9
        Emax = 0.0

    info.text = ("<b>" + mode + "</b>,  t = " + "{:.2f}".format(t * 1e9) + " ns = "
                 + "{:.2f}".format(t / T) + " T"
                 + "<br>Tip of E at z = 4 m, seen facing the wave (from +z):<br>" + result_rotation
                 + "<br>" + result_Emag
                 + "<br>Checks at all " + str(N) + " points:  angle(E, B) = "
                 + "{:.3f}".format(angle_EB_min) + " to " + "{:.3f}".format(angle_EB_max)
                 + " degrees,  S along +z: " + ("yes" if S_forward else "NO")
                 + "<br>Largest difference of angle(E, k) and angle(B, k) from 90 degrees: "
                 + "{:.3f}".format(angle_k_max_dev) + " degrees")
