import numpy as np
import pandas as pd
import zipfile
import os

# Open ZIP File 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
zip_path = os.path.join(BASE_DIR, "Sitting_to_Standing.zip")

z = zipfile.ZipFile(zip_path, "r")

num = 0
print("Files in ZIP:")
for file in z.namelist():
    num+=1
    print(f'{num: 2}. {file}')

# Files to Process (file name -> column to integrate)
files = {
    "Accelerometer.csv": "x",
    "Gyroscope.csv": "z",
    "Gravity.csv": "z",
    "Orientation.csv": "roll",
}

# Numerical Integration Functions
def trapezoidal(x, y):
    h = x[1] - x[0]
    I = h / 2 * (y[0] + y[-1] + 2 * np.sum(y[1:-1]))
    return np.round(I, 4)


def simpson13(x, y):
    h = x[1] - x[0]
    I = h / 3 * (
        y[0] + y[-1]
        + 4 * np.sum(y[1:-1:2])
        + 2 * np.sum(y[2:-2:2])
    )
    return np.round(I, 4)


def simpson38(x, y):
    h = x[1] - x[0]
    I = (3 * h / 8) * (
        (y[0] + y[-1])
        + 3 * np.sum(y[1:-1:3])
        + 3 * np.sum(y[2:-1:3])
        + 2 * np.sum(y[3:-1:3])
    )
    return np.round(I, 4)


# Process Each File
for file, column in files.items():
    print("\n\nProcessing File:", file)
    print("=" * 70)

    csv_file = z.open(file, "r")
    df = pd.read_csv(csv_file)
    print(df.head())

    x = df["seconds_elapsed"].values
    y = df[column].values

    # Number of intervals
    number_segment = len(x) - 1
    print("\nOriginal Data Points :", len(x))
    print("Original Segments    :", number_segment)

    # Adjust intervals so they work for both Simpson's 1/3 and 3/8
    if number_segment % 2 == 0 and number_segment % 3 == 0:
        print("No adjustment needed.")
        n_final = number_segment
    else:
        print("\nAdjusting number of segments...")
        n_final = (number_segment // 6) * 6

    x = x[:n_final + 1]
    y = y[:n_final + 1]

    print("Final Data Points :", len(x))
    print("Final Segments    :", len(x) - 1)
    print("Divisible by 2    :", (len(x) - 1) % 2 == 0)
    print("Divisible by 3    :", (len(x) - 1) % 3 == 0)

    # Numerical Integration
    I_t = trapezoidal(x, y)
    I_s13 = simpson13(x, y)
    I_s38 = simpson38(x, y)

    print("\nIntegration Results")
    print("-" * 30)
    print("Trapezoidal  =", I_t)
    print("Simpson 1/3  =", I_s13)
    print("Simpson 3/8  =", I_s38)

    # Error (Trapezoidal)
    abs_error = abs(I_s38 - I_t)
    rel_error = abs_error / abs(I_s38)
    per_error = rel_error * 100

    print("Trapezoidal Error (Reference: Simpson 3/8)")
    print("-" * 45)
    print("Absolute Error   =", np.round(abs_error, 4))
    print("Relative Error   =", np.round(rel_error, 6))
    print("Percentage Error =", np.round(per_error, 4), "%")

    # Error (Simpson 1/3)
    abs_error = abs(I_s38 - I_s13)
    rel_error = abs_error / abs(I_s38)
    per_error = rel_error * 100

    print("Simpson 1/3 Error (Reference: Simpson 3/8)")
    print("-" * 45)
    print("Absolute Error   =", np.round(abs_error, 4))
    print("Relative Error   =", np.round(rel_error, 6))
    print("Percentage Error =", np.round(per_error, 4), "%")

print("\nProcessing Completed Successfully.\n")

z.close()