import json

def main():
    with open('/etc/python-app-config/config.json', 'r') as fptr:
        config = json.load(fptr)
    print(config.get('message', 'no message'))

if __name__ == '__main__':
    main()
