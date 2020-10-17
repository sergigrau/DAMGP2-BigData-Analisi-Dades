"""
Aquest exercici demostra l´ús de la biblioteca aiohttp, i asyncio per a cridar de manera asíncrona dades
Sergi Grau
"""
import aiohttp
import asyncio
#Las corutinas declaradas con la sintaxis async/await definen funciones asicnronas 
async def peticion_asincrona(session, url):
    await asyncio.sleep(5)
    async with session.get(url) as response:
	#await permite al bucle de eventos gestionar otra corutina
#no se queda esperando obtener la respuesta y continúa la ejecución
        return await response.text()

#se debe registrar certificado SSL o pasar como argument a ClientSession 
#connector=aiohttp.TCPConnector(verify_ssl=False)
async def principal():
    async with aiohttp.ClientSession() as session:
        html = await peticion_asincrona(session, 'https://www.uoc.edu')
        print(html)
    print('se ejecuta sin esperar al codigo asíncrono')

if __name__ == '__main__':
    #el método run obtiene el bucle de eventos y pasa un primera corutina
    loop = asyncio.run(principal())
