
import matplotlib.pyplot as plt
import numpy as np
import math

labels = 'IT', 'Marketing', 'Data Science', 'Finance'
values = [500, 156, 300, 510]
explode = (0.05, 0.05, 0.05, 0.05) 

plt.pie(values, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
plt.show()