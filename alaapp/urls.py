"""ala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from alaapp.views import user, admin, project, game_elements, checkin ,badge , challenge , assignment, time_restriction
from alaapp.views.game_element_view import GameElementView
from django.urls import path

urlpatterns = [
    path('', user.index,name='index'),
    path('home/',user.home, name='home'),  
    path('logout/',user.logout, name='logout'),
    path('register/',user.register,name='register'),
    path('register_user/',user.register_user,name='register_user'),
    path('login/',user.login, name='login'), 
    path('verificate/',user.verificate, name='verificate'),
    path('activate_account/',user.activate_account,name='activate_account'),
    path('active_account/',user.active_account,name='active_account'),
    path('create_admin/',admin.create_admin,name='create_admin'),
    path('modify_project/',project.modify_project,name='modify_project'),
    path('modify/',game_elements.modify,name='modify'),
    path('register_admin/',admin.register_admin,name='register_admin'),
    path('create_project/',project.create_project,name='create_project'),
    path('register_project/',project.register_project,name='register_project'),
    path('edit_project/',project.edit_project,name='register_project'),
    path('create_badge/',badge.badge,name='create_badge'),
    path('process_badge/',badge.process_badge,name='process_badge'),
    path('change_state/',game_elements.change_state,name='change_state'),
    path('create_challenge/',challenge.challenge,name='create_challenge'),
    path('process_challenge/',challenge.process_challenge,name='process_challenge'),
    path('game_element_view/',GameElementView.as_view(),name='game_element_view'),
    path('create_checkin/',checkin.checkin,name='create_checkin'),
    path('process_checkin/',checkin.process_checkin,name='process_checkin'),
    path('view_game_elements/',game_elements.view_game_elements, name='view_game_elements'),
    path('asign_challenge/',challenge.asign_challenge,name="asign_challenge"),
    path('asign_badge/',badge.asign_badge,name="asign_badge"),
    path('see_my_game_elements/',user.see_my_game_elements,name='see_my_game_elements'),
    path('edit_profile/',user.edit_profile,name='edit_profile'),
    path('process_edit_profile/',user.process_edit_profile,name='process_edit_profile'),
    path('game_elements_project/',project.game_elements_project,name='game_elements_project'),
    path('modify_challenge/',challenge.modify_challenge, name='modify_challenge'),
    path('modify_badge/',badge.modify_badge, name='modify_badge'),
    path('see_all_projects/',project.see_all_projects,name='see_all_projects'),
    path('asign_project/',project.asign_project,name='asign_project'),
    path('my_projects/',user.my_projects,name='my_projects'),
    path('add_like_dislike/',assignment.add_like_dislike,name='add_like_dislike'),
    path('create_scorings/',assignment.create_scorings,name='create_scorings'),
    path('create_time_restriction/',time_restriction.time_restriction,name='create_time_restriction'),
    path('process_time_restriction/',time_restriction.process_time_restriction,name='process_time_restriction'),
    path('modify_project_root/',project.modify_project_root,name='modify_project_root'),
    path('process_modify_project/',project.process_modify_project,name='process_modify_project'),
    path('disjoin_project/',project.disjoin_project,name='disjoin_project'),


]

