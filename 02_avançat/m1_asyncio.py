import asyncio
"""
asyncio és una biblioteca per escriure codi simultani mitjançant la sintaxi async / await.
s'utilitza com a base per a diversos marcs asíncrons de Python que proporcionen servidors web i de xarxa d'alt rendiment, biblioteques de connexions de bases de dades, cues de tasques distribuïdes, etc.
sol ser un ajust perfecte per al codi de xarxa estructurat d’alt nivell i lligat a IO.
@sergigrau
"""
async def principal():
    print('hola')
    await asyncio.sleep(1)
    print('món')

loop = asyncio.get_event_loop()
loop.run_until_complete(principal())