from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-1, 1, 100)
y = np.linspace(-2, 2, 100)

plt.plot(x, norm.pdf(x, 0, 1) - 0.125, label = "healthy", color = "green")
plt.plot(y, norm.pdf(y, 0, 2), label = "tumour", color = "red")
plt.xlim(-2,2)
plt.xticks([])
plt.yticks([])
plt.xlabel("Fragment length [bp]")
plt.ylabel("Probability")
plt.legend()
plt.savefig("explanatory_plot_pptx.png")
plt.show()
