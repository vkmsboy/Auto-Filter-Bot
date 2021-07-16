#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🏷 Channel', url='https://telegram.dog/Mj_Linkz/'),
                        InlineKeyboardButton('Creator 🖥', url ='https://telegram.dog/MasterOfTG'),
                    ],
                    [
                        InlineKeyboardButton(
                            "♻️ JOIN OUR GROUP ♻️", url="https://telegram.dog/MovieJunctionGroup")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡ BACK", callback_data="start_data"),
                        InlineKeyboardButton("ABOUT 🚩", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton("🔻 FEEDBACKS & SUGGESTIONS 🔻", url="https://telegram.dog/Mj_Chats")
                   
                ]     
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🚩 HELP", callback_data="help_data"),
                        InlineKeyboardButton("HOME 🏠", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "⚙️ SOURCE CODE ⚙️", url="https://github.com/Iam-The-Master/Auto-Filter-Bot")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass
