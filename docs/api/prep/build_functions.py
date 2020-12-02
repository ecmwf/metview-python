import yaml

fn = []


with open("/Users/sandor/git/metview/share/metview/etc/FunctionList.txt", "r") as f:
    header_done = False
    name = None
    dtype = None
    desc = {}
    for line in f:
        if not header_done and line.startswith("-------"):
            header_done = True
            continue
        if header_done:
            line = line.strip()
            if not name:
                name = line
            else:
                if line.startswith("type: "):
                    dtype = line[len("type: "):]
                elif line.startswith("desc: "):
                    line = line[len("desc: "):]
                    v = line.split("]")
                    group = v[0][1:]
                    desc[group] = v[1].strip() 
                else:
                    desc_main = ""
                    if desc: 
                        gr = list(desc.keys())[0]
                        desc_main = desc[gr]
                    r = {name: {"type": dtype, "category": desc, "desc": desc_main}}
                    fn.append(r)
                    # print("name={} type={} desc={}".format(name, dtype, desc ))
                    name = line
                    dtype =None
                    desc = {}

with open("test_func.yaml", "w") as f:
    yaml.dump(fn, f, default_flow_style=False)
