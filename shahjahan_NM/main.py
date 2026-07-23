import pandas as pd
import numpy as np

# Name: Shah Jahan Mia
# ID: 242-33-091
# Section: B

# Load data 
import os

# CSV files live in the same folder as this script (main.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'Accelerometer.csv')

df = pd.read_csv(csv_path)
df = df.sort_values('seconds_elapsed').reset_index(drop=True)

t_raw = df['seconds_elapsed'].values
a_raw = df['x'].values  # x-axis linear acceleration (m/s^2), gravity already removed

print(f"Raw samples: {len(t_raw)}, time span: {t_raw[-1]-t_raw[0]:.4f} s")
print(f"Raw dt -> min: {np.diff(t_raw).min():.6f}, max: {np.diff(t_raw).max():.6f}, mean: {np.diff(t_raw).mean():.6f}")

h = np.diff(t_raw).mean()          # uniform step size
n_intervals_raw = int((t_raw[-1] - t_raw[0]) / h)
n_intervals = (n_intervals_raw // 6) * 6      # largest multiple of 6 that fits
n_points = n_intervals + 1

t_uniform = t_raw[0] + np.arange(n_points) * h
a_uniform = np.interp(t_uniform, t_raw, a_raw)   # linear interpolation onto uniform grid

print(f"\nResampled to n = {n_points} points ({n_intervals} intervals), h = {h:.6f} s")
print(f"(divisible by 2 -> ok for Simpson 1/3;\n divisible by 3 -> ok for Simpson 3/8)")

t = t_uniform
a = a_uniform
n = n_intervals   # number of intervals

# 1. Trapezoidal rule 
def trapezoidal(y, h):
    return h * (0.5*y[0] + 0.5*y[-1] + np.sum(y[1:-1]))

I_trap = trapezoidal(a, h)

#  2. Simpson's 1/3 rule (needs n even) 
def simpson13(y, h):
    n = len(y) - 1
    assert n % 2 == 0, "Simpson 1/3 needs an even number of intervals"
    odd_sum  = np.sum(y[1:-1:2])   # y1, y3, y5 ...
    even_sum = np.sum(y[2:-1:2])   # y2, y4, y6 ...
    return (h/3) * (y[0] + y[-1] + 4*odd_sum + 2*even_sum)

I_simp13 = simpson13(a, h)

#  3. Simpson's 3/8 rule (needs n divisible by 3) 
def simpson38(y, h):
    n = len(y) - 1
    assert n % 3 == 0, "Simpson 3/8 needs number of intervals divisible by 3"
    total = y[0] + y[-1]
    for i in range(1, n):
        total += (3 if i % 3 != 0 else 2) * y[i]
    return (3*h/8) * total

I_simp38 = simpson38(a, h)

print("\n===== Integration results (velocity change, m/s) =====")
print(f"Trapezoidal rule : {I_trap:.6f}")
print(f"Simpson's 1/3 rule: {I_simp13:.6f}")
print(f"Simpson's 3/8 rule: {I_simp38:.6f}  (taken as 'true' value)")

# Error analysis (Simpson 3/8 as reference) 
true_val = I_simp38

def errors(approx, true):
    abs_err = abs(true - approx)
    rel_err = abs_err / abs(true) if true != 0 else float('nan')
    pct_err = rel_err * 100
    return abs_err, rel_err, pct_err

trap_abs, trap_rel, trap_pct   = errors(I_trap, true_val)
simp13_abs, simp13_rel, simp13_pct = errors(I_simp13, true_val)

print("\n===== Error analysis (reference = Simpson 3/8) =====")
print(f"{'Method':<20}{'Absolute Error':>18}{'Relative Error':>18}{'% Error':>12}")
print(f"{'Trapezoidal':<20}{trap_abs:>18.6f}{trap_rel:>18.6f}{trap_pct:>11.4f}%")
simp13_label = "Simpson 1/3"
print(f"{simp13_label:<20}{simp13_abs:>18.6f}{simp13_rel:>18.6f}{simp13_pct:>11.4f}%")