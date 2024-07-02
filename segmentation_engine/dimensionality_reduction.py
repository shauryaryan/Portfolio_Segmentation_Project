from sklearn.decomposition import PCA

def pca_reduction(data, n_components):
    pca = PCA(n_components=n_components)
    return pca.fit_transform(data)
