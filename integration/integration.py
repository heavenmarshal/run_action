if __name__ == '__main__':
    with open('/etc/secrets/some_token', 'r') as fptr:
        token = fptr.read()
    print(token)
