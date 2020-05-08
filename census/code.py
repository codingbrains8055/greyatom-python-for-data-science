# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate((data, new_record))
age = census[0:, 0]
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)

race_0 = census[census[0:, 2] == 0]
race_1 = census[census[0:, 2] == 1]
race_2 = census[census[0:, 2] == 2]
race_3 = census[census[0:, 2] == 3]
race_4 = census[census[0:, 2] == 4]
len_0 = len(race_0[0:, 2])
len_1 = len(race_1[0:, 2])
len_2 = len(race_2[0:, 2])
len_3 = len(race_3[0:, 2])
len_4 = len(race_4[0:, 2])

min_count = min(len_0, len_1, len_2, len_3, len_4)
if min_count == len_0:
    minority_race = race_0[0, 2]
elif min_count == len_1:
    minority_race = race_1[0, 2]
elif min_count == len_2:
    minority_race = race_2[0, 2]
elif min_count == len_3:
    minority_race = race_3[0, 2]
elif min_count == len_4:
    minority_race = race_4[0, 2]
print(minority_race)

senior_citizens = census[census[0:, 0] > 60]
senior_citizens_len = len(senior_citizens[0:, 0])

working_hour_sum = sum(senior_citizens[0:, 6])
print(working_hour_sum)

avg_working_hour = working_hour_sum / senior_citizens_len
print(avg_working_hour)

high = census[census[0:, 1] > 10]
low  = census[census[0:, 1] <= 10]

avg_pay_high = np.mean(high[0:, 7])
print(avg_pay_high)

avg_pay_low = np.mean(low[0:, 7])
print(avg_pay_low)



