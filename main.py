# -*- coding: utf-8 -*-

import bot_app
import itchat


def main():
    try:
        bot_app.app.run(host='0.0.0.0', port=5490)
    except KeyboardInterrupt:
        if itchat.useHotReload:
            itchat.dump_login_status()


if __name__ == '__main__':
    main()

