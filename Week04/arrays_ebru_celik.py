def replace_center_with_minus_one(n, m, d):

    if (m>n or m==0 or n==0 or d==0):
        print("Not acceptable")

    max_value = math.pow(10, 2) - 1
    my_array = np.arange(max_value + 1).reshape(n, n)

    my_array[m:, m:].reshape(n-m)

    return my_array
