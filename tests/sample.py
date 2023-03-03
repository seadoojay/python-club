import json

def create_properties_file(json_file, properties_file):
    with open(json_file) as f:
        data = json.load(f)

    for cluster, cluster_data in data.items():
        properties = {}
        for k, v in cluster_data.items():
            if isinstance(v, list):
                properties[k] = sorted(list(set(v)))
            else:
                properties[k] = [v]

        with open(f"{properties_file}_{cluster}.properties", 'w') as f:
            for k, v in properties.items():
                line = f"{k} = {' '.join(str(item) for item in v)}\n"
                f.write(line)
