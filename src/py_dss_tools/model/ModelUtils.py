# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : ModelUtils.py
# @Software: PyCharm

from py_dss_interface import DSS
import pandas as pd

class ModelUtils:

    def __init__(self, dss: DSS):
        self._dss = dss

    def is_element_in_model(self, element_class: str, element_name: str):
        element_class = element_class.lower()
        element_name = element_name.lower()
        elements_list = [e.lower() for e in self._dss.circuit.elements_names]
        element_full_name = f"{element_class}.{element_name}"
        if element_full_name not in elements_list:
            raise ValueError(f"Model does not have the {element_class}.{element_name}")

    def disable_elements_type(self, element_type: str):
        self._dss.text(f"batchedit {element_type}..* enabled=false")