#!/bin/bash

check_venv_folder() {
    if [ ! -d ".venv" ]; then
        echo "The '.venv' folder does not exist. Now creating one:"
        poetry install
        echo "Done."
    fi
}

check_venv_folder