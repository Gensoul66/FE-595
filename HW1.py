import numpy as np
import matplotlib.pyplot as plt


def main():
    # create a 2pi sequence and plug it in to sine function and cosine function
    x = np.arange(0, 2 * np.pi, 0.001)
    y_sine = np.sin(x)
    y_cosine = np.cos(x)

    # plot them out
    plt.plot(x, y_sine, label="Sine")
    plt.plot(x, y_cosine, label="Cosine")

    plt.plot(np.linspace(0, 0.5 * np.pi),
             np.tan(np.linspace(0, 0.5 * np.pi)),
             label='Tangent',
             color='red')  # added by Haohang Li

    plt.plot(np.linspace(0.5 * np.pi + 1e-10, 1.5 * np.pi),
             np.tan(np.linspace(0.5 * np.pi + 1e-10, 1.5 * np.pi)),
             color='red')  # added by Haohang Li

    plt.plot(np.linspace(1.5 * np.pi + 1e-10, 2 * np.pi),
             np.tan(np.linspace(1.5 * np.pi + 1e-10, 2 * np.pi)),
             color='red')  # added by Haohang Li
    
    plt.axhline(y=0.0, color='black')  # added by Haohang Li

    plt.ylim(-1.00, 1.00)  # the original scale is from -1.0 to 1.0, added by Haohang Li
    plt.xlabel('x - axis')
    plt.ylabel('y-axis')
    plt.title('My lines')
    plt.legend()
    plt.show()


if __name__ == "__main__" :
    main()
