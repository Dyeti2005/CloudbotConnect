from flask import Blueprint, request

from heyoo import WhatsApp
from bot import Chatbot
from logs import Logger

import os

webhook_bp = Blueprint('webhook', __name__)

log = Logger()
bot = Chatbot()

PHONE_ID = os.environ.get("PHONE_ID")
VERIFY_TOKEN = os.environ.get("META_VERIFY_TOKEN")

@webhook_bp.route('/webhook/', methods=['GET'])
def handle_verification():
    token_sent = request.args.get("hub.verify_token")
    
    if token_sent == VERIFY_TOKEN:
        challenge = request.args.get("hub.challenge")
        return challenge
        
    log.write_log("Error, Invalid verification token")
    return "Invalid verification token", 403

@webhook_bp.route('/webhook/', methods=['POST'])
def handle_messages():
    try:
        data = request.get_json()['entry'][0]['changes'][0]['value']['messages'][0]
        telefono = data['from']
        mensaje = data['text']['body']
        
        log.write_log(f"mensaje: {mensaje}")
        log.write_log(f"telefono: {telefono}")

        reply = bot.reply(mensaje)
        
        log.write_log(f"bot reply: {mensaje}")

        msg=WhatsApp(VERIFY_TOKEN,PHONE_ID)
        msg.send_message(reply,telefono)
        
        return "Message Processed",200
    
    except Exception as Ex:
        log.write_log(str(Ex))