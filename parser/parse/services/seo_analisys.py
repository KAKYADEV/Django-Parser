def seo_counter(result):
    seo_score = 0

    if result['title'] != "No title found":
        seo_score += 1
    if result['description'] != "No description found":
        seo_score += 1
    if result['keywords'] != "No keywords found":
        seo_score += 1

    header_count = 0
    for header in result['headers']:
        if header == "No header found":
            break
        else:
            header_count += 1
    if header_count == len(result['headers']):
        seo_score += 1

    imgs_count = 0
    for img in result['images']:
        if img['alt'] == "No alt text found":
            break
        else:
            imgs_count += 1
    if imgs_count == len(result['images']):
        seo_score += 1

    return seo_score