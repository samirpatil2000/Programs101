import os
import sys


try:
    print("s")
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    x = [exc_type, fname, exc_tb.tb_lineno]
