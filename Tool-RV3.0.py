#!/bin/sh

Red='\33[0;31m'
Green='\33[0;32m'
Yellow='\33[0;33m'
Purple='\33[0;34m'
Pink='\33[0;35m'
Cyan='\33[0;36m'
White='\33[0;37m'
Normal='\33[0m'

clear

echo $Red"______            __           ____        /_  __/___  ____  / /____      / __ \
  / / / __ \/ __ \/ / ___/_____/ /_/ /       / / / /_/ / /_/ / (__  )_____/ _, _/
/_/  \____/\____/_/____/     /_/ |_|"

echo $Cyan"|=====================================|"
echo $Cyan"                                      |"
echo $Cyan[x]$Yellow"Welcome To R-1DD ToolS             |"
echo $Cyan[x]$Pink"Follow Ig : ridd4n                 |"
echo $Cyan[x]$Purple"Author : R-1DD                     |"
echo $Cyan[x]$Red"Contac Person : 08815765630        |"
echo $Cyan"                                      |"
echo $Cyan"|=====================================|"
echo $Cyan"____  _ ___ __       ______            _______                       / __ \(_) (_) /_     /_  __/___  ____  / / ___/                      / /_/ / / / / __ \     / / / __ \/ __ \/ /\__ \                      / ____/ / / / / / /    / / / /_/ / /_/ / /___/ /
/_/   /_/_/_/_/ /_/    /_/  \____/\____/_//____/"

echo $Green"======================================"
echo $Red"                                     |"
echo $Red"1.Ridd Bot                           |"
echo $Green"                                     |"
echo $Red"2.PyPhisher                          |"
echo $cyan"                                     |"
echo $purple"3.Tool-X [DALAM PERBAIKAN]           |"
echo $Yellow"                                     |"
echo $Red"4.SEND BOT [SPAMMER]                 |"
echo $Cyan"                                     |"
echo $Red"5.VMBF_SF                            |"
echo $Cyan"                                     |"
echo $Red"6.EXIT [KELUAR]                      |"
echo $Green"======================================"
read -p "MASUKKAN NOMOR: " Bad

if [ $Bad = 1 ]
then
echo $Cyan"R-1DD : KALEM LURR..."
sleep 2
cd RIDBOT
npm start
fi

if [ $Bad = 2 ]
then
sleep 2
echo $Green"R-1DD : KALEM LURR..."
sleep 2
cd PyPhisher
python pyphisher.py
fi

if [ $Bad = 3 ]
then
sleep 2
echo $Green"R-1DD : KALEM LURR..."
sleep 2
echo $Red"MAAF KAK TOOLS INI SEDANG DALAM PERBAIKAN"
exit
else
sleep 2
fi

if [ $Bad = 4 ]
then
sleep 2
echo $Green"R-1DD : KALEM LURR..."
sleep 2
cd sendbot
python main_bot.py
fi

if [ $Bad = 5 ]
then
sleep 2
echo $Green"R-1DD : KALEM LURR..."
sleep 2
cd vmbf_sf
git pull
python run.py
fi

if [ $Bad = 6 ]
then
sleep 2
echo $Green"R-1DD : KALEM LURR..."
sleep 2
echo $Red"R-1DD : SUKSES KELUAR"
exit
else
sleep 2
fi