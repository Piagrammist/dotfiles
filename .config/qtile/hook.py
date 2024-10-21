import os
from subprocess import run

from libqtile import hook

from util import parse_window_name

HOME = os.path.expanduser('~')


@hook.subscribe.client_new
def client_new(client):
    name = parse_window_name(client.name)
    if name in ['Firefox', 'Google Chrome']:
        client.togroup('3', switch_group=True)
    elif name == 'Visual Studio Code':
        client.togroup('2', switch_group=True)


@hook.subscribe.startup_once
def start_once():
    run(f'{HOME}/.config/qtile/autostart.sh')
