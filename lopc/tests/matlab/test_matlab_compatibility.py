import unittest
from scipy.io import loadmat
import os
from lopc.lopc import lopc
from numpy.testing import assert_array_equal

_MATLAB_DATAFILE = os.path.join(os.path.dirname(__file__), 'lopc-matlab-input-output.mat')

class TestMatlab(unittest.TestCase):

    def setUp(self):
        matlab = loadmat(_MATLAB_DATAFILE)

        self._input = matlab['peakProtein_n']
        self._thres = matlab['thres']
        self._output_correlation = matlab['re_2']
        self._output_p_values = matlab['pe_2']

    def test_compatibility_with_demo_script(self):
        answer_correlation, answer_p = lopc(self._input.T, self._thres)
        assert_array_equal(answer_correlation, self._output_correlation)
        assert_array_equal(answer_p, self._output_p_values)




