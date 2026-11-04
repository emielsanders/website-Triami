# Playground

- `local-blueprint.json`: voor de lokale Playground CLI (mounts, zie PROJECT.md).
- `blueprint.json` (nog te maken zodra er een GitHub-repo is): zelfde stappen, maar `installTheme` met `{"resource":"url","url":"https://raw.githubusercontent.com/<org>/<repo>/main/dist/triami.zip"}` en `importWxr` met de raw-URL van de WXR. Openen met `https://playground.wordpress.net/?blueprint-url=<raw-url-van-blueprint.json>`.
- Tot die tijd: `python3 tools/blueprint.py` maakt `dist/playground-url.txt` met alles inline (thema + pagina's in de URL zelf).
