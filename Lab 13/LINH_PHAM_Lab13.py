import pandas as pd
import matplotlib.pyplot as plt

csv_file = pd.read_csv('atlanta_weather.csv')

high = csv_file['High']
low = csv_file['Low']

month_mapping = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
csv_file['Month_Num'] = csv_file['Month'].map(month_mapping)
months = csv_file['Month_Num']

plt.plot(months, high, "b--o", label='High')
plt.plot(months, low,"g:^", label='Low')
plt.title("Atlanta – Monthly Temperature", fontsize = 20)
plt.xlabel("Month" , fontsize = 16)
plt.ylabel("Temperature (Fahrenheit)" , fontsize = 16)
plt.legend(fontsize=20)

max_temp_index = high.idxmax()
max_temp = high[max_temp_index]
plt.annotate('Highest temperature of the year',xy=(months[max_temp_index], max_temp),
             xytext=(months[max_temp_index] - 1, max_temp - 5),
             arrowprops=dict(facecolor='red'),
             fontsize=12, )
month_labels = list(month_mapping.keys())
plt.xticks(months, month_labels)
plt.show()