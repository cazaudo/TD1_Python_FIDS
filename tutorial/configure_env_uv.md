Pour configurer un nouveau projet avec une version spécifique de Python via uv dans PyCharm, vous avez deux options : l'interface graphique ou le terminal intégré.

## **Option 1 : Via l'interface de PyCharm (Recommandé)**

> 1. Ouvrez PyCharm et cliquez sur **New Project** (Nouveau projet).  
> 2. Choisissez le dossier de votre projet.  
> 3. Dans le menu déroulant **Environment type**, sélectionnez **uv**.  
> 4. Dans le champ **Base interpreter** (ou Python version), sélectionnez la version souhaitée.  
> 5. Si la version voulue n'est pas affichée, cliquez sur **Download executable** (Télécharger l'exécutable). uv va automatiquement télécharger et isoler cette version exacte de Python pour vous.  
> 6. Cliquez sur **Create** (Créer).

## **Option 2 : Via le Terminal de PyCharm**

Si vous préférez les lignes de commande ou si la version ne s'affiche pas dans l'interface, ouvrez le terminal intégré (Alt \+ F12 ou Option \+ F12) dans un dossier vide et tapez :

*`# 1. Initialiser le projet uv`*  
`uv init`

*`# 2. Verrouiller le projet sur une version spécifique (ex: 3.11 ou 3.12)`*  
`uv python pin 3.12`

*`# 3. Créer l'environnement virtuel avec cette version spécifique`*  
`uv venv`

PyCharm va détecter automatiquement le dossier .venv créé et vous proposera de l'associer comme interpréteur du projet.

