# BKK Futár Élő Térkép (PWA)

Ez egy webes alkalmazás a BKK járatainak valós idejű követésére, kifejezetten mobilra és asztali gépre optimalizálva.

## Funkciók
- **Élő térkép:** Járművek mozgása (busz, villamos, metró, stb.) 10 másodperces frissítéssel.
- **Utastájékoztató (Monitor):** Fedélzeti kijelzőt szimuláló nézet, amely mutatja a következő megállót, átszállásokat és a menetidőt.
- **Menetrend és Késés:** Részletes menetrend és aktuális késés kijelzése.
- **Útvonalrajzolás:** A kiválasztott járat útvonalának megjelenítése a térképen.
- **Keresés:** Járatok és megállók keresése.

## Telepítés Androidra (PWA)
Ez az alkalmazás Progressive Web App (PWA) technológiát használ, így telepíthető telefonra anélkül, hogy a Play Áruházból kellene letölteni.

1. **Fájlok előkészítése:**
   - Másold az `index.html`, `manifest.json` és `sw.js` fájlokat egy mappába.
   - Az alkalmazás működéséhez egy webszerverre van szükség (biztonsági okokból a böngészők nem telepítenek PWA-t közvetlenül fájlból).
   - *Alternatíva:* Töltsd fel a fájlokat egy ingyenes tárhelyre (pl. GitHub Pages, Netlify).

2. **Megnyitás telefonon:**
   - Nyisd meg a weboldal linkjét Google Chrome-ban Androidon.

3. **Hozzáadás a kezdőképernyőhöz:**
   - Érints a Chrome menüjére (három pötty a sarokban).
   - Válaszd az **"Alkalmazás telepítése"** vagy **"Hozzáadás a kezdőképernyőhöz"** opciót.
   - Az alkalmazás megjelenik a telefonod menüjében, mint egy normál applikáció.

## Használat
- **Térkép:** Húzd és nagyítsd a térképet. A járművekre kattintva részleteket láthatsz.
- **Monitor:** A jármű részleteinél kattints az "Utastájékoztató" gombra a teljes képernyős nézethez.
- **Menetrend:** A jármű részleteinél kattints a "Menetrend és Késés" gombra.

## Új Alkalmazások (Belső Használatra)

Az eredeti alkalmazás mellett két új modul is elérhető:

### 1. BKK Tervező (`/planner/`)
Itt lehet saját, egyedi útvonalakat tervezni és megállókat rögzíteni a térképen.
- Kattints a térképre megálló hozzáadásához.
- Nevezd el az útvonalat és mentsd el.
- Az itt létrehozott útvonalak megjelennek a Vezetői alkalmazásban.

### 2. BKK Vezető (`/driver/`)
Járművezetők számára készült felület (Monitor), amely a Tervezőben létrehozott útvonalakat használja.
- Indításkor válaszd ki a mentett útvonalat.
- A felület mutatja a következő megállót, a menetidőt és a térképet.
- Az "Indulás" gombbal lehet léptetni a megállókat.
