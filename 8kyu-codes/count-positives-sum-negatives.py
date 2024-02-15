def count_positives_sum_negatives(arr):
    if not arr:  # Verifica se a lista está vazia
        return []

    pos_numbers = 0
    neg_numbers = 0

    for number in arr:
        if number > 0:
            pos_numbers += 1
        elif number < 0:
            neg_numbers += number

    return [pos_numbers, neg_numbers]
