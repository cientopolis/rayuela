from django.core.management import BaseCommand
import geopandas as gpd
import json

from rayuelaApp.models.user import User
from rayuelaApp.models.project import Project
from rayuelaApp.models.project_area import ProjectArea
from rayuelaApp.models.time_restriction import TimeRestriction

text_0 = ''
text_27 = 'Lorem ipsum dolor sit amet.'
text_91 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non ex mattis, tempus quam a.'
text_179 = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras hendrerit eu risus vel maximus.'
            'Suspendisse quis gravida magna. Nullam condimentum, dui in tincidunt tincidunt, erat.')
text_343 = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
            'Phasellus quis aliquam urna. Cras et nunc tortor.'
            'Aenean elementum massa ac ex condimentum malesuada.'
            'Vestibulum quis felis id nulla tincidunt viverra convallis bibendum tortor.'
            'Ut finibus euismod eros sed imperdiet.'
            'Nullam lobortis augue eu mauris dapibus congue. Nam nec accumsan leo.')
desc_Anticipando = ('Estrategias comunitarias para la reducción de desastres e inundaciones urbanas.'
            'Contribuir en la reducción de riesgos ante desastres asociados a eventos hidro-meteorológicos, mediante el diálogo con actores territoriales con el fin de fortalecer el sistema de alerta temprana comunitario centrado en la población')

desc_geovin=('Estudio de enfermedades transmitidas por vectores (animales transmisores)','Proveer de herramientas interactivas, educativas, lúdicas y gratuitas a personas usuarias no especializadas, que permitan contribuir a la problemática relacionada con las vinchucas en todo el país. Fomentar la concientización acerca de la problemática de salud relacionada con la Enfermedad de Chagas, involucrando a la ciudadanía en el monitoreo de su vector.')

desc_cazamosquitos=('Estudio de enfermedades transmitidas por vectores (animales transmisores)','Estudiar la distribución de mosquitos vectores de enfermedades, incluido el Aedes aegypti, vector de los virus dengue, zika, chikungunya y fiebre amarilla. Involucrar a la ciudadanía en el análisis y cuestionamiento de su entorno, tomando acciones individuales para contribuir con la prevención de la propagación del insecto vector.')

desc_preservamos=('Monitoreo ambiental de ecosistemas acuáticos de agua dulce','PreserVamos es una iniciativa del Laboratorio de Aceleración del Programa para el Desarrollo de Naciones Unidas (PNUD) junto con el proyecto de ciencia participativa AppEAR, y diferentes municipios de la provincia de Buenos Aires para estudiar los ambientes acuáticos de agua dulce')

desc_argentinat=('Biodiversidad', 'Conocer más acerca de los ciclos de vida, la distribución y la dinámica poblacional de todas las especies que habitan en Argentina')

desc_mihabitat=('Saneamiento y gestión de residuos; enfermedades transmitidas por vectore', 'Concientizar a las personas jóvenes y a los núcleos familiares sobre los riesgos sanitarios que representan los basurales, roedores y parásitos en sus comunidades. Impulsar, junto con la comunidad educativa, a los barrios en situación de mayor vulnerabilidad (debido este tipo de contaminación) a generar acciones que mejoren su calidad de vida ')

desc_cyano=('Eutrofización de cuerpos de agua y cianobacterias','Se aborda la eutrofización de cuerpos de agua superficiales de manera interrelacionada con su cuenca de aporte, los diferentes usos del agua y el Cianosemáforo, para la prevención del riesgo en aguas de uso recreativo')

website = "https://www.unq.edu.ar/"

PROJECTS = {
    "proy1": ["Anticipando la crecida", True, desc_Anticipando, website],
    "proy2": ["GeoVin", True, desc_geovin, website],
    "proy3": ["Caza Mosquitos", False, desc_cazamosquitos, website],
    "proy4": ["PreserVamos", True, desc_preservamos, website],
    "proy5": ["ArgentiNat.org", True, desc_argentinat, website],
    "proy6": ["Mi habitat", True, desc_mihabitat, website],
    "proy7": ["Cyano", False, desc_cyano, website],
}

# Ubicación de archivos para generar información
path_files = 'rayuelaApp/fixtures/'

# Se obtienen admins existentes
admin1 = User.objects.get(id=2)
admin2 = User.objects.get(id=3)
admin3 = User.objects.get(id=4)

# Se crean restricciones de tiempo
# Lunes a viernes
lunes_a_viernes = TimeRestriction.objects.create(name="Lunes a viernes", date_from="2023-10-01", date_to="2024-10-01",
                                                 hour_from="00:00", hour_to="23:59")
lunes_a_viernes.days.add(1)
lunes_a_viernes.days.add(2)
lunes_a_viernes.days.add(3)
lunes_a_viernes.days.add(4)
lunes_a_viernes.days.add(5)

# Fin de semana
fin_de_semana = TimeRestriction.objects.create(name="Fin de semana", date_from="2023-10-01", date_to="2024-10-01",
                                               hour_from="00:00", hour_to="23:59",)
fin_de_semana.days.add(6)
fin_de_semana.days.add(7)


class Command(BaseCommand):
    help = "Crear proyectos para entorno de desarrollo"

    def handle(self, *args, **options):
        # Se crean proyectos
        for project in PROJECTS:
            new_project = Project.objects.create(name=PROJECTS[project][0], web=PROJECTS[project][3],
                                                 available=PROJECTS[project][1], description=PROJECTS[project][2])
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
