# 7. Create a structured array representing a position (x,y) and a color (r,g,b)

import numpy as np

structured_array = np.array([('x', 9, 81.0), ('y', 3, 27.0)],
                            dtype=[('r', '4'), ('g', '115'), ('b', '0')])
