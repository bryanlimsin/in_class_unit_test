# Writing unit test before writing actual python function
# Note to self: Write code in Spyder but run from gitbash because console in spyder not configured with virtual environment.


# Start of code
# Write function that takes 2 tuples of x and y to predict a 3rd y given a 3rd x

# Correction after I reviewed syntax of python
# Need to use indexing within tuples and lists

# Using method 1 that we learned in class on how to unit test a single predictor
def test_line_function(): # cannot have additional brackets or parenthesis within parameter but we can pre-define those

    from line_predictor_module import line_function # Need create file called line_predictor_module.py
    
    # Need the above to contain line_function()
    
    y3 = line_function((1, 2), (10, 20), 100)
    expected = 200 # I wrote my code such that it is easy predict the next variable 
    assert y3 == expected

    