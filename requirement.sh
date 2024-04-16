##!/bin/bash 
#
cd $HOME

echo "\033[31m [*] Install pyperclip... \033[0m"
pip3 install pyperclip
echo "\033[32m [*] pyperclip install finished! \033[0m"
echo ""

echo "\033[31m [*] Install pandas... \033[0m"
pip3 install pandas
echo "\033[32m [*] pandas install finished! \033[0m"
echo ""

echo "\033[31m [*] Install numpy... \033[0m"
pip3 install numpy
echo "\033[32m [*] numpy install finished! \033[0m"
echo ""

echo "\033[31m [*] Install tkinter... \033[0m"
sudo apt install -y python3-tk
echo "\033[32m [*] tkinter install finished! \033[0m"
echo ""

echo "\033[31m [*] Install PIL... \033[0m"
sudo apt install -y python3-pil python3-pil.imagetk
echo "\033[32m [*] PIL install finished! \033[0m"
echo ""
