# LAB 05: Spring-Mass System Simulation - Lab Report

**Student Name:** _______________________  
**Student ID:** _______________________  
**Date:** _______________________  
**Course:** SCI-103  
**Instructor:** _______________________

---

## 📋 Table of Contents
1. [Objective](#objective)
2. [Introduction & Theory](#introduction--theory)
3. [Methodology](#methodology)
4. [Results](#results)
5. [Analysis & Discussion](#analysis--discussion)
6. [Conclusion](#conclusion)
7. [References](#references)

---

## 🎯 Objective

**Objective Statement:**

The objective of this laboratory experiment is to:
- Simulate a 1D spring-mass system using VPython
- Verify Newton's Second Law and Hooke's Law through numerical simulation
- Analyze the simple harmonic motion of a mass-spring oscillator
- Examine energy conservation (kinetic, potential, and total energy)
- Compare theoretical predictions with experimental measurements

---

## 📚 Introduction & Theory

### Background
A mass-spring system is a fundamental model in physics that demonstrates simple harmonic motion (SHM). When a mass is attached to a spring and displaced from its equilibrium position, the spring exerts a restoring force proportional to the displacement.

### Mathematical Foundation

#### Hooke's Law
The restoring force exerted by the spring is given by:
$$F = -k(x - x_{\text{eq}})$$

Where:
- $F$ = restoring force (N)
- $k$ = spring constant (N/m)
- $x$ = current position (m)
- $x_{\text{eq}}$ = equilibrium position (m)

#### Newton's Second Law
Applying Newton's Second Law ($F = ma$):
$$a = -\frac{k}{m}(x - x_{\text{eq}})$$

Where:
- $a$ = acceleration (m/s²)
- $m$ = mass (kg)

#### Period of Oscillation
For a mass-spring system, the theoretical period of oscillation is:
$$T = 2\pi\sqrt{\frac{m}{k}}$$

#### Energy Conservation
In an ideal spring-mass system without friction, total mechanical energy is conserved:
$$E_{\text{total}} = KE + PE = \text{constant}$$

Where:
- $KE = \frac{1}{2}mv^2$ (kinetic energy)
- $PE = \frac{1}{2}k(x-x_{\text{eq}})^2$ (potential energy)

---

## 🔧 Methodology

### A. Simulation Parameters

| Parameter | Value | Unit |
|-----------|-------|------|
| Mass ($m$) | 1.0 | kg |
| Spring Constant ($k$) | 1.0 | N/m |
| Equilibrium Position ($x_{\text{eq}}$) | 1.0 | m |
| Initial Position ($x_0$) | 12.0 | m |
| Initial Velocity ($v_0$) | 0.0 | m/s |
| Time Step ($dt$) | 0.01 | s |
| Total Simulation Time | 20.0 | s |
| Animation Frame Rate | 100 | fps |

### B. Numerical Integration Method

The simulation uses the **Velocity-Verlet integration scheme**:

$$v_{t+1} = v_t + a_t \cdot dt$$
$$x_{t+1} = x_t + v_{t+1} \cdot dt$$

This method provides better accuracy than simple Euler integration while remaining computationally efficient.

### C. VPython Implementation

The simulation includes:
1. **3D Visualization**: Animated spring-mass system
2. **Real-Time Graphing**: Four concurrent graphs updated during simulation
3. **Data Collection**: Storage of position, velocity, acceleration, and energy data
4. **Post-Analysis**: Automatic calculations of period, energy conservation, and errors

---

## 📊 Results

### 1. Position vs Time Graph

![Position vs Time](./screenshots/position_vs_time.png)

**Description:** The position graph shows sinusoidal oscillation around the equilibrium position.

- **Maximum Displacement:** $x_{\text{max}}$ = __________ m
- **Minimum Displacement:** $x_{\text{min}}$ = __________ m
- **Amplitude (A):** = __________ m

### 2. Velocity vs Time Graph

![Velocity vs Time](./screenshots/velocity_vs_time.png)

**Description:** The velocity graph is 90° out of phase with position, reaching maximum when position crosses equilibrium.

- **Maximum Velocity:** $v_{\text{max}}$ = __________ m/s
- **Minimum Velocity:** $v_{\text{min}}$ = __________ m/s

### 3. Acceleration vs Time Graph

![Acceleration vs Time](./screenshots/acceleration_vs_time.png)

**Description:** The acceleration graph is 180° out of phase with position, always pointing toward equilibrium.

- **Maximum Acceleration:** $a_{\text{max}}$ = __________ m/s²
- **Minimum Acceleration:** $a_{\text{min}}$ = __________ m/s²

### 4. Energy vs Time Graph

![Energy Plot](./screenshots/energy_plot.png)

**Description:** Shows kinetic energy (KE), potential energy (PE), and total energy (TE) over time.

| Quantity | Initial (J) | Final (J) | Average (J) |
|----------|-------------|-----------|-------------|
| Kinetic Energy | __________ | __________ | __________ |
| Potential Energy | __________ | __________ | __________ |
| Total Energy | __________ | __________ | __________ |

### 5. 3D Animation Screenshot

![3D Spring-Mass System](./screenshots/3d_animation.png)

**Description:** The 3D animation shows the spring-mass system with real-time motion visualization.

---

## 📈 Analysis & Discussion

### A. Period Analysis

**Theoretical Period:**
$$T_{\text{theoretical}} = 2\pi\sqrt{\frac{m}{k}} = 2\pi\sqrt{\frac{1.0}{1.0}} = __________ \text{ s}$$

**Measured Period (from simulation):**
$$T_{\text{measured}} = __________ \text{ s}$$

**Period Error:**
$$\text{Error} = \left|\frac{T_{\text{measured}} - T_{\text{theoretical}}}{T_{\text{theoretical}}}\right| \times 100\% = __________\%$$

**Discussion:**
[Write your analysis of the period comparison. Explain any differences between theoretical and measured values.]

---

### B. Velocity Analysis

**Theoretical Maximum Velocity:**
$$v_{\text{max, theory}} = \omega \cdot A = \sqrt{\frac{k}{m}} \cdot A = __________\text{ m/s}$$

Where $\omega = \sqrt{k/m}$ is the angular frequency and $A$ is the amplitude.

**Measured Maximum Velocity:**
$$v_{\text{max, measured}} = __________ \text{ m/s}$$

**Velocity Error:**
$$\text{Error} = \left|\frac{v_{\text{max, measured}} - v_{\text{max, theory}}}{v_{\text{max, theory}}}\right| \times 100\% = __________\%$$

**Discussion:**
[Analyze the velocity measurements and compare with theory.]

---

### C. Acceleration Analysis

**Theoretical Maximum Acceleration:**
$$a_{\text{max, theory}} = \omega^2 \cdot A = \frac{k}{m} \cdot A = __________\text{ m/s}^2$$

**Measured Maximum Acceleration:**
$$a_{\text{max, measured}} = __________ \text{ m/s}^2$$

**Acceleration Error:**
$$\text{Error} = \left|\frac{a_{\text{max, measured}} - a_{\text{max, theory}}}{a_{\text{max, theory}}}\right| \times 100\% = __________\%$$

**Discussion:**
[Analyze the acceleration measurements.]

---

### D. Energy Conservation Analysis

**Initial Total Energy:**
$$E_{\text{initial}} = KE_0 + PE_0 = __________ \text{ J}$$

**Final Total Energy:**
$$E_{\text{final}} = KE_f + PE_f = __________ \text{ J}$$

**Energy Change:**
$$\Delta E = E_{\text{final}} - E_{\text{initial}} = __________ \text{ J}$$

**Relative Energy Error:**
$$\frac{\Delta E}{E_{\text{initial}}} = \left|\frac{E_{\text{final}} - E_{\text{initial}}}{E_{\text{initial}}}\right| \times 100\% = __________\%$$

**Discussion:**
[Explain the energy conservation results. A small error is expected due to numerical integration. Discuss possible sources of error and how they could be minimized.]

**Sources of Error:**
- Finite time step (dt) in numerical integration
- Rounding errors in floating-point calculations
- Approximations in the integration algorithm

---

### E. Phase Relationship Analysis

**Expected Phase Relationships:**
- Position and velocity should be 90° out of phase
- Position and acceleration should be 180° out of phase
- Velocity and acceleration should be 90° out of phase

**Observations:**
[Describe what you observe in the graphs regarding phase relationships.]

---

## 💡 Discussion & Conclusions

### Key Findings

1. **Harmonic Motion:** The simulation successfully demonstrates simple harmonic motion with sinusoidal position, velocity, and acceleration.

2. **Energy Conservation:** The total mechanical energy remains approximately constant throughout the simulation, confirming energy conservation principle.

3. **Theoretical Verification:** Measured values of period, velocity, and acceleration closely match theoretical predictions.

4. **Numerical Accuracy:** The Velocity-Verlet integration scheme provides good accuracy while remaining computationally efficient.

### Observations

[Write your detailed observations and interpretations of the results.]

### Limitations

1. **Numerical Integration:** Using a finite time step introduces small numerical errors that accumulate over time.
2. **Idealized System:** The simulation assumes no damping or air resistance.
3. **Zero Initial Velocity:** The system was started from rest, limiting the range of initial conditions tested.

### Suggestions for Improvement

1. Use a smaller time step for better accuracy
2. Implement adaptive time-stepping algorithms
3. Add damping force to study underdamped, critically damped, and overdamped scenarios
4. Test with different initial conditions (initial velocity ≠ 0)
5. Investigate non-linear spring behavior

### Conclusion

This laboratory successfully simulated a 1D spring-mass system and verified fundamental principles of classical mechanics, including:
- Hooke's Law and Newton's Second Law
- Simple Harmonic Motion
- Energy Conservation
- Period of oscillation

The simulation results closely match theoretical predictions, demonstrating the validity of the numerical methods used and confirming our understanding of oscillatory motion.

---

## 📚 References

1. Halliday, D., Resnick, R., & Walker, J. (2013). *Fundamentals of Physics* (10th ed.). John Wiley & Sons.

2. Marion, J. B., & Thornton, S. T. (2004). *Classical Dynamics of Particles and Systems* (5th ed.). Brooks/Cole.

3. VPython Documentation. Retrieved from https://vpython.org

4. Goldstein, H., Poole, C., & Safko, J. (2002). *Classical Mechanics* (3rd ed.). Addison Wesley.

5. [Any additional references you used]

---

## 📎 Appendices

### Appendix A: Complete VPython Code

[Include the complete `spring_mass_simulation.py` code here or reference the file]

### Appendix B: Raw Data

| Time (s) | Position (m) | Velocity (m/s) | Acceleration (m/s²) | KE (J) | PE (J) | Total E (J) |
|----------|--------------|-----------------|---------------------|--------|--------|-------------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

[Include a representative sample of data points, or attach a CSV file with complete data]

### Appendix C: Calculations

[Show detailed calculations for period, energy, errors, etc.]

---

**Report Submitted By:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

---

*End of Report*
