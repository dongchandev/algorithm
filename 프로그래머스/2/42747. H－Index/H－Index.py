def solution(citations):
    citations.sort(reverse=True)
    h_idx = 0

    for i, citation in enumerate(citations):
        if citation < i + 1:
            break
        h_idx = i + 1
    return h_idx