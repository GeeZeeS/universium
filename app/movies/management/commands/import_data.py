from django.core.management.base import BaseCommand

from actors.models import Actor, Role
from directors.models import Director, DirectorGenre
from movies.models import Movie, MovieGenre, MovieDirector
from base.settings import DATA_ROOT


model_list = {
        "actors": Actor, "roles": Role,
        "directors": Director, "directors_genres": DirectorGenre,
        "movies": Movie, "movies_genres": MovieGenre, "movies_directors": MovieDirector
    }


def data_exists(model, key):
    if model.objects.all().exists():
        print(f"Data: {key} already exists.")
        return True
    return False


def populate_data(model, key):
    try:
        with open(f"{DATA_ROOT}/imdb_ijs_{key}.csv") as file:
            model.csv_manager.from_csv(file)
            print(f"Populated data: {key}")
        return True
    except Exception as err:
        print(f"{err} on Table: {key}")
        return False


class Command(BaseCommand):
    help = ""

    def add_arguments(self, parser):
        parser.add_argument('value')

    def handle(self, *args, **options):
        if options['value']:
            if options['value'] == 'all':
                for key, model in model_list.items():
                    if data_exists(model, key):
                        continue
                    populate_data(model, key)
            elif options['value'] == 'truncate':
                for key, value in model_list.items():
                    value.objects.all().delete()
                    print(f"Deleted data: {key}")
                    continue
            else:
                if data_exists(model_list[options['value']], options['value']):
                    return
                populate_data(model_list[options['value']], options['value'])

