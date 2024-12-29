## Introduzione

L'architettura implementata è una pipeline modulare che permette di eseguire una serie di trasformazioni e analisi su un testo, passando il risultato da un modulo all'altro in modo sequenziale.

## Funzionamento della Pipeline

Il file `pipeline.py` gestisce l'esecuzione della pipeline. Ogni modulo implementa una funzionalità specifica e la pipeline le collega in sequenza per elaborare il testo. La pipeline prende un testo di input, lo processa attraverso ogni modulo e restituisce il risultato finale.

### Struttura della Pipeline

La classe principale che gestisce la pipeline è `Pipeline`.

1. **Caricamento dei moduli dalla configurazione**:  
   La pipeline è configurata tramite un file YAML (`pipeline_config.yaml`). Questo file definisce i moduli da utilizzare nella pipeline, il loro ordine e i parametri specifici da passare ai costruttori dei moduli.

2. **Esecuzione della pipeline**:  
   Il metodo `execute` della classe `Pipeline`:
   - Prende in input un testo.
   - Lo passa attraverso ogni modulo, eseguendo le operazioni previste.
   - Restituisce il risultato finale, che include il testo originale, il testo processato e le entità estratte.

3. **Validazione dell'input e dell'output**:  
   Il codice include i seguenti controlli:
   - **Validazione dell'input**: Ogni modulo riceve un testo di tipo `str` e, se il tipo di input non è corretto, viene sollevata un'eccezione.
   - **Validazione dell'output**: Viene verificato che l'output, processato da ogni modulo, sia del tipo corretto (una stringa). Se l'output è di un tipo errato, viene sollevata un'eccezione.


### Gestione degli Errori

La pipeline è progettata per gestire eventuali errori. Se uno dei moduli fallisce, l'errore viene catturato e sollevato, interrompendo l'esecuzione della pipeline.

### Testing

I test sono stati implementati per verificare che la pipeline funzioni correttamente. I test principali includono:
- **Test di esecuzione della pipeline**: Verifica che la pipeline esegua correttamente tutti i moduli, concatenandoli e producendo un output valido.
- **Test di validazione dell'input**: Verifica che venga sollevata un'eccezione se l'input non è del tipo corretto (ad esempio, se viene passato un intero invece di una stringa).
- **Test di validazione dell'output**: Verifica che venga sollevata un'eccezione se un modulo restituisce un tipo di dato errato (ad esempio, se restituisce un intero invece di una stringa).