import random
import requests
import discord
import time
from discord.ext import commands





@client.event
async def on_ready():
    print('Bot is ready.')
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('!command เพื่อดูคำสั่ง'))

chmain = 519825086086119442
chnsfw = 519855190632038421
chrate = 519826190735769601
@client.event
@commands.cooldown(1, 30, commands.BucketType.channel)
async def on_message(message):
    if message.content.startswith("!เติม"):
        await message.channel.send('เติมได้ผ่านเว็บของเรา: https://www.robuxshopth.com/shop')
    elif message.content.startswith("!เว็บ"):
        await message.channel.send('เติมได้ผ่านเว็บของเรา: https://www.robuxshopth.com/shop')
    elif message.content.startswith("!เรท"):
        embed = discord.Embed(
            colour = discord.Colour.blue()
        )
        
        r = requests.get('https://www.robuxshopth.com/shop')
        rate = r.text.split('<div><span class="display-4">')[1].split('</span> <small>Robux per ฿</small></div>')[0]
        embed.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
        embed.add_field(name='เรท / Rate', value='{}'.format(float(rate)))
        await message.channel.send(embed=embed)
    elif message.content.startswith("$"):
        try:
            author = message.author.mention
            number = int(message.content[1:7])
            r = requests.get('https://www.robuxshopth.com/shop')
            rate = r.text.split('<div><span class="display-4">')[1].split('</span> <small>Robux per ฿</small></div>')[0]
            rate = float(rate)
            if number > 0:
                await message.channel.send('{} ถ้าคุณเติม {} บาท คุณได้ {} Robux' .format(author ,number, int(number*rate)))
            else:
                await message.channel.send('{} การเติมขั้นต่ำคือ 1 บาท'.format(author))
        except Exception:
            print('{} dump kid need to {}'.format(message.author,message.content[1:7]))
    if message.content.startswith("!สต๊อก") or message.content.startswith("!สต็อก"):
        r = requests.get('https://www.robuxshopth.com/shop')
        embedc = discord.Embed(
            title = 'ขณะนี้ร้านไม่ได้เปิดให้บริการ',
            colour = discord.Colour.red()
        )

        embedc.set_thumbnail(url='https://uploads.disquscdn.com/images/0b6e508f1141cc48ce30df6b5a90ce425d8abf136009373739d91a390d876bb4.gif')
        embedc.set_author(name='RBS Assistant',icon_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/61020130_423122961753537_5261659881940713472_n.png?_nc_cat=101&_nc_eui2=AeEXwuirsrgC_EDDA4I9j8Mq9usdDkPpfKgwa_enNlapHTg02P6_nZEeEAZ3YXRVojlXm_NWynkTosEkkavDQUqQO5_ufdocI_6SgZ2kxwRmEA&_nc_oc=AQlugUz2tAtuSsSHR_q1Pq_ISjmVN_dwNvGguzna1X9ejMAeeNeApeT5axlSlc1qnJQ&_nc_ht=scontent.fbkk6-2.fna&oh=42231a028b0fa9075bde86f928d587d0&oe=5DBD106E')
        embedc.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
        embedc.add_field(name='ไม่พร้อมจำหน่าย', value='ดูประกาศได้ที่ห้อง 📣announce-ประกาศ' , inline=False)
        embedc.add_field(name='เว็บใซต์ ', value='https://www.robuxshopth.com/shop', inline=False)
        if 'ขณะนี้พร้อมจำหน่ายอีก' in r.text:
            group = r.text.split('<div class="text-center text-muted pt-3 font12">ระบบอัตโนมัติโดยสินค้า Robux จะเข้าในกลุ่ม <b>')[1].split('</b> ภายใน 1 นาทีหลังจากสั่งซื้อ</div>')[0]
            robux = r.text.split('<div class="col-xl-4 m-auto py-2 bg-info rounded text-white text-shadow text-center">ขณะนี้พร้อมจำหน่ายอีก <b>')[1].split('</b> Robux</div>')[0]
            robuxtext = r.text.split('<div class="col-xl-4 m-auto py-2 bg-info rounded text-white text-shadow text-center">')[1].split(' <b>')[0]
            robuxcheck = ('{} {}'.format(robuxtext,robux))
            if robuxcheck <= 'ขณะนี้พร้อมจำหน่ายอีก 100,000': 
                    embed = discord.Embed(
                        colour = discord.Colour.green()
                    )

                    embed.set_thumbnail(url='https://media1.tenor.com/images/f46b1c315b407d231cf0b3856488c410/tenor.gif?itemid=8591394')
                    embed.set_author(name='RBS Assistant',icon_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/61020130_423122961753537_5261659881940713472_n.png?_nc_cat=101&_nc_eui2=AeEXwuirsrgC_EDDA4I9j8Mq9usdDkPpfKgwa_enNlapHTg02P6_nZEeEAZ3YXRVojlXm_NWynkTosEkkavDQUqQO5_ufdocI_6SgZ2kxwRmEA&_nc_oc=AQlugUz2tAtuSsSHR_q1Pq_ISjmVN_dwNvGguzna1X9ejMAeeNeApeT5axlSlc1qnJQ&_nc_ht=scontent.fbkk6-2.fna&oh=42231a028b0fa9075bde86f928d587d0&oe=5DBD106E')
                    embed.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
                    embed.add_field(name='สินค้าที่กำลังจำหน่ายอยู่ในกลุ่ม: {}'.format(group), value='{} Robux'.format(robux), inline=False)
                    embed.add_field(name='เติมได้ผ่านทางเว็บไซต์ ', value='https://www.robuxshopth.com/shop', inline=False)
                    embed.add_field(name='Status', value='⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜')

            if robuxcheck <= 'ขณะนี้พร้อมจำหน่ายอีก 90,000': 
                    embed = discord.Embed(
                        colour = discord.Colour.green()
                    )

                    embed.set_thumbnail(url='https://media1.tenor.com/images/f46b1c315b407d231cf0b3856488c410/tenor.gif?itemid=8591394')
                    embed.set_author(name='RBS Assistant',icon_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/61020130_423122961753537_5261659881940713472_n.png?_nc_cat=101&_nc_eui2=AeEXwuirsrgC_EDDA4I9j8Mq9usdDkPpfKgwa_enNlapHTg02P6_nZEeEAZ3YXRVojlXm_NWynkTosEkkavDQUqQO5_ufdocI_6SgZ2kxwRmEA&_nc_oc=AQlugUz2tAtuSsSHR_q1Pq_ISjmVN_dwNvGguzna1X9ejMAeeNeApeT5axlSlc1qnJQ&_nc_ht=scontent.fbkk6-2.fna&oh=42231a028b0fa9075bde86f928d587d0&oe=5DBD106E')
                    embed.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
                    embed.add_field(name='สินค้าที่กำลังจำหน่ายอยู่ในกลุ่ม: {}'.format(group), value='{} Robux'.format(robux), inline=False)
                    embed.add_field(name='เติมได้ผ่านทางเว็บไซต์ ', value='https://www.robuxshopth.com/shop', inline=False)
                    embed.add_field(name='Status', value='⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛')

            if robuxcheck <= 'ขณะนี้พร้อมจำหน่ายอีก 80,000': 
                    embed = discord.Embed(
                        colour = discord.Colour.green()
                    )

                    embed.set_thumbnail(url='https://media1.tenor.com/images/f46b1c315b407d231cf0b3856488c410/tenor.gif?itemid=8591394')
                    embed.set_author(name='RBS Assistant',icon_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/61020130_423122961753537_5261659881940713472_n.png?_nc_cat=101&_nc_eui2=AeEXwuirsrgC_EDDA4I9j8Mq9usdDkPpfKgwa_enNlapHTg02P6_nZEeEAZ3YXRVojlXm_NWynkTosEkkavDQUqQO5_ufdocI_6SgZ2kxwRmEA&_nc_oc=AQlugUz2tAtuSsSHR_q1Pq_ISjmVN_dwNvGguzna1X9ejMAeeNeApeT5axlSlc1qnJQ&_nc_ht=scontent.fbkk6-2.fna&oh=42231a028b0fa9075bde86f928d587d0&oe=5DBD106E')
                    embed.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
                    embed.add_field(name='สินค้าที่กำลังจำหน่ายอยู่ในกลุ่ม: {}'.format(group), value='{} Robux'.format(robux), inline=False)
                    embed.add_field(name='เติมได้ผ่านทางเว็บไซต์ ', value='https://www.robuxshopth.com/shop', inline=False)
                    embed.add_field(name='Status', value='⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛')

            if robuxcheck <= 'ขณะนี้พร้อมจำหน่ายอีก 70,000': 
                    embed = discord.Embed(
                        colour = discord.Colour.green()
                    )

                    embed.set_thumbnail(url='https://media1.tenor.com/images/f46b1c315b407d231cf0b3856488c410/tenor.gif?itemid=8591394')
                    embed.set_author(name='RBS Assistant',icon_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/61020130_423122961753537_5261659881940713472_n.png?_nc_cat=101&_nc_eui2=AeEXwuirsrgC_EDDA4I9j8Mq9usdDkPpfKgwa_enNlapHTg02P6_nZEeEAZ3YXRVojlXm_NWynkTosEkkavDQUqQO5_ufdocI_6SgZ2kxwRmEA&_nc_oc=AQlugUz2tAtuSsSHR_q1Pq_ISjmVN_dwNvGguzna1X9ejMAeeNeApeT5axlSlc1qnJQ&_nc_ht=scontent.fbkk6-2.fna&oh=42231a028b0fa9075bde86f928d587d0&oe=5DBD106E')
                    embed.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
                    embed.add_field(name='สินค้าที่กำลังจำหน่ายอยู่ในกลุ่ม: {}'.format(group), value='{} Robux'.format(robux), inline=False)
                    embed.add_field(name='เติมได้ผ่านทางเว็บไซต์ ', value='https://www.robuxshopth.com/shop', inline=False)
                    embed.add_field(name='Status', value='⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛')

            if robuxcheck <= 'ขณะนี้พร้อมจำหน่ายอีก 60,000': 
                    embed = discord.Embed(
                        colour = discord.Colour.green()
                    )

                    embed.set_thumbnail(url='https://media1.tenor.com/images/f46b1c315b407d231cf0b3856488c410/tenor.gif?itemid=8591394')
                    embed.set_author(name='RBS Assistant',icon_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/61020130_423122961753537_5261659881940713472_n.png?_nc_cat=101&_nc_eui2=AeEXwuirsrgC_EDDA4I9j8Mq9usdDkPpfKgwa_enNlapHTg02P6_nZEeEAZ3YXRVojlXm_NWynkTosEkkavDQUqQO5_ufdocI_6SgZ2kxwRmEA&_nc_oc=AQlugUz2tAtuSsSHR_q1Pq_ISjmVN_dwNvGguzna1X9ejMAeeNeApeT5axlSlc1qnJQ&_nc_ht=scontent.fbkk6-2.fna&oh=42231a028b0fa9075bde86f928d587d0&oe=5DBD106E')
                    embed.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
                    embed.add_field(name='สินค้าที่กำลังจำหน่ายอยู่ในกลุ่ม: {}'.format(group), value='{} Robux'.format(robux), inline=False)
                    embed.add_field(name='เติมได้ผ่านทางเว็บไซต์ ', value='https://www.robuxshopth.com/shop', inline=False)
                    embed.add_field(name='Status', value='⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛')

            if robuxcheck <= 'ขณะนี้พร้อมจำหน่ายอีก 50,000': 
                    embed = discord.Embed(
                        colour = discord.Colour.green()
                    )

                    embed.set_thumbnail(url='https://media1.tenor.com/images/f46b1c315b407d231cf0b3856488c410/tenor.gif?itemid=8591394')
                    embed.set_author(name='RBS Assistant',icon_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/61020130_423122961753537_5261659881940713472_n.png?_nc_cat=101&_nc_eui2=AeEXwuirsrgC_EDDA4I9j8Mq9usdDkPpfKgwa_enNlapHTg02P6_nZEeEAZ3YXRVojlXm_NWynkTosEkkavDQUqQO5_ufdocI_6SgZ2kxwRmEA&_nc_oc=AQlugUz2tAtuSsSHR_q1Pq_ISjmVN_dwNvGguzna1X9ejMAeeNeApeT5axlSlc1qnJQ&_nc_ht=scontent.fbkk6-2.fna&oh=42231a028b0fa9075bde86f928d587d0&oe=5DBD106E')
                    embed.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
                    embed.add_field(name='สินค้าที่กำลังจำหน่ายอยู่ในกลุ่ม: {}'.format(group), value='{} Robux'.format(robux), inline=False)
                    embed.add_field(name='เติมได้ผ่านทางเว็บไซต์ ', value='https://www.robuxshopth.com/shop', inline=False)
                    embed.add_field(name='Status', value='⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛')

            if robuxcheck <= 'ขณะนี้พร้อมจำหน่ายอีก 40,000': 
                    embed = discord.Embed(
                        colour = discord.Colour.green()
                    )

                    embed.set_thumbnail(url='https://media1.tenor.com/images/f46b1c315b407d231cf0b3856488c410/tenor.gif?itemid=8591394')
                    embed.set_author(name='RBS Assistant',icon_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/61020130_423122961753537_5261659881940713472_n.png?_nc_cat=101&_nc_eui2=AeEXwuirsrgC_EDDA4I9j8Mq9usdDkPpfKgwa_enNlapHTg02P6_nZEeEAZ3YXRVojlXm_NWynkTosEkkavDQUqQO5_ufdocI_6SgZ2kxwRmEA&_nc_oc=AQlugUz2tAtuSsSHR_q1Pq_ISjmVN_dwNvGguzna1X9ejMAeeNeApeT5axlSlc1qnJQ&_nc_ht=scontent.fbkk6-2.fna&oh=42231a028b0fa9075bde86f928d587d0&oe=5DBD106E')
                    embed.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
                    embed.add_field(name='สินค้าที่กำลังจำหน่ายอยู่ในกลุ่ม: {}'.format(group), value='{} Robux'.format(robux), inline=False)
                    embed.add_field(name='เติมได้ผ่านทางเว็บไซต์ ', value='https://www.robuxshopth.com/shop', inline=False)
                    embed.add_field(name='Status', value='⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛')

            if robuxcheck <= 'ขณะนี้พร้อมจำหน่ายอีก 30,000': 
                    embed = discord.Embed(
                        colour = discord.Colour.green()
                    )

                    embed.set_thumbnail(url='https://media1.tenor.com/images/f46b1c315b407d231cf0b3856488c410/tenor.gif?itemid=8591394')
                    embed.set_author(name='RBS Assistant',icon_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/61020130_423122961753537_5261659881940713472_n.png?_nc_cat=101&_nc_eui2=AeEXwuirsrgC_EDDA4I9j8Mq9usdDkPpfKgwa_enNlapHTg02P6_nZEeEAZ3YXRVojlXm_NWynkTosEkkavDQUqQO5_ufdocI_6SgZ2kxwRmEA&_nc_oc=AQlugUz2tAtuSsSHR_q1Pq_ISjmVN_dwNvGguzna1X9ejMAeeNeApeT5axlSlc1qnJQ&_nc_ht=scontent.fbkk6-2.fna&oh=42231a028b0fa9075bde86f928d587d0&oe=5DBD106E')
                    embed.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
                    embed.add_field(name='สินค้าที่กำลังจำหน่ายอยู่ในกลุ่ม: {}'.format(group), value='{} Robux'.format(robux), inline=False)
                    embed.add_field(name='เติมได้ผ่านทางเว็บไซต์ ', value='https://www.robuxshopth.com/shop', inline=False)
                    embed.add_field(name='Status', value='⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛')

            if robuxcheck <= 'ขณะนี้พร้อมจำหน่ายอีก 20,000': 
                    embed = discord.Embed(
                        colour = discord.Colour.green()
                    )

                    embed.set_thumbnail(url='https://media1.tenor.com/images/f46b1c315b407d231cf0b3856488c410/tenor.gif?itemid=8591394')
                    embed.set_author(name='RBS Assistant',icon_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/61020130_423122961753537_5261659881940713472_n.png?_nc_cat=101&_nc_eui2=AeEXwuirsrgC_EDDA4I9j8Mq9usdDkPpfKgwa_enNlapHTg02P6_nZEeEAZ3YXRVojlXm_NWynkTosEkkavDQUqQO5_ufdocI_6SgZ2kxwRmEA&_nc_oc=AQlugUz2tAtuSsSHR_q1Pq_ISjmVN_dwNvGguzna1X9ejMAeeNeApeT5axlSlc1qnJQ&_nc_ht=scontent.fbkk6-2.fna&oh=42231a028b0fa9075bde86f928d587d0&oe=5DBD106E')
                    embed.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
                    embed.add_field(name='สินค้าที่กำลังจำหน่ายอยู่ในกลุ่ม: {}'.format(group), value='{} Robux'.format(robux), inline=False)
                    embed.add_field(name='เติมได้ผ่านทางเว็บไซต์ ', value='https://www.robuxshopth.com/shop', inline=False)
                    embed.add_field(name='Status', value='⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛')
            if robuxcheck <= 'ขณะนี้พร้อมจำหน่ายอีก 10,000': 
                    embed = discord.Embed(
                        colour = discord.Colour.green()
                    )

                    embed.set_thumbnail(url='https://media1.tenor.com/images/f46b1c315b407d231cf0b3856488c410/tenor.gif?itemid=8591394')
                    embed.set_author(name='RBS Assistant',icon_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/61020130_423122961753537_5261659881940713472_n.png?_nc_cat=101&_nc_eui2=AeEXwuirsrgC_EDDA4I9j8Mq9usdDkPpfKgwa_enNlapHTg02P6_nZEeEAZ3YXRVojlXm_NWynkTosEkkavDQUqQO5_ufdocI_6SgZ2kxwRmEA&_nc_oc=AQlugUz2tAtuSsSHR_q1Pq_ISjmVN_dwNvGguzna1X9ejMAeeNeApeT5axlSlc1qnJQ&_nc_ht=scontent.fbkk6-2.fna&oh=42231a028b0fa9075bde86f928d587d0&oe=5DBD106E')
                    embed.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
                    embed.add_field(name='สินค้าที่กำลังจำหน่ายอยู่ในกลุ่ม: {}'.format(group), value='{} Robux'.format(robux), inline=False)
                    embed.add_field(name='เติมได้ผ่านทางเว็บไซต์ ', value='https://www.robuxshopth.com/shop', inline=False)
                    embed.add_field(name='Status', value='⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛')
            if robuxcheck <= 'ขณะนี้พร้อมจำหน่ายอีก 1,000': 
                    embed = discord.Embed(
                        colour = discord.Colour.green()
                    )

                    embed.set_thumbnail(url='https://media1.tenor.com/images/f46b1c315b407d231cf0b3856488c410/tenor.gif?itemid=8591394')
                    embed.set_author(name='RBS Assistant',icon_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/61020130_423122961753537_5261659881940713472_n.png?_nc_cat=101&_nc_eui2=AeEXwuirsrgC_EDDA4I9j8Mq9usdDkPpfKgwa_enNlapHTg02P6_nZEeEAZ3YXRVojlXm_NWynkTosEkkavDQUqQO5_ufdocI_6SgZ2kxwRmEA&_nc_oc=AQlugUz2tAtuSsSHR_q1Pq_ISjmVN_dwNvGguzna1X9ejMAeeNeApeT5axlSlc1qnJQ&_nc_ht=scontent.fbkk6-2.fna&oh=42231a028b0fa9075bde86f928d587d0&oe=5DBD106E')
                    embed.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
                    embed.add_field(name='สินค้าที่กำลังจำหน่ายอยู่ในกลุ่ม: {}'.format(group), value='{} Robux'.format(robux), inline=False)
                    embed.add_field(name='เติมได้ผ่านทางเว็บไซต์ ', value='https://www.robuxshopth.com/shop', inline=False)
                    embed.add_field(name='Status', value='⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛')

            if robux > '0':
                await client.change_presence(status=discord.Status.online, activity=discord.Game('สถานะ: เปิด✔️ '+ robux))
                await message.channel.send(embed=embed)
        else:
            await message.channel.send(embed=embedc)
            await client.change_presence(status=discord.Status.online, activity=discord.Game('สถานะ: ปิด❌'))



    if message.content.startswith("!command") and message.content.startswith("!command"):
        embed = discord.Embed()

        embed.set_author(name='RBS Assistant',icon_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/61020130_423122961753537_5261659881940713472_n.png?_nc_cat=101&_nc_eui2=AeEXwuirsrgC_EDDA4I9j8Mq9usdDkPpfKgwa_enNlapHTg02P6_nZEeEAZ3YXRVojlXm_NWynkTosEkkavDQUqQO5_ufdocI_6SgZ2kxwRmEA&_nc_oc=AQlugUz2tAtuSsSHR_q1Pq_ISjmVN_dwNvGguzna1X9ejMAeeNeApeT5axlSlc1qnJQ&_nc_ht=scontent.fbkk6-2.fna&oh=42231a028b0fa9075bde86f928d587d0&oe=5DBD106E')
        embed.set_footer(text='Power by RobuxshopTH', icon_url='http://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-check-icon.png')
        await message.channel.send('อยากเรียกใช้งานบอทให้พิมว่า !สต๊อก !เติม !เว็บ !เรท $(จำนวนเงิน เช่น $50)')
    if 'เปิดตอนใหน' in message.content[0:80] or 'เปิดตอนเมื่อไหร่' in message.content[0:80] or 'ร้านเปิดกี่โมง' in message.content[0:80] or 'เมื่อไหร่ร้านจะเปิด' in message.content[0:80] or 'ร้านจะเปิดกี่โมง' in message.content[0:80] or 'เปิดตอนไหน' in message.content[0:80] or 'robux มาตอนใหน' in message.content[0:80]:
        r = requests.get('https://www.robuxshopth.com/shop')
        if 'ขณะนี้พร้อมจำหน่ายอีก' in r.text:
            group = r.text.split('<div class="text-center text-muted pt-3 font12">ระบบอัตโนมัติโดยสินค้า Robux จะเข้าในกลุ่ม <b>')[1].split('</b> ภายใน 1 นาทีหลังจากสั่งซื้อ</div>')[0]
            robux = r.text.split('<div class="col-xl-4 m-auto py-2 bg-info rounded text-white text-shadow text-center">ขณะนี้พร้อมจำหน่ายอีก <b>')[1].split('</b> Robux</div>')[0]
            if robux > '0':
                await message.channel.send('ตอนนี้เปิดอยู่นะครับ มีอยู่ {} Robux'.format(robux))
            else:
                await message.channel.send('ตอนนี้ยังไม่เปิดนะครับ รอประกาศจากทางแอดมินนะครับ')

    admin1 = discord.utils.get(message.guild.members, name= '⌜𝓢𝓟⌟ RobuxshopTH✔')
    admin2 = discord.utils.get(message.guild.members, name= 'dOmiino')
    admin3 = discord.utils.get(message.guild.members, name= 'Get my cyka')
    channelcmd = client.get_channel(593062275892510738)
    if admin1 == message.author or admin2 == message.author or admin3 == message.author:
        if message.content.startswith("!ประกาศ ") and message.content[8:1999]:
            messagesb = message.content[8:1999]
            await channelcmd.send('@everyone, {}'.format(messagesb))
        elif message.content.startswith("!talk main ") and message.content[11:1999]:
            messagesb = message.content[11:1999]
            channelmain = client.get_channel(chmain)
            await channelmain.send('{}'.format(messagesb))
        elif message.content.startswith("!talk nsfw ") and message.content[11:1999]:
            messagesb = message.content[11:1999]
            channelmain = client.get_channel(chnsfw)
            await channelmain.send('{}'.format(messagesb))
        elif message.content.startswith("!talk rate ") and message.content[11:1999]:
            messagesb = message.content[11:1999]
            channelmain = client.get_channel(chrate)
            await channelmain.send('{}'.format(messagesb))
        if 'ปิดแล้ว' in message.content[0:80]:
            rbget = requests.get('https://www.robuxshopth.com/shop')
            if 'รายละเอียดสินค้า' in rbget.text:
                if 'ขณะนี้พร้อมจำหน่ายอีก' in rbget.text:
                    robux = rbget.text.split('<div class="col-xl-4 m-auto py-2 bg-info rounded text-white text-shadow text-center">ขณะนี้พร้อมจำหน่ายอีก <b>')[1].split('</b> Robux</div>')[0]
                    if robux > '0':
                        await client.change_presence(status=discord.Status.online, activity=discord.Game('สถานะ: เปิด✔️ '+ robux))
                else:
                    await client.change_presence(status=discord.Status.online, activity=discord.Game('สถานะ: ปิด❌'))
            else:
                await message.channel.send('Error Code: Please Contact Admin Mosquito to fix this')

client.run('TOKEN HERE')
