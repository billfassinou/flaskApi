# API Flask - Projet Fassinou Bile

Ce projet consiste en une API Flask déployée via Docker. L'API fournit diverses fonctionnalités pour interagir avec les données.

## Utilisation

1. Assurez-vous que Docker est installé sur votre système.

2. Téléchargez l'image Docker depuis Docker Hub :

    ```bash
    docker pull billfass/app-fassinou-bile:v1
    ```

3. Lancez le conteneur Docker :

    ```bash
    docker run billfass/app-fassinou-bile:v1
    ```

## Endpoints

- `/`: Affiche un message d'accueil.
- `/api/welcome`: pour obtenir un message de bienvenue.
- `/api/about`: pour obtenir des informations sur l'équipe de dev.
- `/api/contact`: pour obtenir des informations de contact.
- `/api/user/{id}`: pour obtenir des informations sur un utilisateur spécifique correspondant à l'ID spécifié.
- `/api/articles`: pour obtenir une liste d'articles.

## Contribuer

Les contributions sont les bienvenues ! Pour toute amélioration ou correction de bug, veuillez ouvrir une pull request. Pour des suggestions ou des problèmes, veuillez ouvrir une issue.

## Auteurs

Ce projet a été développé par [Fassinou Bile](https://github.com/billfassinou).

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
