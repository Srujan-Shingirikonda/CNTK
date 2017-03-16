# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# ==============================================================================

__version__ = '2.0.beta12.0+'

import os
import numpy as np

from . import cntk_py

#
# Bubble the below namespaces to cntk root namespace.
#
from .core import *
from .ops import *
from .device import *
from .train import *
from .learners import *
from .losses import *
from .metrics import *
from .initializer import *
from .sample_installer import install_samples

#
# Import the actual modules.
#
from . import debugging
from . import logging
from . import internal
from . import utils
from . import ops
from . import io
from . import layers

# To __remove__
# from .io import *
# from .learner import *
# from .utils import *
# from .layers import *
# End of to remove

DATATYPE = np.float32
InferredDimension = cntk_py.InferredDimension
