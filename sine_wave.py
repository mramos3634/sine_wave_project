# sine_wave.py
import numpy as np
import matplotlib.pyplot as plt

# Define the sine wave parameters
frequency = 5  # Frequency of the sine wave
amplitude = 1  # Amplitude of the sine wave
time = np.linspace(0, 2 * np.pi, 500)  # Time range for the sine wave

# Generate the sine wave
wave = amplitude * np.sin(frequency * time)

# Plot the sine wave
plt.plot(time, wave)
plt.title("Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
