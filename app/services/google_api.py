from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import settings
from .constants import (FORMAT,
                        MAX_ROWS,
                        MAX_COLUMNS,
                        SPREADSHEET_BODY,
                        TABLE_HEADER)


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = SPREADSHEET_BODY
    spreadsheet_body['properties']['title'] = f'Отчет от {now_date_time}'
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheet_id = response['spreadsheetId']
    spreadsheet_url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}'
    return spreadsheet_id, spreadsheet_url


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
    now_date_time = datetime.now().strftime(FORMAT)
    TABLE_HEADER[0][1] = now_date_time
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
        raise ValueError("Данные превышают максимальные размеры таблицы")
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
