

def convert(sample):
    sample = sample.split(',')
    sample[1] = float(sample[1])
    return sample[:2]

def filter_fn(sample):
    if sample is "":
        return False
    return True

def process_csv(text):
    text = text.decode().split('\n')[1:]
    text = filter(filter_fn,text)
    text = list(map(convert,text)) 
    return text
