import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('car_data.csv') #read csv
print('Shape of the dataframe: ', df.shape)

jap_v6 = df[(df['origin'] == 'japan') & (df['cylinders'] == 6)] #find rows base on parameters
list_jap_v6 = jap_v6['name'].to_list()  #put names into a list
print('Japanese v6 car:', list_jap_v6)

no_hp = df[df['horsepower'].isnull()]   #find rows that have Null horsepower
list_no_hp = no_hp['name'].to_list()    #put names into a list
print('Cars with missing horsepower data: ', list_no_hp)

mpg_20 = df[df['mpg'] >= 20] #find rows base on parameters
print('Number of cars having mpg >= 20:', len(mpg_20)) #print the number of rows

mpg_highest = df.loc[df['mpg'].idxmax()]    #find biggest data in mpg
list_mpg_highest = []
list_mpg_highest.append(mpg_highest['name'])    #put names into a list
print('Most fuel efficient car: ', list_mpg_highest)

weight = df['weight']   #put data of row 'weight' into weight
max_weight = weight.max()   #biggest weight
min_weight = weight.min()   #smallest weight
avg_weight = weight.mean()  #average weight
print(f'Minimum Weight: {min_weight}, Maximum Weight: {max_weight}, Average Weight: {avg_weight}')


new_df = df.dropna() #drop rows with missing values
print('Shape after removing the missing values: ', new_df.shape)


mpg = df['mpg'] #put data of row 'mpg' into mpg
displacement = df['displacement'] #put data of row 'displacement' into displacement

plt.subplot(2, 1, 1)    #1st subplot
plt.scatter(mpg, weight, label='weight')    #mpg vs weight
plt.ylabel('weight')

plt.subplot(2, 1, 2)    #2nd subplot
plt.scatter(mpg, displacement, label='displacement')    #mpg vs displacement
plt.ylabel('displacement')
plt.xlabel('mpg')

plt.show()