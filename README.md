# colissimo
A quick and dirty script to follow your Colissimo parcels without leaving your
shell.

This dirty code screen scraps the http://www.laposte.fr site. Hence, as it is
fragile, this project will die soon.

## Installation

From source code:

    git clone <url of the project>
    cd <folder of the cloned project>
    pip install -e .

From Pypi:

    pip install colissimo

## Usage

See:

    colissimo --help

Example:

    stac@sicksadworld:~/development/colissimo>colissimo XXXXXXXXXXXX
    La Poste Colissimo - Colis : XXXXXXXXXXXX

    ┌────────────┬───────────────────────────────────────────────────────────────────┬────────────────────┐
    │ Date       │ Description                                                       │ Lieu               │
    ├────────────┼───────────────────────────────────────────────────────────────────┼────────────────────┤
    │ 20/01/2018 │ Votre colis est en préparation pour la livraison.                 │ Centre Courrier 06 │
    │ 19/01/2018 │ Votre colis est en cours d'acheminement.                          │ Plateforme Colis   │
    │ 18/01/2018 │ Votre colis est en cours d'acheminement.                          │ Plateforme Colis   │
    │ 17/01/2018 │ Votre colis est prêt à être expédié, il va être remis à La Poste. │ Plateforme Colis   │
    └────────────┴───────────────────────────────────────────────────────────────────┴────────────────────┘

    stac@sicksadworld:~/development/colissimo>colissimo XXXXXXXXXXXX
    La Poste Colissimo - Colis : XXXXXXXXXXXX

    ┌────────────┬───────────────────────────────────────────────────────────────────────────────────-─────────────────┬──────────────────────────┐
    │ Date       │ Description                                                                                         │ Lieu                     │
    ├────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────┼──────────────────────────┤
    │ 19/01/2018 │ Votre colis est en cours d'acheminement.                                                            │ Plateforme Colis         │
    │ 18/01/2018 │ Votre colis a été déposé après l'heure limite de dépôt. Il sera expédié dès le prochain jour ouvré. │ Bureau de Poste Puymirol │
    └────────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────┴──────────────────────────┘

