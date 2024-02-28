
def websitePagination(urls, pageSize, page):
    start_index = (page - 1) * pageSize
    end_index = start_index + pageSize
    return urls[start_index:end_index]
