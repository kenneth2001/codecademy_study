import codecademylib3_seaborn

# Add your code below:
from matplotlib import pyplot as plt
import random
numbers_a = range(1,13)
numbers_b = [random.randint(0,1000) for i in range(12)]

plt.plot(numbers_a, numbers_b)
plt.show()