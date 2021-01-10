import yaml

with open("test.yaml", "r") as f:
    conf = yaml.load(f, Loader=yaml.FullLoader)
    # conf = yaml.safe_load(f)
    # print(conf)
    # conf = parse_conf(conf)
    print(conf["item1"])
    print(conf["item2"])