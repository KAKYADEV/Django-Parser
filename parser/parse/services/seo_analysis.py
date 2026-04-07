def title_score_counter(result):
    if result['title'] != "No title found":
        return 1
    else:
        return 0

def description_score_counter(result):
    if result['description'] != "No description found":
        return 1
    else:
        return 0

def keywords_score_counter(result):
    if result['keywords'] != "No keywords found":
        return 1
    else:
        return 0
    
def header_score_counter(result):
    headers = result['headers']
    if result['headers'] == ["No headers found"]:
        header_score = 0
        return 0
    else:
        h1_count = 0
        for header in headers:
            if header['level'] == 1:
                h1_count += 1
        if h1_count == 0:
            return 0
        elif h1_count == 1:
            header_score = 0.4
        else:
            header_score = 0.3

    maximum = 0
    for header in headers:
        if header['level'] > maximum:
            maximum = header['level']
    if maximum == 2:
        header_score += 0.2
    elif maximum >= 3:
        header_score += 0.3
    else:
        header_score += 0.1

    penalty = 0
    levels = []
    for header in headers:
        levels.append(header['level'])
    level_prev = levels[0]
    for level_cur in levels[1:]:
        if level_cur - level_prev == 1 or level_cur - level_prev == 0:
            level_prev = level_cur
        elif level_cur - level_prev > 1:
            penalty += 0.3
            level_prev = level_cur
        else:
            if penalty != 0:
                penalty -= 0.15
                level_prev = level_cur
            else:
                level_prev = level_cur
    if penalty == 0:
        header_score += 0.3
    elif penalty >= 0.3: 
        pass
    else:
        header_score += 0.3 - penalty

    return round(header_score, 1)

def imgs_score_counter(result):
    good_count = 0
    bad_count = 0
    if result['images'] == ["No images found"]:
        imgs_score = 0
    else:
        for img in result['images']:
            if img['alt'] == "No alt text found" or img['alt'] == "":
                bad_count += 1
            else:
                good_count += 1
        if bad_count == 0:
            imgs_score = 1
        elif bad_count == len(result['images']):
            imgs_score = 0
        else:
            imgs_score = 0.5
    return imgs_score

def seo_counter(result):
    title_score = title_score_counter(result)
    description_score = description_score_counter(result)
    keywords_score = keywords_score_counter(result)
    header_score = header_score_counter(result)
    imgs_score = imgs_score_counter(result)
    seo_score = title_score + description_score + keywords_score + header_score + imgs_score
    
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
    if result['images'] == ["No images found"]:
        imgs.append("No images found")
    else:
        if score == 1:
            for img in result['images']:
                if len(imgs) < 2:
                    img['status'] = "good"
                    imgs.append(img)
                else:
                    break
        elif score == 0.5:
            bad_count = 0
            for img in result['images']:
                if (img['alt'] == "No alt text found" or img['alt'] == "") and bad_count == 0:
                    img['status'] = "bad"
                    imgs.append(img)
                    bad_count += 1
                elif img['alt'] != "No alt text found" and img['alt'] != "":
                    if not imgs:
                        img['status'] = "good"
                        imgs.append(img)
                    else:
                        if imgs[0]['status'] == "good":
                            continue
                        else:
                            img['status'] = "good"
                            imgs.append(img)
                if len(imgs) == 2:
                    break
        else:
            for img in result['images']:
                if len(imgs) < 2:
                    img['status'] = "bad"
                    imgs.append(img)
                else:
                    break
            
    return imgs
