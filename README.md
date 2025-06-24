📐 Lesno Calculator

Lesno Calculator est une calculatrice graphique interactive développée en Python avec les bibliothèques pygame et pygame_gui.
Elle permet d'effectuer des opérations arithmétiques de base ainsi que des fonctions trigonométriques et logarithmiques.
L'interface utilisateur propose des boutons pour saisir les nombres, les opérateurs et les fonctions, et affiche le résultat à l'écran.
⚙️ Fonctionnalités

✅ Opérations de base : addition, soustraction, multiplication, division
✅ Parenthèses pour gérer la priorité des opérations
✅ Fonctions scientifiques : cos, sin, tan, log
✅ Constante mathématique π (pi) prise en charge
✅ Effacement du dernier caractère ou de toute l'expression
✅ Gestion des erreurs syntaxiques et mathématiques
🗂️ Structure du projet

    App : classe principale qui gère l'interface et la logique de la calculatrice.

    afficher : fonction utilitaire pour afficher du texte à l'écran.

    UI elements : boutons numériques, opérateurs, fonctions et parenthèses.

    Évènements : chaque bouton est lié à une action qui met à jour l'affichage et l'expression en cours.

    Regex (self.pattern) : expression régulière pour valider et extraire les entrées valides (\d+\.?\d*|[+\-*/()]|[a-z]{2,3}).

🔑 Utilisation

    Installer les dépendances

pip install pygame pygame_gui numpy

Exécuter le script principal

    python calculator.py

    Utiliser la calculatrice

        Cliquer sur les boutons pour construire une expression mathématique.

        Cliquer sur = pour calculer le résultat.

        Utiliser << pour effacer le dernier caractère ou erase all pour tout effacer.

⚠️ Remarques

    La constante pi est reconnue grâce à l'expression régulière [a-z]{2,3} qui capture les fonctions sin, cos, tan, log ainsi que pi (2 caractères).
    ⚙️ Cela fonctionne car pi est importé de numpy et reconnu par eval.

    L'utilisation de eval() permet d'évaluer dynamiquement les expressions mais doit être manipulée avec précaution pour éviter des erreurs ou des risques de sécurité dans d'autres contextes.

✅ Exemple d'expression valide

cos(pi/2) + log(10) - 3.5 * 2

✨ Auteur

Développé par Lesno (Charles Noah)
