#!/bin/bash

check_credentials_file() {
    if [ ! -d ".env" ]; then
        echo "The '.env' folder does not exist. Now creating one:"
        mkdir .env
        touch .env/credentials.json
        echo -e '{\n\t"openai":"",\n\t"gemini":""\n}' > .env/credentials.json
        echo "Done."
    fi
}

check_venv_folder() {
    if [ ! -d ".venv" ]; then
        echo "The '.venv' folder does not exist. Now creating one:"
        poetry install
        echo "Done."
    fi
}

check_credentials_file && check_venv_folder