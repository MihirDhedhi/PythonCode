import numpy as np
import matplotlib.pyplot as plt

def sine_wave(A, f, phi, t):
   
    y = A * np.sin(2 * np.pi * f * t + phi)
    plt.figure()
    plt.plot(t, y, label=f"Sine: A={A}, f={f}Hz, phi={phi}")
    plt.title("Sine Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()
    return y

def cosine_wave(A, f, phi, t):
    
    y = A * np.cos(2 * np.pi * f * t + phi)
    plt.figure()
    plt.plot(t, y, label=f"Cosine: A={A}, f={f}Hz, phi={phi}")
    plt.title("Cosine Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()
    return y

def exponential_signal(A, a, t):
    
    y = A * np.exp(a * t)
    plt.figure()
    plt.plot(t, y, label=f"Exponential: A={A}, a={a}")
    plt.title("Exponential Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()
    return y


if __name__ == "__main__":
    t = np.linspace(0, 1, 500)  
    sine_wave(2, 5, 0, t)       
    cosine_wave(2, 5, 0, t)     
    exponential_signal(1, -3, t) 