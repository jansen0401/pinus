from vision.capture_image import capture_image
from clustering.kmeans_clustering import run_clustering

if __name__ == "__main__":
    print("Menangkap gambar dari kamera...")
    capture_image()

    print("Menjalankan Clustering K-Means...")
    run_clustering()
