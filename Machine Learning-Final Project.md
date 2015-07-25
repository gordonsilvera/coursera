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
Initially, I would like to better understand my variables, and how they related to my outcome and one another. I first apply the `summary(mainTrain1)` function on the dataset. From there, I started considering the relationships between the explanatory variables with Q-plots and Density plots.
```
qplot(pitch_dumbbell, total_accel_dumbbell, colour=classe, data=training)   # sample Q-plot
qplot(total_accel_forearm, colour=classe, data=training, geom="density")    # sample Density Plots
```

###Model Development

#####Initial Model
At first, I created a Linear Discriminant Analysis model that included all numerical features without pre-processing. This generated an Accuracy of 69.9%. I will use this as a benchmark going forward. 

```
trainingInput <- training[,(7:59)]
modelNB = train(classe~., data=trainingInput, method="nb")    # method = "nb", "lda", "gbm"
predNB = predict(modelNB, trainingInput)

modelFit0 <- train(classe~., data = trainingInput, method = "lda"); modelFit0
```

#####Principle Components Analysis
I started by finding the most correlated variables among my potential features. 
```
M <- abs(cor(training[,7:58]))
diag(M) <- 0
which(M > 0.8, arr.ind = T)
```
This output revealed several correlated features. I've grouped these into "sets" below.
- *Set 1*: yaw_belt, total_accel_belt, accel_belt_y, accel_belt_z, roll_belt
- *Set 2*: accel_belt_x, magnet_belt_x, pitch_belt
- *Set 3*: gyros_arm_x, gyros_arm_y
- *Set 4*: accel_arm_x, magnet_arm_x, magnet_arm_y, magnet_arm_z
- *Set 5*: pitch_dumbbell, yaw_dumbbell, accel_dumbbell_x, accel_dumbbell_z
- *Set 6*: gyros_dumbbell_x, gyros_dumbbell_z, gyros_forearm_z, gyros_forearm_y

Next, I developed a model with principle components with the `preProcess()` function (see model below). However, this generated an accuracy of 52% versus 70% for a model without PCA. Therefore -- in order to reduce the number of features used -- I will select a single variable from each (or certain) set(s) to include in the model, rather than using PCA. 



