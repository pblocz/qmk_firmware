pipenv run pipenv-shebang ./config_gen.py
pipenv run keymapviz ../keymap.c -c config-gen.properties
pipenv run keymapviz ../keymap.c -c config-gen.properties -t json -o 'layout_editor/lily58_{}.json'
