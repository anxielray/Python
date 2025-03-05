# _Linear Regression_

Linear regression is a statistical method for modeling the relationship between a dependent variable yyy and one (or more) independent variable(s) xxx. Here, I will describe the core mathematical approach to perform simple linear regression with one independent variable.
Step 1: Understanding the Linear Model

In simple linear regression, we assume a linear relationship between the dependent variable yyy and the independent variable xxx. The model can be expressed as:

y=β0+β1x+ϵy = \beta_0 + \beta_1 x + \epsilony=β0​+β1​x+ϵ

Where:

    yyy is the dependent variable.
    xxx is the independent variable.
    β0\beta_0β0​ is the intercept of the regression line.
    β1\beta_1β1​ is the slope of the regression line.
    ϵ\epsilonϵ is the error term.

Step 2: Collect Data

Gather your data points (xi,yi)(x_i, y_i)(xi​,yi​) for i=1,2,…,ni = 1, 2, \ldots, ni=1,2,…,n where nnn is the number of observations.
Step 3: Calculate the Means

Calculate the mean of xxx and yyy:

xˉ=1n∑i=1nxi\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_ixˉ=n1​i=1∑n​xi​
yˉ=1n∑i=1nyi\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_iyˉ​=n1​i=1∑n​yi​
Step 4: Calculate the Slopes

Now we need to calculate the slope β1\beta_1β1​ of the regression line:

β1=∑i=1n(xi−xˉ)(yi−yˉ)∑i=1n(xi−xˉ)2\beta_1 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2}β1​=∑i=1n​(xi​−xˉ)2∑i=1n​(xi​−xˉ)(yi​−yˉ​)​

This formula indicates how changes in xxx affect yyy.
Step 5: Calculate the Intercept

Next, we calculate the intercept β0\beta_0β0​:

β0=yˉ−β1xˉ\beta_0 = \bar{y} - \beta_1 \bar{x}β0​=yˉ​−β1​xˉ
Step 6: Formulate the Regression Equation

Having calculated β0\beta_0β0​ and β1\beta_1β1​, you can now write the equation of the regression line:

y=β0+β1xy = \beta_0 + \beta_1 xy=β0​+β1​x
Step 7: Make Predictions

You can use the regression equation to make predictions for new values of xxx.
Step 8: Evaluate the Model

Evaluate the goodness of fit of your model using metrics such as:

    R-squared: This statistic indicates how well the regression explains the variability of the data.

R2=1−SSresSStotalR^2 = 1 - \frac{\text{SS}_\text{res}}{\text{SS}_\text{total}}R2=1−SStotal​SSres​​

Where:

    SSres=∑i=1n(yi−y^i)2\text{SS}_\text{res} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2SSres​=∑i=1n​(yi​−y^​i​)2 (the residual sum of squares)
    SStotal=∑i=1n(yi−yˉ)2\text{SS}_\text{total} = \sum_{i=1}^{n} (y_i - \bar{y})^2SStotal​=∑i=1n​(yi​−yˉ​)2 (the total sum of squares)

Conclusion

By following these steps, you can perform simple linear regression analysis mathematically. These steps provide the groundwork for understanding more complex models and methodologies in linear regression, such as multiple linear regression.
