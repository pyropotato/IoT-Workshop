import matplotlib.pyplot as plt
slices = [1,2,1,1]
activities = ['A','B','C','D']
plt.subplot(221)
plt.bar(activities,slices)
plt.show()
