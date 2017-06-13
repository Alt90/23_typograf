import re

NDSP = '\u00A0'


def review_text(text):
    result_text = re.sub(r"([\']+)(.*?)\1", r'«\2»', text)
    result_text = re.sub(r"([\"]+)(.*?)\1", r'«\2»', result_text)
    result_text = re.sub(r'(\s)-(\s)', '\1—\2', result_text)
    result_text = re.sub(r'(\d{1})\s*\(\s*(\d{3})\s*\)\s*(\d{3})\s—\s*(\d{2})\s*—\s*(\d{2})',
                         r'\1 (\2) \3{0}\4{0}\5'.format('-'), result_text)
    result_text = re.sub(r'(\d+)(\s+)(\b[а-яА-Яa-zA-Z]+\b)', r'\1{0}\3'.format(NDSP), result_text)
    result_text = re.sub(r' +', ' ', result_text)
    result_text = re.sub(r'\s{2,}', r'\n', result_text)
    result_text = re.sub(r'(\b[а-яА-Яa-zA-Z]{1,2}\b)(\s+)(\b[а-яА-Яa-zA-Z]+\b)', r'\1{0}\3'.format(NDSP), result_text)
    return(result_text)
