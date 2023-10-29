FORMAT = "%Y/%m/%d %H:%M:%S"


MAX_ROWS = 30
MAX_COLUMNS = 3

SPREADSHEET_BODY = {
    'properties': {
        'title': 'Отчет от',
        'locale': 'ru_RU',
    },
    'sheets': [
        {
            'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': 'Лист1',
                'gridProperties': {
                    'rowCount': MAX_ROWS,
                    'columnCount': MAX_COLUMNS,
                },
            },
        },
    ],
}
TABLE_HEADER = [
    ['Отчет от', None],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]
