def credentials_():
    credentials={}
    with open("D:\\InstaBot\\credentials.txt",'r')as credentials_file:
        for line in credentials_file:
           key, value = line.split(':')
           credentials[key] = value.strip()

    return credentials