#!/bin/bash

source "scripts/utils/color.sh"
source "scripts/utils/separator.sh"

print_bg_blue "Displaying 5-day forecast"

PS3="Input desired output format ($(print_red 'json'), $(print_green 'csv'), $(print_blue 'txt')): "

while true; do
    echo
    read -p "$PS3" format
    case "$format" in
        json)
            print_red "Executing: python -m src.cli location Asuncion --forecast"
            print_separator
            python -m src.cli location Asuncion --forecast
            print_separator
            ;;
        csv)
            print_red "Executing: python -m src.cli location Asuncion --forecast --format csv"
            print_separator
            python -m src.cli location Asuncion --forecast --format csv
            print_separator
            ;;
        txt)
            print_red "Executing: python -m src.cli location Asuncion --forecast --format txt"
            print_separator
            python -m src.cli location Asuncion --forecast --format txt
            print_separator
            ;;
        *)
            echo
            print_red "Invalid output format. Choose one of (json, csv, txt)"
            ;;
    esac

    echo
    read -p "Do you want to continue [$(print_green y)/$(print_red n)]: " response
    if [[ $response != "y" ]]; then
        break
    else
        clear
    fi
done
