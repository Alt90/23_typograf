import re


def review_text(text):
    result_text = re.sub(r"([\']+)(.*?)\1", r'«\2»', text)
    result_text = re.sub(r"([\"]+)(.*?)\1", r'«\2»', result_text)
    result_text = result_text.replace("-", '—')
    result_text = re.sub(r"—(\d+)", r'-\1', result_text)
    return(result_text)