#!/usr/bin/env python3
"""Multivariate Normal distribution"""
import numpy as np


class MultiNormal:
    """This class represents a multivariate normal distribution."""

    def __init__(self, data):
        """Sets mean and cov from data of shape (d, n)"""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = np.mean(data, axis=1, keepdims=True)
        centered = data - self.mean
        self.cov = np.matmul(centered, centered.T) / (n - 1)

    def pdf(self, x):
        """Calculates the PDF at a data point x of shape (d, 1)"""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.cov.shape[0]
        if x.shape != (d, 1):
            raise ValueError('x must have the shape ({}, 1)'.format(d))
        diff = x - self.mean
        det = np.linalg.det(self.cov)
        inv =  np.linalg.inv(self.cov)
        exponent = -0.5 * np.matmul(np.matmul(diff.T, inv), diff)
        norm = 1 / np.sqrt((2 * np.pi) ** d * det)
        return float(norm * np.exp(exponent))