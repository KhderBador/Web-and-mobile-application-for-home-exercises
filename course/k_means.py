import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from models import DataSet


def queryset_to_dataframe(queryset):
    data = list(queryset.values())
      # Convert the queryset to a list of dictionaries
    df = pd.DataFrame(data) 
    len=data.__len__()
    # Create a Pandas DataFrame from the list of dictionaries
    return df
# Load the Dataset

# X, y = load_iris(return_X_y=True)

# X,y = make_blobs(n_samples = 500,n_features = 2,centers = 3,random_state = 23)
dataset= DataSet.objects.all()
df= queryset_to_dataframe(dataset)
print(df)



# Build the Kmeans clustering model


# kmeans = KMeans(n_clusters = 3, random_state = 2)
# kmeans.fit(X)

# Find the cluster center


# kmeans.cluster_centers_

# Predict the cluster group:

# pred = kmeans.fit_predict(X)
# pred[len(pred)-1]

# Plot the cluster center with data points

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.scatter(X[:,0],X[:,1],c = pred, cmap=cm.Accent)
plt.grid(True)
for center in kmeans.cluster_centers_:
	center = center[:2]
	plt.scatter(center[0],center[1],marker = '^',c = 'red')
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")
	
plt.subplot(1,2,2) 
plt.scatter(X[:,2],X[:,3],c = pred, cmap=cm.Accent)
plt.grid(True)
for center in kmeans.cluster_centers_:
	center = center[2:4]
	plt.scatter(center[0],center[1],marker = '^',c = 'red')
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.show()


# The subplot on the left display petal length vs. petal width with data points colored by clusters, 
# and red markers indicate K-means cluster centers.
#  The subplot on the right show sepal length vs. sepal width similarly.
