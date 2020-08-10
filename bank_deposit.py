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


if __name__ == '__main__':
    print(bank_deposit(1000000, 12))
