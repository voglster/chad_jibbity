def process_data(d):
    result = []
    if "items" in d and len(d["items"]) > 0:
        for i in d["items"]:
            if "name" in i and "value" in i:
                n = i["name"]
                v = float(i["value"])
                if v > 10:
                    result.append((n, v))
        result = sorted(result, key=lambda x: x[1], reverse=True)
    return result
