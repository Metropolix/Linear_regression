# Linear_regression
This project is a good introduction to machine learning

There is two file: 
*price_estimation.py* to get an prediction 
*training.py* to train prediction algorithm

# Installation

## Set up a Virtual Env 

### 1- Set up a virtual env

 ```
     => python3 -m venv env 
     => source env/bin/activate 
     => pip install -r requirements
```

# How to use this project 

## Launch without training

If you launch price_estimation.py first you should obtain a predicted value as 0 no matter the value you enter

## Launch training

Launch training.py with no args

## Launch with training

When you have previoulsy launch training, you should have a theta_file.csv updated with new value.
Now if you launch, price_estimation.py you should obtain a result


## Input Behavior

If you enter too big or too small or negative value for km, you will obtain a strange price. It's normal, linear regression is based on a "ax +b" model which doesn't fit perfectly with the case of car price estimations.


