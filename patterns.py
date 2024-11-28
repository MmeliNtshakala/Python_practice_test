
# TODO: Step 1 - return shape from user input (it can't be blank and must be a valid shape!)     
def get_shape():
    
    return ""


# TODO: Step 2 - return height from user input (it must be int!)
#       The maximum possible height must be 80
def get_height():
    
    return ""


# TODO: Step 3 Complete the required shapes below
#       with reference to the unittests
def draw_square(height):
    pass


def draw_triangle_reversed(height):
    pass


def draw_triangle(height):
    pass


def draw_triangle_multiplication(height):
    pass


def draw_pyramid(height):
    pass


def draw_triangle_prime(height):
    pass
         
                
# TODO: Step 4 - add support for other shapes
def draw(shape, height):
    if shape == "pyramid":
        draw_pyramid(height)



# TODO: Step 5 (standalone function) - Solve Pascal's Triangle
def pascal_triangle(n):
    """
    Generates Pascal's triangle and returns the final row as a list.

    Parameters:
    n (int): The row number of Pascal's triangle to generate (0-based index).

    Returns:
    list: The final row of Pascal's triangle as a list.

    Formula for Pascal's Triangle:
    Each element in Pascal's triangle can be calculated using the following formula:

    C(n, k) = n! / (k! * (n-k)!)

    Where:
    - n is the row number (0-based index)
    - k is the column number (0-based index)
    - C(n, k) represents the value at row n and column k in Pascal's triangle
    - n! represents the factorial of n

    To generate a row of Pascal's triangle, iterate over the columns from 0 to n.
    Calculate each element using the formula and store them in a list to form the row.
    Repeat this process for each row up to the desired row number.

    Example:
     * Input: n = 6
     * Output:
     *           1
     *         1   1
     *       1   2   1
     *     1   3   3   1
     *   1   4   6   4   1
     * 1   5  10   10  5   1
    """

    return ""


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    draw(shape_param, height_param)