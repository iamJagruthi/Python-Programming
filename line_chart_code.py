import matplotlib.pyplot as plt
days=list(range(1,28))
temperature = [65, 66, 70, 72, 75, 76, 78, 80, 81, 79, 75, 70, 68, 67, 70, 73, 75, 76, 78, 80, 81, 82, 80, 78, 76, 74, 71]
plt.plot(days, temperature, marker = 'o', label= 'Daily temperature changes in july')
plt.xlabel('days')
plt.ylabel('temperature')
plt.title('Daily temperature changes in july')
plt.legend()
plt.show()
