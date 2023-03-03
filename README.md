# python-club

<pre>
import json

def create_properties_file(json_file, properties_file):
    with open(json_file) as f:
        data = json.load(f)

    properties = {}
    for cluster_data in data.values():
        for k, v in cluster_data.items():
            if isinstance(v, list):
                if k in properties:
                    properties[k].extend(v)
                else:
                    properties[k] = v
            else:
                if k in properties:
                    if properties[k] != v:
                        raise ValueError(f"Inconsistent value for key '{k}' across clusters")
                else:
                    properties[k] = v

    with open(properties_file, 'w') as f:
        for k, v in properties.items():
            if isinstance(v, list):
                v = sorted(list(set(v)))
            line = f"{k} = {' '.join(str(item) for item in v)}\n"
            f.write(line)

</pre>
