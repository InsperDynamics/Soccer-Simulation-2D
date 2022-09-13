#!/bin/bash

#Spawnar server, monitor, e carregar o codigo da nossa equipe
#Certifique-se de que a o repositorio foi clonado para /home/borg

gnome-terminal --working-directory=/home/borg/Soccer-Simulation-2D/Ambiente -e "python3 server.py"
gnome-terminal --working-directory=/home/borg/Soccer-Simulation-2D/Ambiente -e "python3 monitor.py"
gnome-terminal --working-directory=/home/borg/Soccer-Simulation-2D/TimeDynamics -e "python3 agent.py Insper_Dynamics 11"
echo Ambiente Iniciado