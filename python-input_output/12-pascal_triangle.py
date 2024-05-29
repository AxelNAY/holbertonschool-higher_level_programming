"""function to make a Pascal triangle of n"""


def pascal_triangle(n):
    """Make a list of lists of integers representing
    the Pascal's triangle of n.

    Arg:
        n (int): the height of the triangle.

    Return:
        the Pascal triangle."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
