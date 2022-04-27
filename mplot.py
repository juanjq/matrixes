import numpy as np
import matplotlib.pyplot as plt

import httpimport
with httpimport.remote_repo(['plt_config'], 'https://raw.githubusercontent.com/juanjq/matplotlib_configuration/main'):
     import plt_config
        
def plot(M,cmap = 'bwr'):        
        
    plt_config.simple()

    fig, ax = plt.subplots(figsize=(4,4))

    minmax = max([abs(np.amax(M)),abs(np.amin(M))])
    plot   = ax.imshow(M,cmap=cmap,vmin=-minmax,vmax=minmax)
    plt.colorbar(plot)

    ax.axis('off')