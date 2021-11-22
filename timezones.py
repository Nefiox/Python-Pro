from datetime import datetime
import pytz


bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print('Bogotá: ', bogota_date.strftime('%d/%m/%Y, %H:%M:%S'))


mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print('México: ', mexico_date.strftime('%d/%m/%Y, %H:%M:%S'))


argentina_timezone = pytz.timezone("America/Argentina/Buenos_Aires")
argentina_date = datetime.now(argentina_timezone)
print('Argentina: ', argentina_date.strftime('%d/%m/%Y, %H:%M:%S'))