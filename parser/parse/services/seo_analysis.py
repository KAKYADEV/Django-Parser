def seo_counter(result):
    seo_score = 0

    if result['title'] != "No title found":
        title_score = 1
        seo_score += 1
    else:
        title_score = 0

    if result['description'] != "No description found":
        description_score = 1
        seo_score += 1
    else:
        description_score = 0

    if result['keywords'] != "No keywords found":
        keywords_score = 1
        seo_score += 1
    else:
        keywords_score = 0

    header_count = 0
    for header in result['headers']:
        if header == "No headers found":
            break
        else:
            header_count += 1
    if header_count == len(result['headers']):
        header_score = 1
        seo_score += 1
    else:
        header_score = 0


    imgs_count = 0
    if result['images'] == ["No images found"]:
        imgs_score = 0
    else:
        for img in result['images']:
            if img['alt'] == "No alt text found":
                break
            else:
                imgs_count += 1
        if imgs_count == len(result['images']):
            imgs_score = 1
            seo_score += 1
        else:
            imgs_score = 0

    score = {
        'title_score' : title_score,
        'description_score' : description_score,
        'keywords_score' : keywords_score,
        'header_score' : header_score,
        'imgs_score' : imgs_score,
        'seo_score' : seo_score,
    }

    return score

def img_storage(result, score):
    imgs = []
    if score == 1:
        for img in result['images']:
            if len(imgs) < 2:
                img['status'] = "good"
                imgs.append(img)
            else:
                break
    else:
        for img in result['images']:
            if img['alt'] == "No alt text found" and img['alt'] not in imgs:
                img['status'] = "bad"
                imgs.append(img)
            elif img['alt'] != "No alt text found" and (len(imgs) == 0 or imgs[0]['alt'] == "No alt text found"):
                img['status'] = "good"
                imgs.append(img)
            if len(imgs) == 2:
                break
            
    return imgs
