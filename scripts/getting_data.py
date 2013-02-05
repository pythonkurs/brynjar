#!/usr/bin/env python
import sys
sys.path.append("../")
from brynjar.session2 import get_esc_repair_frac_NYCT

frac = get_esc_repair_frac_NYCT()
print frac
