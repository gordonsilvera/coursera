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

To cleanse the data, I have removed features with missing data. With the remaining features, I realize that they are aggregated into two types of groups. To simply certain portions of the analysis, I will analyze data within these "sub-feature" groupings. 
- *Body Dimensions*: belt, arm, dumbbell, forearm
- *Metric Dimensions*: roll, pitch, yaw, total acceleration, gyration (x,y,z), acceleration (x,y,z), magnet (x,y,z)


###Cross Validation
I have randomly selected 75% of “pml-training.csv” to train my models. 



###Exploratory Data Analysis
Initially, I would like to better understand my variables, and how they related to my outcome and one another. I first apply the `summary(mainTrain1)` function on the dataset. From there, I started considering the relationships between the explanatory variables with Q-plots and 
```
qplot(pitch_dumbbell, total_accel_dumbbell, colour=classe, data=training)   # sample Q-plot
qplot(total_accel_forearm, colour=classe, data=training, geom="density")    # sample Density Plots
```
Q-plots and Density Plots show some noticable differences in the classes; however, it is evident  that we will consider interations between sets of explanatory features -- I will use principle components for this. 

#####Principle Components Analysis
I started by finding the most correlated variables among my potential features. 
```
M <- abs(cor(training[,7:58]))
diag(M) <- 0
which(M > 0.8, arr.ind = T)
```
This output revealed several correlated features. I've grouped these into "sets" below.
- Set 1: 
