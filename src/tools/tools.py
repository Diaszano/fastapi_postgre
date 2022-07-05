#-----------------------
# BIBLIOTECAS
#-----------------------
from aiohttp import ClientSession
from datetime import datetime, timedelta
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class AssetService():
    @staticmethod
    async def day_summary(symbol:str) -> dict:
        async with ClientSession() as session:
            yesterday = datetime.today() - timedelta(days=1);
            url       = (
                "https://www.mercadobitcoin.net/api/"
                f"{symbol}/day-summary/"
                f"{yesterday.year}/{yesterday.month}/{yesterday.day}/"
            );
            response = await session.get(url);
            try:
                data   :dict = await response.json();
                retorno:dict = {
                    'lowest' : data['lowest'],
                    'highest': data['highest'],
                    'symbol' : symbol
                }
            except:
                retorno:dict = {
                    'lowest' : 0,
                    'highest': 0,
                    'symbol' : symbol
                }
            return retorno;
    
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------