# Statisticsc


- `print(a,b,c, "hey" + " there")`
- `print(f"hey {name}")`
- `input("prompt message")` -- returns string
  

## Introduction 


## Python for statistics and data analysis


## Capstone Prorject 1 : Virtual Escape Room With Python

```python 

random.shuffle(list_)
start_time = time.time()

```

```python
import time, random

puzzles = [ {k1:v1, k2:v2, ...}, ...]

def play_escape_room(time_limit):
    start_time = time.time()

    random.shuffle(puzzles)
    num_puzzles = len(puzzles)
    solved_puzzles = 0

    for puzzle in puzzles:
        time_limit = play_puzzle(puzzle, time_limit)
        solved_puzzles += 1

        elapsed_time = time.time() - start_time

        if elapsed_time > time_limit :
            print("Time's up")
            return
        else:
            print(f"You have {round(time_limit - elapsed_time)} seconds remaining")

    if solved_puzzles == num_puzzles:
        print("Congratulations!")

def play_puzzle(puzzle, time_limit):
    is_correct = False

    while not is_correct:
        print(puzzle['question'])
        user_sol = input('Enter your solution: ')

        is_correct = puzzle['solution'].lower() == user_solution.lower()

        if is_correct:
            print("Correct")
            print(f"Story: {puzzle['story']}")
        else:
            time_limit -= 50
            print(f"Incorrect. Try again. Time remaining = {time_limit}")
    return time_limit
```

<br/><br/>


## Descriptive Statistics

- Variable types
  - Quantitative
    - Continuous
    - Discrete
  - Qualitative
    - Nominal
      - say eye color; No natural order
    - Ordinal 
      - say educattion; There is a natural order

<br/><br/>

- population 
- sample
  - subset of a population
  - must represet population otherwise could lead to unreliable conclusions

<br/><br/>

```python
# `%cd` prints current directory in colab
# `with path` -- sets cd path

import pandas as pd
import seaborn as sns
import scipy.stats as st

df = pd.read_csv("file.csv")
df.head()

df.info() # ColumnName, Non-Null, Count, Dtype

df.OBP.hist() # plots a histogram with the OBP column values

df.loc[ (df.Team == 'BOS') & (df.Year >= 2000)]

```

<br/><br/>


- Measures of Central Tendency
  - show typical or center value of a dataset
  - summarize data. 
  - mean
    - average
    - add everything and divide by total number of values
    - highly influenced by outliers or extreme values
    - types
      - Arithmetic
      - Geometric
      - Harmonic
    - $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$
    - $x_i$ - values
    - $n$ - number of observations
    - mean should be used to describe symmetrical distributions
    - ```python
      df.col_name.mean()
      df.loc[df.Team == "ARI"].RS.mean()
      df.loc[(df.Team == "ARI") &(df.Year >= 2005)].RS.mean()

      df.loc[(df.Team == "CHC") & ( (df.Year < 2000) | (df. Year > 2005 ))].RA.mean()
      ```
  - median 
    - represents middle value when values are sorted
    - less sensitive to outliers
    - more robust for skewed data
    - center of ordered set or 50th percentile of an ordered distribution or set
    - `df.loc[(df.Team == "BAL") & (df.Year <= 2000)].W.median()`
  - mode
    - most frequent value
    - can have multiple modes or none at all
    - useful for categorical or discrete data
    - less informative for continuous data with numerous unique values
    - most common element in a set or group
    - `df.OBP.mode() `

- Measures of Dispersion
  - standard deviation
    - measures a data set dispersion from its mean
    - businesses always strive for a lower variablity
    - consistency is a sign of quality
    - $\sigma_{population} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{x})^2}$
      - $x_i$ - values
      - $\bar{x}$ - mean
      - $n$ - number of observations
    - $\sigma_{sample} = \sqrt{\frac{1}{N - 1  } \sum_{i=1}^{N} (x_i - \bar{x})^2}$
      - $x_i$ - values
      - $\bar{x}$ - mean
      - $n$ - number of observations
    - sample size and variability correlate positively
      - higher sample size, lower variability ...
    - standard deviation of population is less than of a sample 
  - variance
    - standard deviation squared
    - both variance and standard deviation represent same Key Performance Indicator
    - $\sigma^2 =\frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{x})^2$
    ```python
    df.OOBP.mean()
    df.OOBP.std() # Sample Standard Deviation by default. Normalized by N - 1; ddof = 1
    df.OOBP.std(ddof = 0) # Population Standard Deviation
    
    # DDOF - Delta Degrees of Freedom

    df.OOBP.var()
    ```

