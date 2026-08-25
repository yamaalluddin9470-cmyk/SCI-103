from vpython import *
import numpy as np

# ============================================================================
# LAB 06: VPython Simulation - 1D Spring-Mass System with Real-Time Graphs
# ============================================================================

# Setup display
scene = display(width=900, height=700, center=vector(6, 0, 0), 
                title="Spring-Mass System Simulation (Simple Harmonic Motion)")

# ============================================================================
# SECTION 1: Setup Graphs for Real-Time Plotting
# ============================================================================

# Graph 1: Position vs Time
g1 = graph(title='Position vs Time', xtitle='Time (s)', ytitle='Position (m)', 
           width=400, height=300, x=0, y=550)
f1 = gcurve(color=color.green, label='x(t)', graph=g1)

# Graph 2: Velocity vs Time
g2 = graph(title='Velocity vs Time', xtitle='Time (s)', ytitle='Velocity (m/s)', 
           width=400, height=300, x=450, y=550)
f2 = gcurve(color=color.blue, label='v(t)', graph=g2)

# Graph 3: Acceleration vs Time
g3 = graph(title='Acceleration vs Time', xtitle='Time (s)', ytitle='Acceleration (m/s²)', 
           width=400, height=300, x=0, y=200)
f3 = gcurve(color=color.red, label='a(t)', graph=g3)

# Graph 4: Energy vs Time (Kinetic, Potential, Total)
g4 = graph(title='Energy vs Time', xtitle='Time (s)', ytitle='Energy (J)', 
           width=400, height=300, x=450, y=200)
f_ke = gcurve(color=color.cyan, label='Kinetic Energy', graph=g4)
f_pe = gcurve(color=color.orange, label='Potential Energy', graph=g4)
f_te = gcurve(color=color.white, label='Total Energy', graph=g4)

# ============================================================================
# SECTION 2: Physical Setup - Spring-Mass System
# ============================================================================

# Fixed pivot point
pivot = vector(0, 0, 0)

# Fixed bracket/wall
bracket = box(pos=pivot, size=vector(0.1, 5, 5), color=color.green)

# Mass (ball)
mass = 1.0  # kg
ball = sphere(pos=vector(12, 0, 0), velocity=vector(0, 0, 0), 
              radius=1, mass=mass, color=color.blue)
ball.label = label(pos=ball.pos, text='Mass', opacity=0)

# Spring properties
spring_constant = 1.0  # N/m
spring = helix(pos=pivot, axis=ball.pos - pivot, radius=0.4, 
               constant=spring_constant, thickness=0.1, coils=20, color=color.red)

# Equilibrium position (where spring force = 0)
eq_pos = vector(spring_constant, 0, 0)
eq_marker = sphere(pos=eq_pos, radius=0.3, color=color.yellow, opacity=0.5)
eq_label = label(pos=eq_pos + vector(0, 1.5, 0), text='Equilibrium', opacity=0)

# ============================================================================
# SECTION 3: Simulation Parameters
# ============================================================================

t = 0  # Current time
dt = 0.01  # Time step (smaller for better accuracy)
t_max = 20  # Total simulation time
rate_limit = 100  # Animation frame rate

# Initial conditions
ball.pos = vector(12, 0, 0)  # Displace from equilibrium
ball.velocity = vector(0, 0, 0)  # Start from rest

# Storage for data analysis
time_data = []
pos_data = []
vel_data = []
acc_data = []
ke_data = []
pe_data = []
te_data = []

# Initial energy
x0 = ball.pos.x - eq_pos.x
initial_pe = 0.5 * spring_constant * x0**2
initial_ke = 0.5 * mass * mag(ball.velocity)**2
initial_energy = initial_pe + initial_ke

# ============================================================================
# SECTION 4: Main Simulation Loop
# ============================================================================

