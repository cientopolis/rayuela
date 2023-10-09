from django.core.management import BaseCommand
import geopandas as gpd
import json

from rayuelaApp.models.user import User
from rayuelaApp.models.project import Project
from rayuelaApp.models.project_area import ProjectArea
from rayuelaApp.models.time_restriction import TimeRestriction

PROJECTS = {
    "proy1": ["Proyecto incial", True, "Lorem ipsum dolor sit amet."],
    "proy2": ["Proyecto Dos", True,
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus quis aliquam urna. Cras et nunc tortor. Aenean elementum massa ac ex condimentum malesuada. Vestibulum quis felis id nulla tincidunt viverra convallis bibendum tortor. Ut finibus euismod eros sed imperdiet. Nullam lobortis augue eu mauris dapibus congue. Nam nec accumsan leo."],
    "proy3": ["Otro proyecto 3", False, ""],
    "proy4": ["Proyecto 4", True,
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non ex mattis, tempus quam a."],
    "proy5": ["Nuevo proyecto 5", True,
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras hendrerit eu risus vel maximus. Suspendisse quis gravida magna. Nullam condimentum, dui in tincidunt tincidunt, erat."],
    "proy6": ["Proyecto número 6", True,
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non ex mattis, tempus quam a."],
    "proy7": ["Último proyecto", False,
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus quis aliquam urna. Cras et nunc tortor. Aenean elementum massa ac ex condimentum malesuada. Vestibulum quis felis id nulla tincidunt viverra convallis bibendum tortor. Ut finibus euismod eros sed imperdiet. Nullam lobortis augue eu mauris dapibus congue. Nam nec accumsan leo."],
}

# Ubicación de archivos para generar información
path_files = 'rayuelaApp/fixtures/'

# Se obtienen admins existentes
admin1 = User.objects.get(id=2)
admin2 = User.objects.get(id=3)
admin3 = User.objects.get(id=4)

# Se crean restricciones de tiempo
# Lunes a viernes
lunes_a_viernes = TimeRestriction.objects.create(name="Lunes a Viernes", date_from="2023-10-01", date_to="2024-10-01", hour_from="00:00", hour_to="23:59")
lunes_a_viernes.days.add(1)
lunes_a_viernes.days.add(2)
lunes_a_viernes.days.add(3)
lunes_a_viernes.days.add(4)
lunes_a_viernes.days.add(5)

# Fin de semana
fin_de_semana = TimeRestriction.objects.create(name="Fin de semana", date_from="2023-10-01", date_to="2024-10-01", hour_from="00:00", hour_to="23:59",)
fin_de_semana.days.add(6)
fin_de_semana.days.add(7)


class Command(BaseCommand):
    help = "Crear proyectos para entorno de desarrollo"

    def handle(self, *args, **options):
        # Se crean proyectos
        for project in PROJECTS:
            new_project = Project.objects.create(name=PROJECTS[project][0], available=PROJECTS[project][1],
                                                 description=PROJECTS[project][2])
            new_project.save()

            print("Creando proyecto {}".format(PROJECTS[project][0]))

        # Se agregan admins a los proyectos
        Project.objects.get(id=1).add_admin(admin1)
        Project.objects.get(id=1).add_admin(admin2)

        Project.objects.get(id=2).add_admin(admin2)
        Project.objects.get(id=2).add_admin(admin3)

        Project.objects.get(id=3).add_admin(admin3)

        Project.objects.get(id=4).add_admin(admin1)
        Project.objects.get(id=4).add_admin(admin2)
        Project.objects.get(id=4).add_admin(admin3)

        Project.objects.get(id=5).add_admin(admin1)

        Project.objects.get(id=6).add_admin(admin2)
        Project.objects.get(id=6).add_admin(admin3)

        Project.objects.get(id=7).add_admin(admin1)
        Project.objects.get(id=7).add_admin(admin2)
        Project.objects.get(id=7).add_admin(admin3)

        # Se agregan restricciones de tiempo a los proyectos
        Project.objects.get(id=1).add_time_restriction(lunes_a_viernes)
        Project.objects.get(id=1).add_time_restriction(fin_de_semana)
        Project.objects.get(id=2).add_time_restriction(lunes_a_viernes)
        Project.objects.get(id=2).add_time_restriction(fin_de_semana)
        Project.objects.get(id=3).add_time_restriction(lunes_a_viernes)
        Project.objects.get(id=4).add_time_restriction(fin_de_semana)
        Project.objects.get(id=5).add_time_restriction(lunes_a_viernes)
        Project.objects.get(id=5).add_time_restriction(fin_de_semana)
        Project.objects.get(id=6).add_time_restriction(lunes_a_viernes)
        Project.objects.get(id=6).add_time_restriction(fin_de_semana)
        Project.objects.get(id=7).add_time_restriction(fin_de_semana)

        # Se agregan áreas a los proyectos
        geojson_la_plata = gpd.read_file(path_files+'la_plata.geojson', driver='GeoJSON')
        area = json.loads(geojson_la_plata.to_json())
        la_plata = ProjectArea.objects.create(name=area['type'])
        la_plata.save()
        la_plata.add_subareas(area['features'])

        geojson_lago = gpd.read_file(path_files+'lago.geojson', driver='GeoJSON')
        area = json.loads(geojson_lago.to_json())
        lago = ProjectArea.objects.create(name=area['type'])
        lago.save()
        lago.add_subareas(area['features'])

        Project.objects.get(id=1).add_area(lago)
        Project.objects.get(id=2).add_area(la_plata)
        Project.objects.get(id=3).add_area(lago)
        Project.objects.get(id=4).add_area(la_plata)
        Project.objects.get(id=5).add_area(lago)
        Project.objects.get(id=6).add_area(la_plata)
        Project.objects.get(id=7).add_area(lago)
