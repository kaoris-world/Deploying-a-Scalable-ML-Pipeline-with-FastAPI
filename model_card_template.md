# Model Card
For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a Random Forest Classifier built with scikit-learn. The goal is simple.
Given some basic information about a person, predict whether they earn more or less
than $50K a year. The model uses 100 decision trees and was built with a fixed
random seed so results stay consistent across runs.

## Intended Use
This model was built as part of a machine learning pipeline project. It is meant to
explore how demographic and employment data relates to income levels. It is a good
tool for research or learning purposes, but it should not be used to make real
decisions about people like hiring, lending, or anything with real consequences.

## Training Data
The data comes from the 1994 US Census, commonly known as the "Adult" dataset.
It has about 32,000 records and includes information like age, education, job type,
marital status, race, sex, and hours worked per week. The dataset was split 80/20.
80% was used to train the model and 20% was set aside for testing.

## Evaluation Data
The 20% test split was used to evaluate the model. The same data processing steps
from training were applied to the test data to keep things consistent.

## Metrics
The model was evaluated using Precision, Recall, and F1 Score.

Overall performance on the test set:

Precision: 0.7391
Recall: 0.6384
F1: 0.6851

Performance varies depending on the group. The model tends to do better on larger,
more represented groups in the data. Smaller groups like people who work without
pay have very few examples, so those results are not as reliable.

## Ethical Considerations
The dataset includes sensitive attributes like race, sex, and country of origin.
Since the data is from 1994, it likely reflects the biases and inequalities of that
time. The model picks up on those patterns, which means it may not treat all groups
equally. Anyone using this model should be aware of that and look closely at the
slice performance results before drawing any conclusions.

## Caveats and Recommendations
The data is 30 years old at this point, so a lot has changed in terms of job markets,
income levels, and demographics. This model works well as a learning project but
would need to be rebuilt with more current data before it could be useful in any
real world setting. Always check the slice outputs to understand how the model
performs across different groups, not just overall.