while t < t_max:
    rate(rate_limit)
    
    # Calculate displacement from equilibrium
    displacement = ball.pos - eq_pos
    
    # Apply Hooke's Law: F = -k*x
    # Acceleration: a = F/m = -(k/m)*x
    acceleration = -(spring_constant / mass) * displacement
    
    # Numerical Integration (Velocity-Verlet-like)
    ball.velocity = ball.velocity + acceleration * dt
    ball.pos = ball.pos + ball.velocity * dt
    
    # Update spring visualization
    spring.axis = ball.pos - spring.pos
    
    # Update ball position label
    ball.label.pos = ball.pos + vector(0, 2, 0)
    
    # ========================================================================
    # SECTION 5: Energy Calculations
    # ========================================================================
    
    # Displacement from equilibrium (x-component only)
    x = ball.pos.x - eq_pos.x
    
    # Potential Energy: PE = 1/2 * k * x^2
    pe = 0.5 * spring_constant * x**2
    
    # Kinetic Energy: KE = 1/2 * m * v^2
    ke = 0.5 * mass * mag(ball.velocity)**2
    
    # Total Energy
    total_energy = ke + pe
    
    # ========================================================================
    # SECTION 6: Plot Data in Real-Time
    # ========================================================================
    
    # Plot position (x-component only)
    f1.plot(pos=(t, x))
    
    # Plot velocity (x-component only)
    f2.plot(pos=(t, ball.velocity.x))
    
    # Plot acceleration (x-component only)
    f3.plot(pos=(t, acceleration.x))
    
    # Plot energies
    f_ke.plot(pos=(t, ke))
    f_pe.plot(pos=(t, pe))
    f_te.plot(pos=(t, total_energy))
    
    # ========================================================================
    # SECTION 7: Store Data for Post-Analysis
    # ========================================================================
    
    time_data.append(t)
    pos_data.append(x)
    vel_data.append(ball.velocity.x)
    acc_data.append(acceleration.x)
    ke_data.append(ke)
    pe_data.append(pe)
    te_data.append(total_energy)
    
    # Increment time
    t += dt

# ============================================================================
# SECTION 8: Post-Simulation Analysis & Verification
# ============================================================================

print("\n" + "="*70)
print("SPRING-MASS SYSTEM SIMULATION RESULTS")
print("="*70)

print(f"\nSimulation Parameters:")
print(f"  Mass (m):             {mass} kg")
print(f"  Spring Constant (k):  {spring_constant} N/m")
print(f"  Equilibrium Position: {eq_pos.x} m")
print(f"  Time Step (dt):       {dt} s")
print(f"  Simulation Duration:  {t_max} s")

# Calculate theoretical period
T_theoretical = 2 * np.pi * np.sqrt(mass / spring_constant)
print(f"\n📊 PERIOD ANALYSIS:")
print(f"  Theoretical Period (T = 2π√(m/k)): {T_theoretical:.4f} s")

# Find peaks in position to measure experimental period
pos_array = np.array(pos_data)
time_array = np.array(time_data)

# Find local maxima (peaks)
from scipy.signal import find_peaks
peaks, _ = find_peaks(pos_array, height=max(pos_array)*0.9)

if len(peaks) >= 2:
    period_measured = 2 * (time_array[peaks[1]] - time_array[peaks[0]])
    period_error = abs(period_measured - T_theoretical) / T_theoretical * 100
    print(f"  Measured Period (from simulation): {period_measured:.4f} s")
    print(f"  Period Error: {period_error:.2f}%")
else:
    print(f"  Note: Could not measure experimental period (need more oscillations)")

# Energy conservation analysis
print(f"\n⚡ ENERGY CONSERVATION ANALYSIS:")
print(f"  Initial Total Energy:   {initial_energy:.6f} J")
print(f"  Final Total Energy:     {te_data[-1]:.6f} J")
print(f"  Energy Variation (ΔE):  {abs(te_data[-1] - initial_energy):.6f} J")
print(f"  Relative Error (ΔE/E):  {abs(te_data[-1] - initial_energy)/initial_energy * 100:.4f}%")

# Find max displacement
max_displacement = max(pos_data)
min_displacement = min(pos_data)
print(f"\n📏 DISPLACEMENT ANALYSIS:")
print(f"  Maximum Displacement:   {max_displacement:.4f} m")
print(f"  Minimum Displacement:   {min_displacement:.4f} m")
print(f"  Amplitude:              {max_displacement:.4f} m")

# Max velocity
max_velocity = max(vel_data, key=abs)
print(f"\n🚀 VELOCITY ANALYSIS:")
print(f"  Maximum Velocity:       {max_velocity:.4f} m/s")
print(f"  Theoretical Max (v_max = ω*A): {np.sqrt(spring_constant/mass) * max_displacement:.4f} m/s")

# Max acceleration
max_acceleration = max(acc_data, key=abs)
print(f"\n⚙️  ACCELERATION ANALYSIS:")
print(f"  Maximum Acceleration:   {max_acceleration:.4f} m/s²")
print(f"  Theoretical Max (a_max = ω²*A): {(spring_constant/mass) * max_displacement:.4f} m/s²")

print("\n" + "="*70)
print("Simulation Complete! Check the graphs for visualization.")
print("="*70 + "\n")
