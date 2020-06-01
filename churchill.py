import random
import matplotlib.pyplot as plt

with open("frases.txt") as f:
    frases = f.readlines()
frases = [x.strip() for x in frases]

frase = random.choice(frases)
churchill = "Winston Churchill"

xmin, xmax = 20, 1180
ymin, ymax = 250, 975
im = plt.imread("churchill.jpeg")
plt.imshow(im)
props = dict(boxstyle='square', pad=0.3, facecolor='#2B292A', alpha=0)
plt.text(xmin, ymin, frase, fontsize=14, verticalalignment='top', bbox=props, color='white')
plt.text(285, 1050, churchill, fontsize=14, verticalalignment='top', color='white', style='italic')
plt.xticks([])
plt.yticks([])
plt.tight_layout()

plt.show()
#plt.savefig("frase.png", dpi = 150)
