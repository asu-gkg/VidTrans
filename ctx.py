n = 20


def pred_text(result, i):
    res = ""
    for i in range(i - n, i):
        if 1 <= i < len(result['segments']) - 1:
            res += result['segments'][i - 1]['text']
    return res


def succ_text(result, i):
    res = ""
    for i in range(i + 1, i + n):
        if 1 <= i < len(result['segments']) - 1:
            res += result['segments'][i - 1]['text']
    return res
