"""Bot de dificultad: 20 partidas por nivel (0-3) con un bot de 80 % de aciertos.
Uso: python3 build.py && python3 tests/bot_dificultad.py   (requiere playwright + chrome)"""
import asyncio, os
from playwright.async_api import async_playwright
JS = open(os.path.join(os.path.dirname(__file__), 'bot_nivel.py')).read().split('JS="""')[1].split('"""')[0]
URL = 'file://' + os.path.abspath('dist/index.html')
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get('CHROME') or None,args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 820, 'height': 800})
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto(URL)
        for L in (0, 1, 2, 3):
            w = T = 0
            for _ in range(20):
                r = await pg.evaluate(JS, [L, .8]); w += r.startswith('won'); T += int(r.split('t=')[1].split()[0])
            print(f'nivel {L+1}: victorias {w}/20, duración media {T/20:.0f} s')
        print('errores JS:', errs or 'ninguno')
        await b.close()
asyncio.run(main())
