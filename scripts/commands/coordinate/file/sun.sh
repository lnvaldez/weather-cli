#!/bin/bash

source "scripts/utils/color.sh"
source "scripts/utils/separator.sh"

print_bg_blue "Write sunrise and sunset times to file"

PS3="Input desired target file ($(print_red 'json'), $(print_green 'csv'), $(print_blue 'txt')): "

while true; do
    echo
    read -p "$PS3" format
    case "$format" in
        json)
            print_red "Executing: python -m src.cli coordinate 41.4086874 -75.6621294 --sun --target file "
            print_separator
            python -m src.cli coordinate 41.4086874 -75.6621294 --sun --target file
            echo "Reading json file..."
            cat src/data/data.json 
            echo
            print_red "Check your data.json file"
            print_separator
            ;;
        csv)
            print_red "Executing: python -m src.cli coordinate 41.4086874 -75.6621294 --sun --format csv --target file"
            print_separator
            python -m src.cli coordinate 41.4086874 -75.6621294 --sun --format csv --target file
            echo "Reading csv file..."
            cat src/data/data.csv
            echo 
            print_green "Check your data.csv file"
            print_separator
            ;;
        txt)
            print_red "Executing: python -m src.cli coordinate 41.4086874 -75.6621294 --sun --format txt --target file"
            print_separator
            python -m src.cli coordinate 41.4086874 -75.6621294 --sun --format txt --target file
            echo "Reading txt file..."
            cat src/data/data.txt
            echo
            print_blue "Check your data.txt file"
            print_separator
            ;;
        *)
            echo
            print_red "Invalid output format. Choose one of (json, csv, txt)"
            ;;
    esac

    echo
    read -p "Do you want to continue (file will be emptied) [$(print_green y)/$(print_red n)]: " response
    if [[ $response != "y" ]]; then
        python -m src.cli clear json 
        python -m src.cli clear csv 
        python -m src.cli clear txt
        clear
        break
    else
        python -m src.cli clear json 
        python -m src.cli clear csv 
        python -m src.cli clear txt
        clear
    fi
done
