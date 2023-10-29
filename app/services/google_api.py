from aiogoogle import Aiogoogle

from app.core.config import settings
from .constants import (MAX_ROWS,
                        MAX_COLUMNS,
                        SPREADSHEET_BODY,
                        TABLE_HEADER)


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    service = await wrapper_services.discover('sheets', 'v4')
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=SPREADSHEET_BODY)
    )
    return response['spreadsheetId'], response['spreadsheetUrl']


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheetid: str,
        charity_projects: list,
        wrapper_services: Aiogoogle
) -> None:
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = [
        *TABLE_HEADER,
        *[list(map(
            str,
            [project.name,
             project.close_date,
             project.description])) for project in charity_projects]
    ]
    num_rows = len(table_values)
    num_cols = max(len(row) for row in table_values)
    if num_rows > MAX_ROWS or num_cols > MAX_COLUMNS:
        raise ValueError(f'Данные превышают максимальные размеры таблицы. '
                         f'Количество строк: {num_rows}, максимальное: {MAX_ROWS}. '
                         f'Количество столбцов: {num_cols}, максимальное: {MAX_COLUMNS}')
    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range=f'R1C1:R{num_rows}C{num_cols}',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
