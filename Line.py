import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle

class Line():
    """
        A class to store previous frame and calculate average 
        of the most recent line fit coefficients and updates internal smoothed coefficients
        fit_coeffs is a 3-element list of 2nd-order polynomial coefficients
    """
    def __init__(self, number_of_windows):
        self.n = number_of_windows
        self.detected = False
        self.A = []
        self.B = []
        self.C = []
        self.A_avg = 0.
        self.B_avg = 0.
        self.C_avg = 0.

    def get_fit(self):
        return (self.A_avg, self.B_avg, self.C_avg)

    def add_fit(self, fit_coeffs):
        # Coefficient queue full?
        q_full = len(self.A) >= self.n

        # Append line fit coefficients
        self.A.append(fit_coeffs[0])
        self.B.append(fit_coeffs[1])
        self.C.append(fit_coeffs[2])

        # Pop from index 0 if full
        if q_full:
            _ = self.A.pop(0)
            _ = self.B.pop(0)
            _ = self.C.pop(0)

        # Simple average of line coefficients
        self.A_avg = np.mean(self.A)
        self.B_avg = np.mean(self.B)
        self.C_avg = np.mean(self.C)
        return (self.A_avg, self.B_avg, self.C_avg)
