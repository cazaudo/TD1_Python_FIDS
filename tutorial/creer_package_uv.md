Pour créer un package Python avec [uv](https://www.docstring.fr/blog/quest-ce-que-uv-en-python/), la méthode la plus rapide consiste à utiliser la commande **uv init \--lib \<nom\_du\_package\>**. Cet outil moderne écrit en Rust remplace avantageusement Poetry et pip en initialisant instantanément une structure standardisée et prête à être publiée. \[1, 2\]

Voici le tutoriel étape par étape pour concevoir, coder et construire votre bibliothèque.

## ---

**1\. Initialiser le projet**

Ouvrez votre terminal et exécutez la commande suivante pour générer la structure dédiée aux bibliothèques (--lib) : \[1\]

`uv init --lib mon_package`  
`cd mon_package`

Le projet généré contient automatiquement : \[1, 2\]

> * Un dossier src/mon\_package/ pour votre code source.  
> * Un fichier pyproject.toml configuré avec le backend de build par défaut de uv.  
> * Un fichier README.md.

## **2\. Ajouter du code source**

Ouvrez le fichier principal généré dans src/mon\_package/hello.py et ajoutez votre logique métier :

`def dit_bonjour(nom: str) -> str:`  
    `return f"Bonjour {nom}, bienvenue dans mon package construit avec uv !"`

Modifiez ensuite le fichier src/mon\_package/\_\_init\_\_.py pour exposer votre fonction :

`from .hello import dit_bonjour`

`__all__ = ["dit_bonjour"]`

## **3\. Gérer les dépendances**

Si votre bibliothèque nécessite des packages externes (par exemple requests), ajoutez-les à l'aide de la commande uv add : \[2\]

`uv add requests`

Cette commande met automatiquement à jour la section \[project.dependencies\] de votre fichier pyproject.toml et verrouille les versions exactes dans le fichier uv.lock. \[2, 3\]

## **4\. Configurer les métadonnées**

Ouvrez le fichier pyproject.toml. Complétez les informations essentielles nécessaires avant toute distribution :

`[project]`  
`name = "mon_package"`  
`version = "0.1.0"`  
`description = "Une description courte de ma superbe bibliothèque"`  
`readme = "README.md"`  
`requires-python = ">=3.12"`  
`authors = [`  
    `{ name = "Votre Nom", email = "votre.email@example.com" }`  
`]`  
`dependencies = [`  
    `"requests>=2.31.0",`  
`]`

`[build-system]`  
`requires = ["hatchling"]`  
`build-backend = "hatchling"`

## **5\. Construire le package (Build)**

Pour compiler votre code sous forme d'archives distribuables (.whl et .tar.gz), exécutez simplement : \[4\]

`uv build`

Les fichiers générés sont placés dans le dossier dist/. Ils sont prêts à être partagés ou installés localement.

## **6\. Publier sur PyPI**

Une fois votre package construit, vous pouvez le téléverser directement sur PyPI ou sur un index privé grâce à la commande dédiée : \[2\]

`uv publish`

\[1\] [https://blog.stephane-robert.info](https://blog.stephane-robert.info/docs/developper/programmation/python/uv/)  
\[2\] [https://www.youtube.com](https://www.youtube.com/watch?v=l6WyNOIk0Ng)  
\[3\] [https://www.youtube.com](https://www.youtube.com/watch?v=Ey-Z7u-5oQQ&t=6)  
\[4\] [https://www.youtube.com](https://www.youtube.com/watch?v=81nERix3NpE&vl=fr-FR)