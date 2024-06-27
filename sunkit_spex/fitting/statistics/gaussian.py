import numpy as np


def chi_squared(data_y, model_y):
    """
    The form to optimise while fitting.

    * No error included here. *

    Parameters
    ----------
    data_y : `ndarray`
        The data to be fitted.

    model_y : `ndarray`
        The model values being fitted.

    Returns
    -------
    `float`
        The value to be optimized that compares the model to the data.
    """
    return np.sum((data_y - model_y)**2)