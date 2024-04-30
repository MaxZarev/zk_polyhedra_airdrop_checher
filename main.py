import requests
import json


def main():

    with open('wallets.txt', 'r') as file:
        wallets = file.read().split('\n')

    balances = []
    total = 0

    for address in wallets:

        url = f'https://pub-88646eee386a4ddb840cfb05e7a8d8a5.r2.dev/2nd_data/{address[2:5].lower()}.json'  # replace this URL with the actual URL you are targeting
        response = requests.get(url)

        data = json.loads(response.text)

        for item in data:
            if item.lower() == address.lower():
                amount = int(data[item]['amount'], 16) / 10 ** 18
                total += amount
                balances.append(f'{address}:{amount}')
                print(f'{address}: {amount}, total: {total}')
                break

    # записать итоговый список в текстовый файл
    with open('balances.txt', 'w') as file:
        file.write('\n'.join(balances))

if __name__ == '__main__':
    main()
