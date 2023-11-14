tickets_collection = [i.strip() for i in input().split(', ')]
winning_items = ['@', '#', '$', '^']
left_part = ''
right_part = ''

for ticket in tickets_collection:
    no_match = True
    if len(ticket) == 20:
        left_part = ticket[:10]
        right_part = ticket[10:]
        for symbol in winning_items:
            for match in range(10, 5, -1):
                winning_combination = match * symbol
                if winning_combination in left_part \
                        and winning_combination in right_part:
                    if len(winning_combination) == 10:
                        print(f'ticket "{ticket}" - {match}{symbol} Jackpot!')
                        no_match = False
                        break
                    else:
                        print(f'ticket "{ticket}" - {match}{symbol}')
                        no_match = False
                        break

        if no_match:
            print(f'ticket "{ticket}" - no match')
    else:
        print('invalid ticket')
