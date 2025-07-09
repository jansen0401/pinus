import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def run_clustering():
    df = pd.read_excel("data/pinus_data.xlsx")
    df['Diameter'] = df['Circumference (m)'] / 3.1416
    data = df[['Diameter', 'Douglas Fir']].dropna()

    model = KMeans(n_clusters=3, random_state=42)
    data['Cluster'] = model.fit_predict(data)

    plt.scatter(data['Diameter'], data['Douglas Fir'], c=data['Cluster'], cmap='viridis')
    plt.xlabel('Diameter (m)')
    plt.ylabel('Tinggi Pohon (m)')
    plt.title('Clustering Pinus (K-Means)')
    plt.savefig("clustering/cluster_plot.png")
    plt.show()
