# -*- coding:utf-8 -*-
from datetime import datetime


def sample(x):
    return x * 10


def sample2(x):
    try:
        y = sample(x + 1)
    except IndexError:
        raise ValueError("invalid")
    return y


class EMail(object):
    def send(self, sender, to, cc, bcc, subject, body):
        sent = self.sending_at()
        return {
            "from": sender,
            "to": to,
            "cc": cc,
            "bcc": bcc,
            "subject": subject,
            "body": body,
            "sent": sent,
        }

    def sending_at(self):
        return datetime.now()
