## Coursera: Machine Learning Final Project
7/25/15

###About the Dataset
Dumbbell Biceps Curl in five different fashions:
- Class A: exactly according to the specification 
- Class B: throwing the elbows to the front 
- Class C: lifting the dumbbell only halfway
- Class D: lowering the dumbbell only halfway
- Class E: throwing the hips to the front

Read more: http://groupware.les.inf.puc-rio.br/har#ixzz3gv6LfTpo

To cleanse the data, I have removed features with missing data. With the remaining features, I realize that they are aggregated into two types of groups. 
- Body Dimensions: belt, arm, dumbbell, forearm
- Metric Dimensions: roll, pitch, yaw, total acceleration, gyration (x,y,z), acceleration (x,y,z), magnet (x,y,z)

###Cross Validation
I have randomly selected 75% of “pml-training.csv” to train my models. 



###Exploratory Data Analysis
Initially, I would like to better understand my variables, and how they related to my outcome and one another. To do this, I have used the 





