from dataclasses import dataclass
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tool import tool
from decimal import Decimal

@dataclass
class Finace:
    @staticmethod
    def calc_jurus(time:int , saldo:Decimal, jurus: Decimal) -> Decimal:
        return saldo(1 +jurus)**time