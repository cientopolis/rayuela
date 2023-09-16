from django.core.management import BaseCommand
from rayuelaApp.models.project import Project
from rayuelaApp.models.user import User

PROJECTS = {
    "proy1": ["Proyecto incial", True, "Lorem ipsum dolor sit amet."],
    "proy2": ["Proyecto Dos", True, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus quis aliquam urna. Cras et nunc tortor. Aenean elementum massa ac ex condimentum malesuada. Vestibulum quis felis id nulla tincidunt viverra convallis bibendum tortor. Ut finibus euismod eros sed imperdiet. Nullam lobortis augue eu mauris dapibus congue. Nam nec accumsan leo."],
    "proy3": ["Otro proyecto 3", False, ""],
    "proy4": ["Proyecto 4", True, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non ex mattis, tempus quam a."],
    "proy5": ["Nuevo proyecto 5", True, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras hendrerit eu risus vel maximus. Suspendisse quis gravida magna. Nullam condimentum, dui in tincidunt tincidunt, erat."],
    "proy6": ["Proyecto número 6", True, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non ex mattis, tempus quam a."],
    "proy7": ["Último proyecto", False, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus quis aliquam urna. Cras et nunc tortor. Aenean elementum massa ac ex condimentum malesuada. Vestibulum quis felis id nulla tincidunt viverra convallis bibendum tortor. Ut finibus euismod eros sed imperdiet. Nullam lobortis augue eu mauris dapibus congue. Nam nec accumsan leo."],
}

# Se obtienen admins existentes
admin1 = User.objects.get(id=2)
admin2 = User.objects.get(id=3)
admin3 = User.objects.get(id=4)


class Command(BaseCommand):

    help = "Crear proyectos para entorno de desarrollo"

    def handle(self, *args, **options):
        # Se crean proyectos
        for project in PROJECTS:
            new_project = Project.objects.create(name=PROJECTS[project][0], available=PROJECTS[project][1],
                                                 description=PROJECTS[project][2])
            new_project.save()

            print("Creando proyecto {}".format(PROJECTS[project][0]))

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
