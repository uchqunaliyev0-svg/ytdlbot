#!/usr/local/bin/python3
# coding: utf-8

# ytdlbot - constant.py
# 8/16/21 16:59
#

__author__ = "Benny <benny.think@gmail.com>"

import typing

from pyrogram import Client, types


class BotText:

    start = """
🎬 YouTube va boshqa saytlardan video yuklab olish botiga xush kelibsiz!

📌 /help — bot imkoniyatlari haqida ma'lumot
"""

    help = """
1. YouTube va yt-dlp tomonidan qo'llab-quvvatlanadigan istalgan sayt havolasini yuboring — bot yuklab beradi.

2. Maxsus havolalar uchun: `/spdl {URL}` buyrug'idan foydalaning.

3. Agar bot ishlamasa, qayta urinib ko'ring.

4. Video sifati va formatini o'zgartirish uchun /settings buyrug'idan foydalaning.
    """

    about = "YouTube Downloader bot — video va audio yuklab olish uchun qulay vosita."

    settings = """
Video formati va sifatini tanlang. Bu sozlamalar faqat **YouTube videolari** uchun amal qiladi.
🔴 Yuqori: 1080P
🟡 O'rta: 720P
🟢 Past: 480P

Videoni fayl sifatida yuborsangiz, Telegram uni to'g'ridan to'g'ri ijro eta olmaydi.

Joriy sozlamalaringiz:
Video sifati: {}
Yuborish turi: {}
"""


class Types:
    Message = typing.Union[types.Message, typing.Coroutine]
    Client = Client
