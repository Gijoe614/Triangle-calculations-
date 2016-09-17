def is_triangle ( a, b, c ) :
    """Returns True if a, b, c can be a triangle"""

    return not ( ( a + b < c ) or (a + c < b ) or (b + c < a ))

def user_interface () :
    a = int ( raw_input ("Enter a ") )
    b = int ( raw_input ("Enter b ") )
    c = int ( raw_input ("Enter c ") )

    if is_triangle ( a, b, c ) :
        print a, b, c, "is a triangle"
    else :
        print a, b, c, "is not a triangle"


while True :
    user_interface ()
