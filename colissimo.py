from html.parser import HTMLParser
from collections import namedtuple

import click
import requests
from terminaltables import SingleTable
from colorclass import Color


SERVICE_URL =\
    "https://www.laposte.fr/professionnel/outils/suivre-vos-envois/{}/{}"


Row = namedtuple('Row', ['date', 'remark', 'location'])


class LaPosteParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.stack = []
        self.rows = []
        self.current_date = None
        self.current_remark = None
        self.current_location = None

    def __path_ends_with(self, path):
        tags = path.split('/')
        if len(tags) > len(self.stack):
            return False
        return self.stack[-len(tags):] == tags

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)

    def handle_endtag(self, tag):
        # in case of bad formated HTML (tag without closing pair)
        while tag != self.stack[-1]:
            self.stack.pop()

        if self.__path_ends_with('tbody/tr'):
            if self.current_date is not None\
                and self.current_remark is not None\
                and self.current_location is not None:
                self.rows.append(Row(self.current_date,
                                     self.current_remark,
                                     self.current_location))
                self.current_date = None
                self.current_remark = None
                self.current_location = None
            else:
                raise RuntimeError('Bad state')
        self.stack.pop()

    def handle_data(self, data):
        if self.__path_ends_with('tbody/tr/td/p'):
            if self.current_date is None:
                self.current_date = data
            elif self.current_remark is None:
                self.current_remark = str(data)
            elif self.current_location is None:
                self.current_location = str(data)


@click.command()
@click.option('--lang', default='fr',
              type=click.Choice(['fr', 'en', 'es', 'de', 'nl', 'it']),
              help='chosen language')
@click.argument('code')
def cli(lang, code):
    r = requests.get(SERVICE_URL.format(lang, code),
        headers={'X-Requested-With': 'XMLHttpRequest'})
    parser = LaPosteParser()
    parser.feed(r.text)
    click.echo('La Poste Colissimo - Colis : {}'.format(code))
    click.echo()
    data = []
    data.append(['Date', 'Description', 'Lieu'])
    for row in parser.rows:
        data.append([Color('{autogreen}' + row.date + '{/autogreen}'),
                     row.remark,
                     Color('{autocyan}' + row.location + '{/autocyan}')])
    table = SingleTable(data)
    click.echo(table.table)
