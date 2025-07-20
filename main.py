# main.py
# Questo è il punto di ingresso per le nostre automazioni Speckle.

from speckle_automate import (
    AutomationContext,
    execute_automation,
    automation_run,
)

@automation_run
def run_function(ctx: AutomationContext) -> None:
    """
    Questa è la funzione principale che Speckle eseguirà ad ogni commit.
    Da qui, orchestreremo le nostre diverse validazioni.
    """
    print("Automazione avviata...")

    # 1. Carica il modello dal commit che ha attivato l'automazione
    root_object = ctx.get_commit_root()
    print(f"Ricevuto commit dallo stream: {ctx.stream_id}")
    print(f"Oggetto radice di tipo: {root_object.speckle_type}")

    # --- QUI INIZIEREMO A INSERIRE LE NOSTRE REGOLE ---
    # Esempio:
    # rule_1_result = check_room_classification(root_object)
    # if not rule_1_result:
    #     ctx.mark_run_failed("Validazione fallita: Regola #1 violata.")
    #     return

    # Se tutte le regole passano
    ctx.mark_run_succeeded("Tutte le validazioni sono state superate con successo!")
    print("Automazione completata.")

# =================================================================================
# Le funzioni per le singole regole verranno definite qui sotto.
# Ad esempio:
#
# def check_room_classification(root_object):
#     """Controlla la Regola #1: Classificazione delle stanze."""
#     # ... logica della regola ...
#     return True # o False
# =================================================================================

if __name__ == "__main__":
    # Questa parte serve per testare lo script localmente in futuro.
    execute_automation(run_function)

