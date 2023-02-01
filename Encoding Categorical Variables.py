
#Ordinal encoding
# create dictionary of label:values in order
rating_dict = {'Excellent':5, 'New':4, 'Like New':3, 'Good':2, 'Fair':1}
 
#create a new column 
cars['condition_rating'] = cars['condition'].map(rating_dict)



# using scikit-learn
from sklearn.preprocessing import OrdinalEncoder
 
# create encoder and set category order
encoder = OrdinalEncoder(categories=[['Excellent', 'New', 'Like New', 'Good', 'Fair']])
 
# reshape our feature
condition_reshaped = cars['condition'].values.reshape(-1,1)
 
# create new variable with assigned numbers
cars['condition_rating'] = encoder.fit_transform(condition_reshaped)

#Label Encoding
from sklearn.preprocessing import LabelEncoder
 
# create encoder
encoder = LabelEncoder()
 
# create new variable with assigned numbers
cars['color'] = encoder.fit_transform(cars['color'])

#One-hot Encoding
import pandas as pd
# use pandas .get_dummies method to create one new column for each color
ohe = pd.get_dummies(cars['color'])
 
# join the new columns back onto our cars dataframe
cars = cars.join(ohe)


