#!/bin/bash

# ANSI escape sequence code
BG_BLUE='\x1b[44m'

RED='\x1b[31m'
GREEN='\x1b[32m'
BLUE='\x1b[34m'
NC='\033[0m'

print_bg_blue() {
    echo -e "${BG_BLUE}$1${NC}"
}

print_red() {
    echo -e "${RED}$1${NC}"
}

print_green() {
    echo -e "${GREEN}$1${NC}"
}

print_blue() {
    echo -e "${BLUE}$1${NC}"
}
