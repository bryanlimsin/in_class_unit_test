# Write actual function for predictor
# Simple y = mx + c
# In our predictor function, c == 0 since we are just finding gradient m


# Construct the gradient from the 2 inputs
def find_gradient(a, b):
    # defining variables via indexing
    x1 = a[0]
    x2 = b[0]

    y1 = a[1]
    y2 = b[1]
    
    # find the gradient
    m = (y2 - y1)/(x2 - x1) # Rise over run
    return m

def line_function(a, b, x3):
    
    # get the gradient into this function from previously defined - find_gradient() function
    gradient_m = find_gradient(a, b)
    
    # do predictor by the typical y = mx
    
    y3 = gradient_m * x3
    return y3
    
    
# The following code just helps me manually test at command line that my function works
if __name__ == "__main__":
    final_answer = line_function((1, 2), (10, 20), 100)
    print(final_answer)
    