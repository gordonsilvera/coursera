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
modelFit0 <- train(classe~., data = trainingInput, method = "lda")
modelFit0
```

#####Principle Components Analysis
I then considered relationships between the explanatory features using Principle Componnets. I started by finding the most correlated variables among my potential features. 
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

Next, I developed a model with principle components with the `preProcess()` function (see model below). However, this generated an accuracy of 52% versus 70% for a model without PCA. 
```
modelFit1 <- train(classe~., data = trainingInput, method = "lda", preProcess=c("pca"))
modelFit1
```
Therefore -- in order to reduce the number of features used -- I will select a single variable from each (or certain) set(s) to include in the model, rather than using PCA. 

#####Model Selection
The next step is to determine which model to use. I will consider the following methods (I've described results of each for reference): lda, qda, nb
- *Linear Discriminant Analysis (lda)*: accurary of 69.9%
- *Quadratic Discriminant Analysis (qda)*: accuracy of 89.3%
- *.... (xx)*: accuracy of
- *Naive Bayes (nb)*: this calculation exceeded 10+ minutes therefore I decided not to use it

The [.....] model was the best balance of accuracy and efficiency/scalability, therefore I will move forward with this model.
```
modelQDA <- train(classe~., data = trainingInput, method = "qda"); modelQDA

Quadratic Discriminant Analysis 

14718 samples
   52 predictor
    5 classes: 'A', 'B', 'C', 'D', 'E' 

No pre-processing
Resampling: Bootstrapped (25 reps) 

Summary of sample sizes: 14718, 14718, 14718, 14718, 14718, 14718, ... 

Resampling results
  Accuracy   Kappa      Accuracy SD  Kappa SD   
  0.8948217  0.8670708  0.004669971  0.005868669
```

#####Variable Importance
The final step in my model selection process is to select 5 features to include in the model (as requested in the project instructions). Note that I would generally keep all features in the model. To reduce the number of features, I will use Variable Importance (`varImp()`) in the caret package. To select the final faetures, I have averaged the area under the curve (AUC) for the ROC calculation of each feature. Also, as previously mentioned, I will only keep a single feature from each of my highly correlated "sets" mentioned in the Principle Component section above. 
```
modelQDAImp <- varImp(modelFit3, scale=FALSE)
modelQDAImp
```

Below is the final model I used, a Quadratic Discriminant Model limited to 5 predictors. Unfortunately, the Accuracy falls from 89.3% to 50.0%. 

```
trainingFinal <- subset(training, select= c(classe, pitch_forearm, roll_dumbbell, magnet_arm_x, magnet_belt_y, accel_forearm_x))
modelFitFinal <- train(classe~., data = trainingFinal, method = "qda"); modelFitFinal

Quadratic Discriminant Analysis 

14718 samples
    5 predictor
    5 classes: 'A', 'B', 'C', 'D', 'E' 

No pre-processing
Resampling: Bootstrapped (25 reps) 

Summary of sample sizes: 14718, 14718, 14718, 14718, 14718, 14718, ... 

Resampling results
  Accuracy   Kappa      Accuracy SD  Kappa SD   
  0.5002189  0.3671346  0.007301924  0.009091167
```






