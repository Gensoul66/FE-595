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
    plt.xlabel('x - axis')
    plt.ylabel('y-axis')
    plt.title('My lines')
    plt.legend()
    plt.show()


if __name__ == "__main__" :
    main()
