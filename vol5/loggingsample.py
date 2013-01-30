# -*- coding:utf-8 -:-
import logging
import logging.config

# django logging
# http://docs.djangoproject.jp/ja/latest/topics/logging.html

# python logging document
# http://docs.python.jp/2/library/logging.html

# logging default setting: logging.basicConfig
# http://stackoverflow.com/questions/2557168/how-do-i-change-the-default-format-of-log-messages-in-python-app-engine
# http://docs.python.jp/2/library/logging.html#logging.basicConfig

LOGGING = {
    'version': 1,
    'formatters': {
        '()': {
            'format': '=====> %(message)s',
        },
        'precise': {
            'format': '%(asctime)s %(message)s',
            'datefmt': '%Y/%m/%d %H:%M:%S',
        },
    },
    'handlers': {
        'logfile': {
            #'level': 'NOTSET',
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/tmp/loggingsample.log',
        },
        'console': {
            'level': 'WARN',
            'class': 'logging.StreamHandler',
            'formatter': 'precise',
        },
    },
    'loggers': {
        'foo': {
            'handlers': ['logfile', 'console'],
            'level': 'DEBUG',
        },
    }
}


# ロギングの設定を読み込む。
logging.config.dictConfig(LOGGING)


# rootロガーで出力。
logging.debug(u'(debug) いまがわ よしもと')  # 出力されない
logging.info(u'(info) いまがわ よしもと')    # 出力されない
logging.error(u'(error) いまがわ よしもと')  # 出力される


# fooロガーを使用して出力。
logger = logging.getLogger('foo')
logger.debug(u'今川義元')
logger.warn(u'不正な書き込みが行われました。')
