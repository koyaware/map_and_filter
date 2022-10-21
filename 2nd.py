scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def filter_scores(score):
    return list(filter(lambda i:i > 75,score))
print(filter_scores(scores))