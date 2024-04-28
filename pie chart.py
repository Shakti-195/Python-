
import matplotlib.pyplot as plt

# Data stored in a dictionary
marks = {'Math': 25, 'Hindi': 35, 'Python': 45, 'Physics': 15, 'Chemistry': 20}

# Create lists for labels and values
subjects = list(marks.keys())
marks_values = list(marks.values())

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(marks_values, labels=subjects, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Student XYZ Marks Distribution')
plt.show()
