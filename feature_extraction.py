def extract_features_from_url(url):
    features = []
    features.append(len(url))                     # Feature 1: Length of URL
    features.append(url.count('@'))               # Feature 2: Number of '@'
    features.append(url.count('-'))               # Feature 3: Number of '-'
    features.append(url.startswith('https'))      # Feature 4: HTTPS (True/False)
    return features