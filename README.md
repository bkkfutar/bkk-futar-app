# BKK Futár Alkalmazások (PWA)

Ez a projekt két webes alkalmazást tartalmaz a BKK járatainak valós idejű követésére és járművezetői szimulációra.

## Alkalmazások

### 1. BKK Tervező (`/planner`)
- **Célközönség:** Utasok
- **Funkciók:** Élő térkép, járatkereső, menetrendek, járművek követése.
- **Elérés:** Nyisd meg a `/planner/` mappát a böngészőben.

### 2. BKK Vezető (`/driver`)
- **Célközönség:** Járművezetők (szimuláció)
- **Funkciók:** Fedélzeti kijelző (Monitor) nézet, következő megálló, átszállások, menetidő.
- **Használat:** Válassz egy járművet a térképen, és automatikusan megnyílik a vezetői monitor nézet.
- **Elérés:** Nyisd meg a `/driver/` mappát a böngészőben.

## Telepítés (PWA)
Mindkét alkalmazás Progressive Web App (PWA) technológiát használ, így telepíthető telefonra:

1. Nyisd meg a központi oldalt (`index.html`) vagy a választott alkalmazást.
2. A böngésző menüjében válaszd a **"Hozzáadás a kezdőképernyőhöz"** vagy **"Telepítés"** opciót.
3. Az alkalmazás külön ikonként jelenik meg a telefonodon.

## Fejlesztés
- A fájlok szerkesztése után frissítsd a `sw.js` verziószámát a gyorsítótár törléséhez.
