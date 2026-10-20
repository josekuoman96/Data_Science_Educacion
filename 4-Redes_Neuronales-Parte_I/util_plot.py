import matplotlib.pyplot as plt
import numpy as np

def plot_region_classifier(X, y, model, pad=5):
    x1_min, x1_max = np.min(X[:,0])-pad, np.max(X[:,0]+pad)
    x2_min, x2_max = np.min(X[:,1])-pad, np.max(X[:,1]+pad)
    xx1, xx2 = np.meshgrid(
        np.linspace(x1_min, x1_max, 300),
        np.linspace(x2_min, x2_max, 300)
    )
    
    yhat = model.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    yhat = np.where(yhat < 0.5, 0, 1)
    yhat = yhat.reshape(xx1.shape)

    X_class0 = X[np.argwhere(y==0).ravel()]
    X_class1 = X[np.argwhere(y==1).ravel()]
    
    plt.scatter(X_class0[:,0], X_class0[:,1], c='skyblue', marker='o', edgecolors='k')
    plt.scatter(X_class1[:,0], X_class1[:,1], c='tomato', marker='o', edgecolors='k')
    plt.contourf(xx1, xx2, yhat, alpha=.3, cmap='coolwarm')
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max);