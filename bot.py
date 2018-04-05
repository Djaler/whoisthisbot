from telegram.ext import Filters, MessageHandler, Updater

from config import ENV, PORT, URL


class Bot:
    def __init__(self, token):
        self._token = token
        self._updater = Updater(token)
        
        self._init_handlers()
    
    def run(self):
        if ENV == "prod":
            self._updater.start_webhook(listen='0.0.0.0', port=PORT,
                                        url_path=self._token)
            self._updater.bot.set_webhook(URL + self._token)
            self._updater.idle()
        else:
            self._updater.start_polling(poll_interval=1)
    
    def _init_handlers(self):
        self._updater.dispatcher.add_handler(
            MessageHandler(Filters.forwarded, self._get_forward_from_info))
    
    @staticmethod
    def _get_forward_from_info(bot, update):
        message = update.message
        user = message.forward_from
        
        text = ["ID = {}".format(user.id),
                "First name = {}".format(user.first_name)]
        if user.last_name:
            text.append("Last name = {}".format(user.last_name))

        message.reply_text(text="\n".join(text))
