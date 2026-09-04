try:
    import imp  # This module was removed in Python 3.12+
    print("Le module 'imp' a été importé avec succès. Ce script est compatible avec votre version de Python (probablement Python < 3.12).")
    # Example usage (will also work if import succeeds)
    # For a simple check, just the import is sufficient to demonstrate the incompatibility.
    # finder = imp.find_module("os")
    # print(f"imp.find_module('os') succeeded: {finder}")
except ImportError:
    print("Erreur: Le module 'imp' n'a pas pu être importé. Ce script n'est pas compatible avec votre version de Python (probablement Python >= 3.12).")
except Exception as e:
    print(f"Une erreur inattendue est survenue: {e}")
