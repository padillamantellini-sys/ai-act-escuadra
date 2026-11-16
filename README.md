# AI Act: Escuadra

Juego web personal para estudiar el Reglamento (UE) 2024/1689 (AI Act). Uso privado de estudio.
**No es asesoramiento jurídico.** Las preguntas son material de repaso y pueden contener errores; el estado normativo
(p. ej. Omnibus digital de IA) debe contrastarse con EUR-Lex/BOE/AESIA. Marcar dudas como `[VERIFICAR]`.

## Estructura
- `src/template.html` — HTML, CSS y lógica del juego (con marcadores `//@@INC` y `//@@ASSET`).
- `data/` — banco de preguntas y fichas de repaso, por capas. **Solo se AÑADE al final**: las claves de progreso
  (`localStorage`) dependen del orden de las preguntas.
- `assets/` — imágenes en base64 (fondos, soldados, enemigos, barricada, pergamino).
- `build.py` — une todo en `dist/index.html` (un solo archivo).
- `tests/` — bot de dificultad con Playwright.

## Uso
```
python3 build.py
open dist/index.html
```
Regla: tras cualquier cambio, ejecutar `build.py` y subir también `dist/index.html`.

## Pendiente
Ver Issues (validación con guías AESIA, parche móvil en juegos antiguos, nuevas preguntas, `[VERIFICAR]`).
