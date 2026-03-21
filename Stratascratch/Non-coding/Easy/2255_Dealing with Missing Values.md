### 2255_Dealing with Missing Values
https://platform.stratascratch.com/technical/2255-dealing-with-missing-values
```yml
Company : IBM + 1 more
Difficulty : Easy
Question Type : Technical
Title : Dealing with Missing Values
```

- My solution
``` 
In a previous data project, we developed a model to classify care service demand groups
based on medical records of 194,475 seniors aged 65 and older nationwide.
At that time, I gained experience with LightGBM while addressing missing values.
In supervised learning, LightGBM does not impute missing values (NaN) separately
but automatically handles them by minimizing loss during decision-making.
For example, when classifying users into multiple groups based on physical functional limitations and mental health issues,
each class is converted into one-hot encoding, and the model compares the predicted probabilities with the actual ground truth.
The loss function used here is Multi-class Logloss, and through this,
the model learns by optimizing the prediction accuracy for each class.
```

- Analyze
```
With the goal of answering in 90 seconds, GPT provided this response.
When preparing for an interview, it definitely seems challenging to polish my answers in English:
```
```
In a previous project, I developed a model to classify care service demand groups based on
the medical records of over 194,000 seniors nationwide.
During this project, I gained experience with LightGBM and its handling of missing values.
In supervised learning, LightGBM does not require explicit imputation for NaN values; instead,
it automatically assigns them to the branch that minimizes the loss during tree splitting.
For example, when classifying users into multiple groups based on physical functional limitations and mental health issues,
 each class is represented in one-hot encoding, and the model compares predicted probabilities with actual labels.
The loss function used here is Multi-class Logloss,
which allows the model to optimize prediction accuracy across all classes while naturally handling missing values.
```
