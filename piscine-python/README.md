# Piscine-Python

- _This file contains the documentation for the Piscine-Python project._
- _Note that this piscine is a custom-made piscine and not from the 42-schools._

## Quest 1: Variables

### Print

- Define the following variables:

  - _An integer called epochs_

  - _A float called learning_rate_

  - _A string called model_name_

  - _A boolean called use_gpu_

- Print each variable and its type.
- Submit a file named `scalar_values.py` containing the code above.

Example output:

```sh
$ python scalar_values.py
epochs: 7
learning_rate: 0.1
model_name: sonnet
use_gpu: True
$
```

---

### User-Input

Goal: Take input and return meaningful output.

- Ask the user for their name, age, and favorite programming language.
Output a formatted string using f-strings.
- Submit a file named `data_input.py` containing the code above.

Exampe output:

```sh
$ python data_input.py 
Please enter your name: Anxiel
Please enter your age: 19
Please enter your favorite language: python
Hello Anxiel, you are 19 years old and your favorite language is python.
$
```

---

### Type Conversion

Goal: Convert between types like an ML pipeline does with data.

- You’re reading data from a CSV as strings.
Convert "32" into an integer, "3.141" into a float, and "True" into a boolean.
- Print them with their types.
- Submit a file named `type_conversion_lab.py` containing the code above.

Example output:

```sh
$ python type_conversion_lab.py
32 as an  integer is: 32, and is of Type: <class 'int'>
3.141 as a Float: 3.141, and is of Type: <class 'float'>
True as a Boolean: True, and is of Type: <class 'bool'>
$
```

---

### Feature Scaling

Goal: Normalize feature values — intro to how ML models treat variables.

- Given a variable `feature_value = 85` and `max_value = 100`,
write a formula to scale feature_value between 0 and 1.
Print the result.
- Submit a file named `feature_scaling_lab.py` containing the code above.

Example output:

```sh
$ python feature_scaling_lab.py 
Normalized value: 0.40
$
```

---

### Matrix

Goal: Store and explore structured data.

- Create variables for a 2D matrix using nested lists:
matrix = [[1, 2], [3, 4], [5, 6]]
- Print the number of rows and columns using len().
- Submit the file `matrix.py` containing the code above.

Example output:

```sh
$ python matrix.py
Number of rows: 12
Number of columns: 90
$
```

---

### Name_me

Goal: Use variables to describe data.

- Given a list:

```python
data = [3.2, 7.1, 4.6, 5.5, 9.0]
```

- Calculate the following and store in separate variables:

  - Minimum

  - Maximum

  - Mean

  - Range (max - min)
- Submit the file `name_me.py` containing the code above.

Example output:

```sh
$ python name_me.py
Minimum: 21.0
Maximum: 1.8
Mean: 9.0
Range: 48.7
$
```

---

### Parse_my_data

Goal: Introduce the idea of text as data.

- Ask the user to enter a sentence.
Then:

  - Store the sentence in a variable

  - Count how many words there are

  - Convert it to lowercase

- Print the result with a note on “preprocessing text data”
- Submit the file `parse_my_data.py` containing the code above.

Expected output:

```sh
$ python parse_my_data.py 
Please enter a sentence: Hello my name is Anxiel and I love programming in Python!
Number of words: 11
Lowercase sentence: hello my name is anxiel and i love programming in python!
Note: This is an example of preprocessing text data.
$
```

---

### Variable Scope

Goal: Understand scope — useful for functions, ML models, and beyond.

- Write a function train_model() that declares a local variable model_status = 'Training'
Outside the function, set model_status = 'Not started'
- Print the variable inside and outside to show the difference in scope.
- Submit the file `variable_scope.py` containing the code above.

Expected output:

```sh
$ python variable_scope.py 
Outside the function: Not started
Inside the function: Training
Outside the function after calling the function: Not started
$
```

---

### Error Calcluate

Goal: Use variables to simulate concepts in ML.

- Define:

```py
bias = 0.3  
variance = 0.6  
error = bias**2 + variance**2
```

- Print the total error and make sure that the error calculated has only 4 significant figures.
- Submit the file `error_calculate.py` containing the code above.

Expected output:

```sh
$ python error_calculate.py
Error: 0.5700
$
```

---

### Data Pipeline

Goal: Simulate a simplified ML data pipeline using only variables.

- Define variables for each stage of the pipeline:

  - `"raw_data"`

  - `"clean_data"`

  - `"features"`

  - `"model"`

  - `"prediction"`

- Use basic string or list manipulations to simulate "transforming" data through each stage.
- Submit the file `data_pipeline.py` containing the code above.

Expected output:

```sh
$ python data_pipeline.py            
Raw Data:    This is a sample sentence with extra whitespace and UPPERCASE letters.   
Clean Data: this is a sample sentence with extra whitespace and uppercase letters.
Features: ['this', 'is', 'a', 'sample', 'sentence', 'with', 'extra', 'whitespace', 'and', 'uppercase', 'letters.']
Model: simple_model
Prediction: Prediction based on features: ['this', 'is', 'a', 'sample', 'sentence', 'with', 'extra', 'whitespace', 'and', 'uppercase', 'letters.']
$
```

---
