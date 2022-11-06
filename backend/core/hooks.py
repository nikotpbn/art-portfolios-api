def custom_preprocessing_hook(endpoints):
    filter = []
    # your modifications to the list of operations that are exposed in the schema
    for (path, path_regex, method, callback) in endpoints:
        if '/api/arts/' in path and method == 'GET':
            filter.append((path, path_regex, method, callback))
        if '/api/arts/\{id\}/' in path and method == 'GET':
            filter.append((path, path_regex, method, callback))
        pass
    return filter