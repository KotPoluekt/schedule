import schedule
import requests

def greetings():
    todos_dict = {
        "08:00": "drink coffee",
        "12:00": "sleep",
        "13:00": "work"
    }

    # print("Day's tasks")
    # for k, v in todos_dict.items():
    #     print(f'{k} -> {v}')

    response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
    data = response.json()
    btc_price = round(data.get('btc_usd').get('last'),2)

    print(f'Bitcoin last price = {btc_price}$')


def main():
    #greetings()

    # schedule.every(4).seconds.do(greetings)
    # schedule.every(4).minutes.do(greetings)
    #schedule.every().hour.do(greetings)
    schedule.every().day.at('22:41').do(greetings)


    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()