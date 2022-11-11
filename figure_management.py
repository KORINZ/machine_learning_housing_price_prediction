from pathlib import Path
import matplotlib.pyplot as plt

IMAGES_PATH = Path() / "images" / "end_to_end_project"

# define the default font sizes
plt.rc('font', size=14)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)


class FigureManagement:

    @staticmethod
    def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
        IMAGES_PATH.mkdir(parents=True, exist_ok=True)
        path = IMAGES_PATH / f"{fig_id}.{fig_extension}"
        if tight_layout:
            plt.tight_layout()
        plt.savefig(path, format=fig_extension, dpi=resolution)
