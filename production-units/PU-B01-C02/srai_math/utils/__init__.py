import platform
import random
import sys

import numpy as np


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)


def environment_info():
    info = {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "numpy": np.__version__,
    }
    try:
        import pandas as pd
        info["pandas"] = pd.__version__
    except ImportError:
        info["pandas"] = None
    print(info)
    return info