<br/><br/>

- CV -- Coefficient of Variation
  - measure of data variability expressed as a %  of mean
  - measure of association between two variables
  - measures relative variability of a set of data
  - allows standardized comparision of datasets
  - $CV = \frac{\sigma}{average}$
  - ```python
    df.describe() # count, mean, std, min, 25%, 50%, 75%, max

    cv = df.RS.std() / df.RS.mean()

    # as a rule of thumb, data with high variability has CV > 1
    ```


<br/><br/>

- Covariance
  - indicates the direction of the relationship between two variables 
  - covariance > o => positive relationship -- directly proportional
  - covariance < 0 => negative relationship -- inversely proportional
  - covariance = 0 => no relationship
  - $$\text{COV}(x, y)_{pop} = \frac{\varepsilon(x_i - \bar{x})(y_i - \bar{y})}{N}$$
  - $$\text{COV}(x, y)_{sample} = \frac{\varepsilon(x_i - \bar{x})(y_i - \bar{y})}{N - 1}$$
  - only measures the direction, does not indicate the strength of the relationship
  - ```python

    # covariance works with continuous variables

    df_co = df[["col1", "col2", "col3"]]
    df_co.cov() # say a 3x3 matrix with cov values
    ```

<br/><br/>



- Correlation
  - Pearson Correlation, Kendall Correlation, Spearman Correlation, ...
  - measures the strength of a relationship between two variables
  - varies between -1 and 1
  - correlation = 1 => positively strong
  - correlation =  -1 => negatively strong
  - correlation = 0 => no relationship
  - $$r =  \frac{\sum (x_i - \bar{x})(y_i - \bar{y})} {\sqrt{\sum (x_i - \bar{x})^2(y_i - \bar{y})^2}}$$
  - is at the heart of Machine Learning. 
  - Correlation is not causation
  - spurious correlation
    - that which come out of luck 
  - confirmation bias -- say you are looking from a business perspective, and somethimes things look apparent, and you are trying to connect the dots, and you fall into the issue, which is that you try and you assume causation when in fact it is just correlation
  - ```python
    df_co.corr() # correlation matrix. Represents strength and direction of relationship. between -1 and 1

    # rule of thumb. >0.5 strong | >0.3 & <0.5 medium | >0.1 & < 0.3 low

    sns.heatmap(data = df_co.corr(), 
                annot = True,  # data values
                center = 0, 
                cmap = 'coolwarm', 
                linewidths = 1 # lines between boxes
                linecolor = 'black')
    ```
<br/><br/>

- Normal Distribution
  - aka Gaussian Distribution is a pattern
  - It is symmetrical and is characterized by bell shaepd curve
  - Most values center arount the mean
  - real-life distributions are similar to normal distribution but are never exactly like it
  - 68-95-99 rule
    - 68.26% of observations are within 1 standard deviation from mean
    - 95.44% of observations are within 2 standard deviations from mean
    - 99.72% of observations are within 3 standard deviations from mean
  - 6-sigma represents a goal where 99.9966% of the products are defect free
  - ```python
    df.W.hist()

    df.W.plot.density()

    # 68 95 99
    df.loc[(df.W <= df.W.mean() + 1 * df.W.std()) & 
            (df.W >= df.W.mean() - 1 * df.W.std())].W.count() / df.W.count()
    # this should be close to 68%


    ```

<br/><br/>




## Confidence Intervals

## Capstone Project 2 : Lights, Camera, Statistics


## Hypothesis Testing

## Capstone Project 3 : ChatGPT Data Analysis

## Multilinear Regression

## Capstone Project 4 : Multilinear Regression

## Logistic Regression

## Capstone Project 5 : Surviving Titanic - Logistic Regression with ChatGPT

## Cox Proportional Hazard Regression

## Capstone Project 6 : Surviving the App-pocalypse - Cox Regression with ChatGPT

