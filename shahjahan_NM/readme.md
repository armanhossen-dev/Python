# Numerical Integration on Accelerometer Data

Integrates x-axis linear acceleration from `Accelerometer.csv` over time to get
velocity change (Δv), using three numerical integration methods, then compares
accuracy against Simpson's 3/8 rule as the reference answer.

## Setup

1. Place `main.py`, `requirements.txt`, and all sensor CSVs (including
   `Accelerometer.csv`) in the same folder.
2. (Recommended) activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run:
   ```
   python main.py
   ```

## What it does

- Loads `Accelerometer.csv` (696 samples, ~10ms spacing, ~6.98s span).
- Resamples onto a uniform time grid of 690 intervals (h ≈ 0.01004 s) —
  divisible by both 2 and 3 — so Trapezoidal, Simpson's 1/3, and Simpson's 3/8
  all run on the identical dataset.
- Computes Δv (m/s) with each method.
- Using Simpson's 3/8 as the "true" value, computes absolute, relative, and
  percentage error for the other two methods.

## Results

**Integration (Δv, m/s)**

| Method | Result |
|---|---|
| Trapezoidal | -0.007872 |
| Simpson's 1/3 | -0.008006 |
| Simpson's 3/8 (reference) | -0.008826 |

**Error vs. Simpson's 3/8**

| Method | Absolute Error | Relative Error | % Error |
|---|---|---|---|
| Trapezoidal | 0.000955 | 0.1082 | 10.82% |
| Simpson's 1/3 | 0.000820 | 0.0930 | 9.30% |

Simpson's 1/3 is closer to the 3/8 result than Trapezoidal, as expected since
both Simpson variants are higher-order (O(h⁴)) than Trapezoidal (O(h²)).

## Customizing

To integrate a different signal, edit the two lines near the top of `main.py`:

```python
csv_path = os.path.join(BASE_DIR, 'Accelerometer.csv')   # swap CSV file
a_raw = df['x'].values                                    # swap column (x/y/z)
```
Any of the other sensor CSVs (`Gyroscope.csv`, `TotalAcceleration.csv`, etc.)
work the same way as long as they have a `seconds_elapsed` time column.