from django.core.management import BaseCommand
from rayuelaApp.models.user import User
from rayuelaApp.models.role import Role

insecure_password = 'sha256$BuAcJkInBJ$aea840b1833711c9e63134c606d72ab623992ce762aba25795405ffb2d488202'

USERS = {
    "root": ["ROOT", "Root", "root@correofalso.com", insecure_password],
    "admin1": ["ADMIN", "Administrador", "admin1@admin.com", insecure_password],
    "admin2": ["ADMIN", "Administradora", "admin2@admin.com", insecure_password],
    "admin3": ["ADMIN", "Otro administrador", "admin3@admin.com", insecure_password],
    "pv1": ["PLAYER", "Persona Voluntaria 1", "persona-voluntaria-1@correofalso.com", insecure_password],
    "pv2": ["PLAYER", "P. Voluntaria 2", "p-voluntaria-2", insecure_password],
    "pv3": ["PLAYER", "Persona V. 3", "persona-v-3@correofalso.com", insecure_password],
    "pv4": ["PLAYER", "P.V. 4", "pv4@correofalso.com", insecure_password],
}


class Command(BaseCommand):

    help = "Crear usuarios/as para entorno de desarrollo"

    def handle(self, *args, **options):
        # Se crean roles
        role_root = Role.objects.create(name="ROOT")
        role_admin = Role.objects.create(name="ADMIN")
        role_player = Role.objects.create(name="PLAYER")

        role_id = None
        # Se crean usuarios/as
        for user_name in USERS:
            if USERS[user_name][0] == "ROOT":
                role_id = role_root
            if USERS[user_name][0] == "ADMIN":
                role_id = role_admin
            if USERS[user_name][0] == "PLAYER":
                role_id = role_player

            new_user = User.objects.create(username=user_name, password=USERS[user_name][3],
                                           complete_name=USERS[user_name][1], email=USERS[user_name][2], role_id=role_id)
            new_user.save()
            print("Creando user {} con rol {}".format(user_name, role_id))