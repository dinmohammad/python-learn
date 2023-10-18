def raise_of_pow(base_url, pow_num):
    result = 1
    for item in range(pow_num):
        result = result * base_url
    return result

print( raise_of_pow(2,3) )