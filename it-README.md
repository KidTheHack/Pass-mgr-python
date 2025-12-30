---
title: Password manager in python
---

# Introduzione:
Questo è il mio **password manager** scritto in python, è un progetto
molto minimalista che usa solo la libreria **cryptography** con la 
classe **Fernet**, per le funzioni di **crittografia** indispensabili
al funzionamento, e **InvalidToken** per gestire eventuali eccezioni
su chiavi non valide. 
A seguire trovate una rapida guida all'utilizzo, e se siete 
interessati sul mio [sito](https://kid-hack.com "Il mio sito") 
troverete una guida più dettagliata, su com'è strutturato il progetto
nei minimi dettagli.
Spero vi possa interessare ed essere utile, non esitate a conttatarmi
per qualsiasi cosa, qui su Github o ai contatti che trovate sul mio
[sito](https://kid-hack.com "Il mio sito").

# Funzionalità implementate:
* Creazione di nuove chiavi e password file.
* Caricamento di chiavi e password file già esistenti.
* Decriptazione dei servizi presenti.
* Gestione dei password file:
    * Lista dei servizi presenti.
    * Aggiunta di nuovi servizi.
    * Eliminazione di servizi.

# Utilizzo:
Per prima cosa bisogna generare o caricare una chiave, creare o
caricare un password file, dopo di che è possibile utilizzare tutte
le altre funzionalità.

## Opzioni:
1. Genera nuove chiavi per la **cifratura** dei file con le password.
2. Carica chiavi già esistenti.
3. Crea nuovi password file **cifrati**.
4. Carica password file già esistenti.
5. Aggiunge nuovi servizi al password file caricato.
6. Genera una lista di tutti i servizi presenti nel file.
7. Consente di ottenere lo username e la password salvata in un servizio.
8. Elimina un servizio.
