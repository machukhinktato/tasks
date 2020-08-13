def bank_deposit(deposit, duration):
    """ function which calculating and shown actual gain of deposit"""
    deposit_gain = 0
    tiny_gain = {
        'begin_sum': deposit, 'end_sum': deposit_gain, '6': 5, '12': 6, '24': 5
    }
    standard_gain = {
        'begin_sum': deposit, 'end_sum': deposit_gain, '6': 6, '12': 7, '24': 6.5
    }
    maximal_gain = {
        'begin_sum': deposit, 'end_sum': deposit_gain, '6': 7, '12': 8, '24': 7.5
    }
    if deposit < 10000:
        if str(duration) in tiny_gain:
            deposit += int(deposit / 100 * tiny_gain[str(duration)])
            tiny_gain['end_sum'] = deposit
            return tiny_gain['end_sum']
        else:
            raise ValueError
    elif 10000 <= deposit < 100000:
        if str(duration) in standard_gain:
            deposit += int(deposit / 100 * standard_gain[str(duration)])
            standard_gain['end_sum'] = deposit
            return standard_gain['end_sum']
        else:
            raise ValueError
    else:
        if str(duration) in maximal_gain:
            deposit += int(deposit / 100 * maximal_gain[str(duration)])
            maximal_gain['end_sum'] = deposit
            return maximal_gain['end_sum']
        else:
            raise ValueError


# alternative option

def get_percent(amount, months):
    """in touch with percentage"""
    if months not in [6, 12, 24]:
        return False

    rates = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    )

    for rate in rates:
        if rate['begin_sum'] <= amount < rate['end_sum']:
            return rate[months]

    return False


def deposit(amount, months):
    """summary of profit"""
    percent = get_percent(amount, months)
    if not percent:
        print('tariff is not liquid')

    total = amount
    for _ in range(months):
        profit = total * percent / 100 / 12
        total += profit

    return (round(total, 2))


if __name__ == '__main__':
    print(bank_deposit(1000000, 12))
    print(deposit(10000, 24))