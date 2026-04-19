#!/usr/bin/env python3.10
import time
from datetime import date
t = time.time()
today_date = date.today()
print(f"Seconds since January 1, 1970: {t} or {t:.2e} in scientific notation")
print(today_date.strftime("%B %d %Y") )