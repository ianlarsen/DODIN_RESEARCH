def filter_relevant_items(items, keywords):
    relevant = []
    for item in items:
        content = (item.get("title", "") + " " + item.get("description", "")).lower()
        for kw in keywords:
            if kw.lower() in content:
                relevant.append(item)
                break
    return relevant