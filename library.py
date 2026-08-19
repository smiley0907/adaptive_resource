# ============================================================
# CELL 1: INSTALL REQUIRED LIBRARIES
# ============================================================

%pip install -q "qiskit>=1.1,<3" "qiskit-aer>=0.17,<0.18" pandas numpy matplotlib psutil

# ============================================================
# CELL 2: IMPORT LIBRARIES
# ============================================================

import os
import time
import platform
import statistics

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psutil

import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import MCXGate
from qiskit.circuit.library import ZGate
from qiskit_aer import AerSimulator

from IPython.display import display

print("Qiskit version     :", qiskit.__version__)
print("Platform           :", platform.platform())
print("Python version     :", platform.python_version())
print("Logical CPUs       :", psutil.cpu_count(logical=True))
print("Physical CPUs      :", psutil.cpu_count(logical=False))
