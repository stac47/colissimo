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

    stac@sicksadworld:~/development/colissimo>colissimo --lang en XXXXXXXXXXX
    La Poste Colissimo - Colis : XXXXXXXXXXX

    | Date       | Description                                                                                          | Lieu                                   |
    |------------|------------------------------------------------------------------------------------------------------|----------------------------------------|
    | 01/18/2018 | Your parcel has been posted after the posting deadline. It will be shipped on the next working day.  | Post office Puymirol                   |

    stac@sicksadworld:~/development/colissimo>colissimo --lang fr XXXXXXXXXXX
    La Poste Colissimo - Colis : XXXXXXXXXXX

    | Date       | Description                                                                                          | Lieu                                   |
    |------------|------------------------------------------------------------------------------------------------------|----------------------------------------|
    | 18/01/2018 | Votre colis a été déposé après l'heure limite de dépôt. Il sera expédié dès le prochain jour ouvré.  | Bureau de Poste Puymirol               |

    stac@sicksadworld:~/development/colissimo>colissimo --lang de XXXXXXXXXXX
    La Poste Colissimo - Colis : XXXXXXXXXXX

    | Date       | Description                                                                                          | Lieu                                   |
    |------------|------------------------------------------------------------------------------------------------------|----------------------------------------|
    | 18/01/2018 | Ihr Paket wurde nach Annahmeschluss aufgegeben. Es wird am folgenden Werktag abgeschickt.            | Postfiliale Puymirol                   |

