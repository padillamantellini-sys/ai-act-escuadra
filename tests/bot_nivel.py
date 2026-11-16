import asyncio
from playwright.async_api import async_playwright
JS="""([li,acc])=>{startLevel(li);cancelAnimationFrame(raf);closeModal();let q=0,lost=0;
 for(let s=0;s<3600*3&&G.state==='play';s++){let tgt=G.scrolls[0]||G.enemies.filter(e=>e.y>0).sort((a,b)=>b.y-a.y)[0];if(tgt){G.px+=Math.max(-5.5,Math.min(5.5,tgt.x-G.px))}
  const before=G.correct;update(1/60);
  if(G.state==='quiz'){q++;const ok=Math.random()<acc;if(ok){G.correct++;G.score+=100;const u=UPG.filter(x=>x.ok(G));const sold=u.find(x=>x.t.startsWith('🪖'));(sold||u[0]).fn(G)}else{loseSoldier();if(G.lives<=0){G.state='over';break}}if(G.correct>=G.goal){G.state='won';break}G.state='play'}}
 return G.state+' t='+G.t.toFixed(0)+' lives='+G.lives+' q='+q}"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':820,'height':800})
        for f in ('escuadra12',):
            await pg.goto(f'file:///home/claude/game/{f}.html')
            res=[]
            for _ in range(6): res.append(await pg.evaluate(JS,[LI,.7]))
            print(f,res)
        await b.close()
asyncio.run(main())
