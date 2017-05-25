import re


def review_text(text):
    result_text = re.sub(r"([\']+)(.*?)\1", r'«\2»', text)
    result_text = re.sub(r"([\"]+)(.*?)\1", r'«\2»', result_text)
    result_text = result_text.replace("-", '—')
    result_text = re.sub(r"—(\d+)", r'-\1', result_text)
    result_text = re.sub(r"(\d+) ", r'\1{}'.format('\u00A0'), result_text)
    result_text = re.sub(r' +', ' ', result_text)
    result_text = re.sub(r'(\b[^\W\d]{1,2})\s+\b', r'\1{}'.format('\u00A0'), result_text)
    result_text = re.sub(r'\s{2,}', r'\n', result_text)
    return(result_text)
