# ZTM Machine Learning and Data Science


<details open>
    <summary> ML & DS </summary>

## Contents
1. Machine Learning 101
2. Python
3. Work Environment
4. Data Analysis Pandas
5. Numpy
6. Data Visualizations : MatplotLib
7. Scikit-learn
8. Supervised learning
9. Regression 
10. Classification
11. Time Series
12. Neural Networks
13. Deep Learning
14. Transfer Learning
15. TensorFlow
16. Keras
17. Data Engineering
18. Hadoop 
19. Spark
20. Storytelling and Communication


## Introduction 

- [Course Resources](https://dev.mrdbourke.com/zero-to-mastery-ml/)
- [Github ](https://github.com/mrdbourke/zero-to-mastery-ml/discussions)

## Machine Learning 101

- computers do tasks for us
- we can specify rules, and it will follow -- calculate
- but how can a computer detect emotions, or persons, or animals, or objects; computers can't do a few things that only humans can
- however, machine learning changes this for good. Atleast most of the times
- AI -- human intelligence exhibited by machines
- narrow AI -- just as good or better than humans at specific tasks 
- general AI
- ML -- subset of AI; try and achieve AI through patterns in a set of data; science of getting machines act without being actually programmed
- DL -- one of the techniques for implementing machine learning
- DS -- Work with data, analyze, derive some sort of action or insights to drive business
- Teachable Machine by Google -- experiment how models or machine learning works. 
- Spreadsheets > Relational DB MySQL > Big Data - NoSQL MongoDB > Machine Learning
- ![](assets/2024-04-12-05-46-01.png)
- [ml-playground.com](https://ml-playground.com) -- go here and play around with the model
- use machines predit results based on incoming data
- [vas3k blog](https://vas3k.com/index.html)
- ![](assets/2024-04-12-05-55-22.png)
- Machine learning uses an algorithm or a program (called models )to take data and understand / learn different patterns to be able to take similar data and make future predictions and decisions; differ from normal programs in the learning aspect.
-  Normal Algorithm: Input & Instructions > Output
-  ML Algorithm: Input & Output > Tries to figure out instructions
-  Data Analysis: Look at data and try to understand it by comparing different examples, different features, visualizations, 
-  Data Science: Running experiments on a set of data with the hopes of finding actionable insights within it 

## ML & DS Framework

- Write code, make mistakes, build projects, learn what matters
- 6 steps
  1. problem definition -- what are we dealing with -- supervised, unsupervised, classification, regression?
  2. data -- what kind of data do we have -- structured, unstructured
  3. evaluation -- what success means to us -- say 95% accuracy -- something to aim for, because there is no perfect model 
  4. features -- what do we already know about the data
  5. modeling -- based on our problem and data what ml model should we use
  6. experimentation -- how could we improve, what can be done next 

- When shouldn't we use ML
  - will a simple handcoded instruction based system work?
- Types of Machine Learning
  - Supervised -- data and label; try predicting labels;
    - classification
      - binary classification
      - multi-class classification
    - regression -- predict a number
  - Unsupervised -- you provide labels, they aren't there to begin with
    - clustering
    - recommendation systems often start out as unsupervised
  - Transfer Learning -- leverage what one ML model learned in another ML model
  - Reinforcement Learning -- perform some action within a defined space and rewarding it or punishing it -- goal is to maximize the score 
- Types of Data
  > The more data the better
  - Structured Data
  - Unstructured Data
  - Static Data -- doesn't change over time -- CSV
  - Streaming Data -- constantly changed over time 

  - Static file > Jupyter Notebook > Pandas Data Analysis Matplotlib > scikit-learn Machine Learning
- Types of Evaluation -- what defines success for us
  - metrics
    - classification
      - accuracy
      - precision
      - recall
    - regression
      - mean absolute error
      - mean squared error
      - root mean squared error
    - recommendation
      - precision at k
- Features in Data -- what do we know about data; different forms of data
  - use feature variables to predict target variables
  - Numerical features
  - Categorical features
  - Derived feature -- Feature engineering -- creating new or altering existing features
  - Feature coverage -- process of ensuring all samples have similar information; How many samples have different features; Ideally every sample has the same feature
- Modelling
  - Based on problem and data, what machine learning model should we use
  - Generalization -- Ability of a ML model to perform well on unseen data
  - Data Splitting -- 70-80 10-15 10-15 
    - Training 
    - Validation -- tune
    - Test -- test and compare different models
  - Picking the model 
    - Choosing and training a model -- minimize time between experiments
      - Structured -- XGBoost, CatBoost, RandomForest -- Decision Tree Algorithms
      - Unstructured -- Deep Learning, Neural Networks, Transfer Learning
      - Some models work better than others on different problems
      - Don't be afraid to try things
      - Start small and build up (add complexity) as you need
    - Tuning a model
      - ML models have hyperparameters that you can adjust
      - A models first results aren't its last
      - Tuning can take place on training or validation data sets
    - Model comparision -- how will our model perform in the real world
      - Underfitting
        - Data Mismatch -- when the data your testing on is different from training data
        - fixes 
          - try a more advanced model
          - increase model hyperparameters
          - reduce amount of features
          - train longer
      - Overfitting
        - Data Leakage -- some of test leaks into training data
        - fixes 
          - collect more data
          - try less advance models
  - want to avoid overfitting and underfitting (head towards generality)
  - keep the test separate at all times
  - compare apples to apples
  - one best performance metric does not equal best model
- Experimentation
  - Machine Learning projects become tool matching projects
- Tools
  - Anaconda
  - Jupyter
  - Matplotlib
  - Pandas
  - NumPy
  - Scikit-learn
  - XGBoost
  - Pytorch 
  - TensorFLow
  - CatBoost
  - ![](assets/2024-04-14-03-34-31.png)

- [Elements of AI](https://www.elementsofai.com/)

## Data Science Environment Setup

- Anaconda - Hardware Store -- Software Distribution
- Miniconda - Workbench -- Software Distribution
- Conda - Personal assistant -- package manager 
- [getting your computer ready with conda](https://www.mrdbourke.com/get-your-computer-ready-for-machine-learning-using-anaconda-miniconda-and-conda/)
- [getting started with conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
- [conda cheatsheet](https://cdn.fs.teachablecdn.com/wyrLtEMTQ9OsuZzc00Jf)
- Collection of packages -- environment
- `conda create --prefix ./env pandas numpy matplotlib scikit-learn`
- `conda activate /Users/user/Download/temp/test_project1/env`
- `conda env list`
- `jupyter notebook`
- `conda install jupyter`
- `conda deactivate`
- you can now simply share the entire project folder, and ash can now activate the env and continue with work
- or you can export env to a YML file using `conda env export --prefix /Users/user/Desktop/project_1/env > environment.yml`
- `conda env create --file environment.yml --name env_from_file`

<br/>

- [Jupyter for beginners](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
- A cell can be in edit more or command mode
- ESC -- command mode; Enter -- Edit mode
- While in command mode, y -- code; m -- markdown
- `![alt text](link to image)`


## Pandas Data Analysis

- `conda env list` & `conda activate path_to_env`
- ```python
  import pandas as pd

  series = pd.Series(['Toyota', 'Lexus', 'Nexus'])
  series # 1 dimensional column object

  colors = pd.Series(['Black', 'Grey', 'Matt Black'])

  car_data = pd.DataFrame({"Make":series, "Color": colors})

  car_sales = pd.read_csv('filename.csv')

  car_sales.to_csv('newfile.csv', index = False) # index is set to True by default

  online_data = pd.read_csv('path_to_file.csv')
  ```
- index starts at 0
- axis = 0 --> row
- axis = 1 --> column


## Numpy


## Matplotlib


## Scikit-learn

![](assets/2024-08-19-15-43-18.png)

- sklearn -- python ML Library
  - built on numpy and matplotlib
  - built-in ml models
  - methods to evaluate
  - well designed api

![](assets/2024-08-19-15-45-34.png)

- refresher
  - teach computer what a snake is? ML can help
  - procedural programs -- input --> steps --> output
  - ml : input, output --> a robot that knows the steps / function / model / algorithm 
- [scikit-learn-reference-notebook](section-2-data-science-and-ml-tools/scikit-learn-what-were-covering.ipynb)

### Typical scikit-learn workflow 

- `conda env list`
- `conda activate path`
- `jupyter lab` `jupyter notebook`
- ```python
  np.random.seed(39)

  hd = pd.read_csv()
  X = hd.drop("target", axis = 1)
  y = hd["target"]

  from sklearn.ensemble import RandomForestClassifier
  clf = RandomForestClassifier()

  clf.get_params() # default hyperparameters

  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, )

  clf.fit(X_train, y_train)

  y_preds = clf.predict(X_test)

  clf.score(X_train, y_train) # might get 1 100%
  clf.score(X_test, y_test)

  from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

  classification_report(y_test, y_preds)
  confusion_matrix(y_test, y_preds)
  accuracy_score(y_test, y_preds)  
  ```

<br/>

- ```python
  np.random.seed(39)
  for i in range(10, 100, 10):
    clf = RandomForestClassifier(n_estimators=i).fit(X_train, y_train)
    print(f"{i} estimators ==> {clf.score(X_test, y_test) * 100 :.2f} accuracy")
  ```
- ```python
  import pickle

  pickle.dump(clf, open("fancy_name.pkl", "wb"))

  loaded_model = pickle.load(open("fancy_name.pkl", "rb"))
  loaded_model.score(X_test, y_test)
  ```

<br/>

- ```python
  import warnings

  warnings.filterwarnings("ignore")
  warnings.filterwarnings("default")

  sklearn.show_versions()

  ```

- `conda activate envpath`
- `conda list`
- `conda update packagename`
- `conda search packagename --info` -- if dependencies required are not met, the package version can not be installed
- `conda list python` 
- `conda uninstall packagename`
- `conda install python=3.6.9 sciki-learn=0.22 numpy pandas jupyter`


### Getting data ready

- Handle missing data
- Handle text data (convert to numerical)
- Feature scaling 
  - uses
    - improve model performance, convergenc, and prevents bias
    - reduce outliers impact
    - ensure data is on same scale and equal contributions to the model
  - sensitive
    - linear regression, logistic regression, neural network, PCA -- use gradient descent
    - KNN, K-means clustering, SVM -- distance-based algorithms
  - Normalization aka min-max scaling 
    - rescales all values to be between 0 and 1  sklearn.preprocessing.MinMaxScaler
  - Standardization
    - subracts mean value from all features (resulting features have 0 mean)
    - scales features to unit variance by dividing the feature by standard deviation `sklearn.preprocessing.StandardScaler`
  - ![](assets/2024-08-20-08-47-39.png)
  - usually not required for target
  - usually not required for tree based models -- the decision tree splits node based on a single feature -- others do not have effect
  - reading
    - [1 Feature Scaling : Why](https://medium.com/@rahul77349/feature-scaling-why-it-is-required-8a93df1af310)
      - puts values in same range so no variable is dominant
      - most algorithms use euclidean distance between two data points
        - k-nearest neighbors
        - principal component analysis -- get features with high variance -- variance is high for high magnitude features
        - speed up gradient descent
        - tree based models are not distance based models and hence do not require scaling
        - Linear Discriminant Analysis (LDA) and Naive Bayes, by design give weights to features. So scaling might not help
    - [2 Feature Scaling with Scikit-learn](https://benalexkeen.com/feature-scaling-with-scikit-learn/)
      - Normalization
        - Min Max Scaling
          - xi = x - minx(x) / max(x) - min(x)
          - shrinks range to 0 and 1 or -1 and 1 if negative values are present
          - sensitive to outliers; consider robust scaler if outliers are present
          - `from sklearn.preprocessing import minmax_scale`
          - `scaled_data = minmax_scale(original_data)`
          - `preprocessing.MinMaxScaler().fit_transform(df)`
        - Mean Normalization
          - xi = x - average(x) / max(x) - min(x)
          - `from sklearn import preprocessing`
          - `preprocessing.Normalizer().fit(X_train).transform(X_train)`
          - `from scipy import stats`
          - `normalized_data = stats.boxcox(original_data)`
        - Robust Scaler
          - uses interquartile range and hence robust to outliers
          - xi - Q1(x) / Q3(x) - Q1(x)
          - `scaler = preprocessing.RobustScaler()`
          - `robust_scaled_df = scaler.fit_transform(x)`
          - `robust_scaled_df = pd.DataFrame(robust_scaled_df, columns=['x1', 'x2'])`
      - In scaling you are changing the range of the data, in normalization you are changing the shape of the distribution
      - Standardization aka z-score normalization
        - assumes data is normally distributed; if not, not the best scaler to use
        - resulting distribution mean = 0, standard deviation = 1
        - xi = x - xbar (mean) / sigma (variance)
        - `from sklearn.preprocessing import StandardScaler`
        - `sc=StandardScaler(); X_train1=sc.fit_transform(X_train)`
      - Scaling to unit length
        - xi = x / mod(x)
      - Normalizer -- each point is within one unit distance from origin of the cartesian co-ord system
        - `scaler = preprocessing.Normalizer(); scaled_df = scaler.fit_transform(df)`
        - `scaled_df = pd.DataFrame(scaled_df, columns=df.columns)`
    - [3 Normalization vs Standardization](https://www.analyticsvidhya.com/blog/2020/04/feature-scaling-machine-learning-normalization-standardization/)
      - ```python
        from sklearn.preprocessing import MinMaxScaler
        
        pd.describe()

        norm = MinMaxScaler().fit(X_train)
        X_train_norm = norm.transform(X_train)
        X_test_norm = norm.transform(X_test)

        from sklearn.preprocessing import StandardScaler
        X_train_stand = X_train.copy()
        X_test_stand = X_test.copy()

        # numerical features
        num_cols = ['Item_Weight','Item_Visibility','Item_MRP','Outlet_Establishment_Year']

        # apply standardization on numerical features
        for i in num_cols:

            # fit on training data column
            scale = StandardScaler().fit(X_train_stand[[i]])
    
            # transform the training data column
            X_train_stand[i] = scale.transform(X_train_stand[[i]])
    
            # transform the testing data column
            X_test_stand[i] = scale.transform(X_test_stand[[i]])
        ```
      - standardizing one hot encoded features would mean assigning a distribution which we do not want
      - SVM with RBF kernel assumes that all features are centered around zero and variance is of same order -- hence standardization works best than normalization




<br/>

```python
import matplotlib.pyplot as plt
%matplotlib inline

# features x and labels y
# filling aka imputing / disregarding missing values 
# converting non-numerical to numerical -- feature engineering

X = hd.drop("drop", axis = 1)
y = hd["target"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, )

X_train.shape, X_test.shape, y_train.shape, y_test.shape
# ((242, 13), (61, 13), (242,), (61, ))

```

- Clean Data (handle missing values) ---> Transform Data (encoding data into machine understandable format | data is workable) ---> Reduce Data (dimensionality reduction | for computing optimization)
- ```python

  from sklearn.ensemble import RandomForestRegressor

  model = RandomForestRegressor()
  model.fit(X_train, y_train) # value error, could not convert string to float; or input contains NaN
  model.score(X_test, y_test)

  from sklearn.preprocessing import OneHotEncoder # Categories to numbers 
  from sklearn.compose import ColumnTransformer 

  categorical_features = ['Make', 'Color', 'Doors']
  one_hot = OneHotEncodeer()
  transformer = ColumnTransformer([("one_hot", 
                                    one_hot, 
                                    categorical_features)], # apply one hot encoding to these columns
                                    remainder='passthrough') # don't do anything for the rest of the columns
  transformed_X = transformer.fit_transform(X)

  pd.DataFrame(transformed_X) # col names = 0, 1, 2, 3, 4, 5, ...

  dummies = pd.get_dummies(car_sales[["Make", "Color", "Doors"]]) # another approach; col names = Make_Honda Make_Lexus, ...
  ```

![](assets/2024-08-19-16-45-28.png)

- In newer versions sklearn >= 0.23 -- OneHotEncoder class was upgraded to handle None and NaN values
- `sklearn.__version__`

### Missing values 
- Imputing : filling with some value
- Remove samples altogether
- Using pandas
  - ```python
    df.isna().sum() # missing values in each col

    df['col'].fillna("missing", inplace=True) # fills missing as value
    df['col'].fillna(df['col'].mean(), inplace=True)
    df['col'].value_counts()

    df.dropna(inplace=True) # removes rows with missing values
    ```
- It is best to fill/transform the training set and test set separately; split first; better to keep them separate. 
- Using sikit-learn
  - ```python
    df.isna().sum() 
    df.dropna(subset=['colname'], inplace=True) # drop rows contining this col val as null

    from sklearn.impute import SimpleImputer
    from sklearn.compose import ColumnTransformer

    cat_imputer = SimpleImputer(strategy = "constant", fill_value = "missing")
    door_imputer = SimpleImputer(strategy="constant", fill_value = 4)
    num_imputer = SimpleImputer(strategy="mean")

    cat_features = ["Make", "Color"]
    door_features = ["Doors"]
    num_features = ["Odometer"]

    imputer = ColumnTransformer([
      ('cat_imputer', cat_imputer, cat_features),
      ('door_imputer', door_imputer, door_features), 
      ('num_imputer', num_imputer, num_features)
    ])

    filled_X = imputer.fit_transform(X)  

    pd.DataFrame(filled_X, columns = ["Make", "Color", "Doors", "Odometer"])
    ```
### Choosing right model

- sklearn refers to ML models, algorithms as estimators
- Classification problem -- predicting category
  - CLF -- classification estimator
- Regression problem -- predicting number
- [SKLearn Algorithms Map](https://scikit-learn.org/1.3/tutorial/machine_learning_map/index.html)

```python
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
housing

housing_df = pd.DataFrame(housing['data'])
housing_df.columns = housing['feature_names']
housing_df["target_name"] = housing['target']

housing_df = housing_df.drop('MedHouseVal', axis = 1)

from sklearn.linear_model import Ridge

model = Ridge()
model.fit(X_train, y_train)
model.score(X_test, y_test) # coefficient of determination for ridge by default

from sklearn.ensemble import RandomForestRegressor

np.random.seed(39)

X = housing_df.drop('target', axis = 1)
y = housing_df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)
model.score(X_test, y_test) 

from sklearn.svc import LinearSVC
np.random.seed(39)
X = df.drop('target', axis = 1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LinearSVC()
clf.fit(X_train, y_train)
clf.score(X_test, y_test)
```

- If you have structured data, use ensemble methods
- If you have unstructured data, use deep learning or transfer learning


### Fitting a model 

- 

```python
y_preds = clf.predict(X_test)
np.mean(y_preds == y_test)

```










</details>

<br/>
<hr/>
<br/>


## Resources 

- [Intro to scikit-learn](https://github.com/mrdbourke/zero-to-mastery-ml/blob/master/section-2-data-science-and-ml-tools/introduction-to-scikit-learn.ipynb)
- [Intro to scikit-learn video](https://github.com/mrdbourke/zero-to-mastery-ml/blob/master/section-2-data-science-and-ml-tools/introduction-to-scikit-learn-video.ipynb)
- [Full example in google colab](https://colab.research.google.com/drive/162DyoCBFeufMjJI7n4XCiYpdqIdktZw_)

------


# Data Camp : Machine Learning 

## Supervised Learning with scikit-learn

- Supervised
  - Classification
  - Regression -- continuous value
  - requirements
    - no missing values
    - data in numeric format
    - data stored in pandas DF or Numpy Array
- Unsupervised

<br/>

```python
from sklearn.module import Model 

model = Model()
model.fit(X, y)
predictions = model.predict(X_new)
print(predictions)
```

- binary classification
  - zero or one
- k-Nearest Neighbors
  - looks at k closest labeled data points
  - takes a majority vote
 
```python
from sklearn.neighbors import KNeighborsClassifier 

X = churn_df[['col1', 'col2']].values
y = churn_df['col3'].values # .values converts to numpy arrays 

knn = kNeighborsClassifier(n_neighbors = 12)
knn.fit =(X, y)

predictions = knn.predict(X_new) # numpy array
```

<br/>

- Accuracy crct_predictions/total_observations
- large k -- less complex -- can cause underfitting
- small k -- more complex -- can cause overfitting

```python
from sklearn.model_selection import train_test_split

X = churn_df.drop("churn", axis=1).values
y = churn_df["churn"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42, stratify=y) # target label proportions reflect that of the original dataset.

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

print(knn.score(X_test, y_test)) # Models accuracy


neighbors = np.arange(1, 13)
train_accuracies = {}
test_accuracies = {}

for neighbor in neighbors:
  knn = KNeighborsClassifier(n_neighbors=neighbor)

  knn.fit(X_train, y_train)
  
  train_accuracies[neighbor] = knn.score(X_train, y_train)
  test_accuracies[neighbor] = knn.score(X_test, y_test)
print(neighbors, '\n', train_accuracies, '\n', test_accuracies)


plt.title("KNN: Varying Number of Neighbors")

plt.plot(neighbors, train_accuracies.values(), label="Training Accuracy")

plt.plot(neighbors, test_accuracies.values(), label="Testing Accuracy")

plt.legend()
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")

plt.show()
```