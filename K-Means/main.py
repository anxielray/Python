# [Question 1]: Exercise 2: K-Means Clustering

# Objective: Implement the K-Means clustering algorithm to group a set of 2D points.

# Instructions:

#     Generate a synthetic dataset of 2D points that can be clustered. You can use NumPy for this, arranging points into groups based on random centers.
#     Implement the K-Means algorithm:
#         Initialize kkk cluster centroids randomly from your dataset.
#         Assign each point to the nearest centroid.
#         Update centroids based on the assigned points.
#         Repeat the assignment and update steps until convergence (i.e., until the centroids do not change significantly).
#     Plot the final clustered points along with their corresponding centroids.

# Hints:

#     Utilize the distance formula to compute the nearest centroid for each point.
#     Consider convergence to occur when the centroids change by less than a small threshold (like 1e-4).
#     Use matplotlib to visualize the clusters and centroids.

# Bonus:

# After completing the exercises, consider implementing additional features like:

#     Allowing the user to specify the number of clusters kkk for the K-Means algorithm.
#     Evaluating the performance of your linear regression model using metrics like Mean Squared Error (MSE).
