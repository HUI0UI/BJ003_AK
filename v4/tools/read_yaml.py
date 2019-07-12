import yaml


def read_yaml():
    with open("./page/login.yaml","r",encoding='utf-8') as f:
        return yaml.load(f)

if __name__ == '__main__':
    print(read_yaml())

    arrs = []
    for i in read_yaml().values():
        arrs.append((i.get("username"),i.get("pwd")))
    print(arrs)