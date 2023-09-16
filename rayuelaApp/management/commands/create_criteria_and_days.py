from django.core.management import BaseCommand
from rayuelaApp.models.criteria import Criteria
from rayuelaApp.models.day import Day

CRITERIA = {
    "crit1": "Diversión",
    "crit2": "Dificultad",
    "crit3": "Originalidad",
    "crit4": "Duración",
}

DAYS = {
    "lunes": "Lunes",
    "martes": "Martes",
    "miercoles": "Miércoles",
    "jueves": "Jueves",
    "viernes": "Viernes",
    "sabado": "Sábado",
    "domingo": "Domingo",
}


class Command(BaseCommand):

    help = "Crear criterios y días para entorno de desarrollo"

    def handle(self, *args, **options):
        # Se crean proyectos
        for criterion in CRITERIA:
            new_criterion = Criteria.objects.create(name=CRITERIA[criterion])
            new_criterion.save()

            print("Creando criterio {}".format(CRITERIA[criterion]))

        for day in DAYS:
            new_day = Day.objects.create(name=DAYS[day])
            new_day.save()

            print("Creando día {}".format(DAYS[day]))
