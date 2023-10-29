from datetime import datetime

FORMAT = "%Y/%m/%d %H:%M:%S"

NOW_DATE_TIME = datetime.now().strftime(FORMAT)

MAX_ROWS = 30
MAX_COLUMNS = 3

SPREADSHEET_BODY = {
    'properties': {
        'title': f'Отчет от {NOW_DATE_TIME}',
        'locale': 'ru_RU',
    },
    'sheets': [
        {
            'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': 'Лист1',
                'gridProperties': {
                    'rowCount': 100,
                    'columnCount': 3,
                },
            },
        },
    ],
}
TABLE_HEADER = [
    ['Отчет от', NOW_DATE_TIME],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]
