# Write actual function for predictor
# Simple y = mx + c
# In our predictor function, c == 0 since we are just finding gradient m


# Construct the gradient from the 2 inputs
def find_gradient(a, b):
    # defining variables via indexing
    x1 = a[0]
    x2 = b[0]

    y1 = a[1]
    y2 = b[2]
    
    # find the gradient
    m = (y2 - y1)/(x2-x1)
    return m