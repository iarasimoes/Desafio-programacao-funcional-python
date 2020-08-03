from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
        'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
        'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
        'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
        'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
        'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
        'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
        'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
        'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
        'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
        'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564627800, 'start': 1564626000}
]


def call_calculator(start, end):
    fixed_fee = 0.36
    call_minute = 0.09

    value = 0

    start = datetime.fromtimestamp(start)
    end = datetime.fromtimestamp(end)

    call_duration = end - start

    if start.hour in range(6, 22):
        minutes_fixed_fee = int(call_duration.total_seconds()/60)
        value = (minutes_fixed_fee*call_minute)+fixed_fee
    else:
        value = fixed_fee
    return round(value, 2)


def classify_by_phone_number(records):
    results = []
    for record in records:
        value = call_calculator(record['start'], record['end'])
        item = {'source': record['source'], 'total': value}
        if not any(record['source'] == result['source'] for result in results):
            results.append(item)
        else:
            for result in results:
                if result['source'] == item['source']:
                    result['total'] = round(result['total'] + item['total'], 2)
    return sorted(results, key=lambda k: k['total'], reverse=True)


classify_by_phone_number(records)
