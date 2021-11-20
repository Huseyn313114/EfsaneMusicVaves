from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as BN
from helpers.filters import command, other_filters2


@Client.on_message(command(["start", f"start"]))
async def start(_, message: Message):
    await message.reply_photo("https://i.ibb.co/khRz42f/Turkish-Voice.jpg")
    await message.reply_text(
        f"""**Salam, {message.from_user.mention} 🎵
Sesli sohbetlerde musiqi çalabilen botam. Ban yetkisiz, Ses yönetimi yetkisi verib, Asistantı qrupa elave edin.\n\nDüzenleme [DBMBOSSdu 🇦🇿](https://t.me/DBMsohbet).
 **""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Qrupuna  Elave ele ➕", url="https://t.me/Efsanestar_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistant", url="https://t.me/DBMmusicasistantbot" 
                    ),
                    InlineKeyboardButton(
                        "💬 Sohbet", url="https://t.me/DBMsohbet"
                    ),
                    InlineKeyboardButton(
                        "🙎‍♂️ Sahibim", url="https://t.me/DBMBOSSdu") 
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Github", url="https://github.com/Huseyn313114"
                    )
                ]
            ]
        ), 
     disable_web_page_preview=True
   ) 

@Client.on_message(command(["bilgi"])) 
async def bilgi(_, message: Message):
      await message.reply_text(f"**Merhaba {message.from_user.mention}!\n Bu botun bilgi menüsü 📚\n\n ▶️ /play - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /play <song name> - istediğiniz şarkıyı çalınız\n 🔴 /ytplay <Sorgu> - youtube üzerinden çalar\n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n\n Yalnızca yöneticiler için..\n ⏩ /resume - şarkı çalmaya devam et\n ⏹ /end - müzik botunu kapatmak için\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n 🎚 /ses asistan hesabın ses seviyesini kontrol et\n\n ⚪ /katil - Müzik asistanı grubunuza katılır\n ⚫ /ayril - Müzik asistanı grubunuzu terk eder.**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "👨‍🔧 Sahibim", url="https://t.me/DBMBOSSdu")
                 ]
             ]
         )
    )
