#!/bin/bash

#Spawnar server, monitor, e carregar o codigo da nossa equipe

gnome-terminal --working-directory=/home/borg/Soccer-Simulation-2D/starter-stack -e "python3 server.py"
gnome-terminal --working-directory=/home/borg/Soccer-Simulation-2D/starter-stack -e "python3 monitor.py"
gnome-terminal --working-directory=/home/borg/Soccer-Simulation-2D/'Codigo Principal' -e "python3 agent.py Insper_Dynamics 11"
echo Ambiente Iniciado