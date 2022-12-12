import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os
os.chdir(r'E:\BS Teaching\Fall2022\IDS\PyProgs\CSV_Files')
data = pd.read_csv("Kmeans_dataset.csv")
# print(data.head())
f1 = np.array(data['Income'])
f2 = np.array(data['SpendingScore'])
################# PLOT ############
# sns.relplot(x=f1, y=f2, data = data)
# plt.show()
#### finding optimal number of clusters using the elbow method ##
features=list(zip(f1, f2))
# wcss_list = []  # Initializing the list for the values of WCSS
# # # Using for loop for iterations from 1 to 10.
# for i in range(1, 11):
#      kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42) # init='random'
#      kmeans.fit(features)
#      wcss_list.append(kmeans.inertia_) # Sum of squared distances of samples to their closest cluster cente
# print(wcss_list)
# plt.plot(range(1, 11), wcss_list)
# plt.title('The Elobw Method Graph')
# plt.xlabel('Number of clusters(k)')
# plt.ylabel('wcss_list')
# plt.show()
########## Train Model #########
kmeans = KMeans(n_clusters=5, init='k-means++', random_state= 46)
kmeans.fit(features)
# print(kmeans.labels_)
# print(kmeans.inertia_) # gives within-cluster sum of squares.
# print(kmeans.n_iter_)
# print(kmeans.cluster_centers_)
#### Plot Clusters #####
sns.relplot(x=f1, y=f2, s=100, data = data, style=kmeans.labels_)
plt.show()