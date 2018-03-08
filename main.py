# Copyright (c) 2018 by your name. All Rights Reserved.

__author__ = 'Ahmad Abdulnasir <dabolinux@gmail.com> www.dabolinux.com'
__copyright__ = 'Copyright (c) 2016, salafi'
__version__ = "3.1"

import sqlite3
import sys
import os
import time
import android
from random import randint as ran

droid = android.Android()
decimal_decoder = lambda s: int(s, 10)
decimal_encoder = lambda i: str(i)
working_space = os.getcwd()
j = sys.argv
k = j[0].split('/')
go = k[1:-1]
moo = '/'.join(go)
w_sp = '/'+moo
os.chdir(w_sp)
def fileinfo():
    global db
    if os.path.isfile(w_sp+'/ver.sqlite'):
        os.chdir(w_sp)
        db = sqlite3.connect('ver.sqlite')
    else:
        print('Error Unknown database')
        sys.exit(1)
def get_users():
    db.row_factory = lambda cursor, row: row[0]
    c = db.cursor()
    users = c.execute('SELECT user FROM users').fetchall()
    return users
def get_id():
    db.row_factory = lambda cursor, row: row[0]
    c = db.cursor()
    ids = c.execute('SELECT id FROM users').fetchall()
    return ids
def dev():
    db.row_factory = lambda cursor, row: row[0]
    c = db.cursor()
    devo = c.execute('SELECT item FROM developer').fetchall()
    return devo
def amount():
    db.row_factory = lambda cursor, row: row[0]
    c = db.cursor()
    amt = c.execute('SELECT amt FROM amount').fetchall()
    amount = amt[0]
    return amount

def user(username):
    users = get_users()
    ids = get_id()
    gida = dict(zip(users, ids))
    if username in gida.keys():
        uni = gida[username]
        print('Unique id is', uni)
        return uni
    else:
        username not in gida.keys()
        print('Asses Denied for %s, sending with developers ID' %username)
        luck = dev()
        lucky = ran(0,1)
        uni = luck[lucky]
        print(uni)
    db.close()
    return uni
#### Block to generate valid imei ####
def gen(n, imei):
    array = []
    physics = list(range(0,n))
    for i in physics:
        valid_luhn = generate(str(imei+i))
        imeic = str(imei+i)+valid_luhn
        array.append(imeic)
    return array
def notgen(n, imei):
    array = []
    physics = list(range(0,n))
    for i in physics:
        check = str(ran(0,9))
        imeic = str(imei+i)+check
        array.append(imeic)
    return array
### Block to generate 9 imei's ###
def spam(array):
    count = 0
    physics = array
    egg = len(physics)
    ko = []
    while count <= egg:
        jojo = []
        su0 = str(physics.pop(0))
        jojo.append(su0)
        su1 = str(physics.pop(0))
        jojo.append(su1)
        su2 = str(physics.pop(0))
        jojo.append(su2)
        su3 = str(physics.pop(0))
        jojo.append(su3)
        su4 = str(physics.pop(0))
        jojo.append(su4)
        su5 = str(physics.pop(0))
        jojo.append(su5)
        su6 = str(physics.pop(0))
        jojo.append(su6)
        su7 = str(physics.pop(0))
        jojo.append(su7)
        su8 = str(physics.pop(0))
        jojo.append(su8)
        sp = ','
        msg = sp.join(jojo)

        ko.append(msg)
        del jojo
        count +=9
        if len(physics) == 0:
            break
        else:
            continue
    return ko
def aisha():
    user_name = input('Username? : ')
    uni = user(user_name)
    n = amount()
    #n = int(input('Amount?: '))
    if n % 9 != 0:
       print('Error, cant send with', n)
       sys.exit(1)
    else:
        pass
    imei = input('imei?: ')
    if imei.isdigit() and len(imei) == 14:
        print('Imei is Good')
    elif imei.isalnum() and len(imei) == 14:
        print('Imei is only Numbers')
        sys.exit(1)
    elif len(imei) != 14:
        print('Only 14 digit of imei supported')
        sys.exit(1)
    else:
        print('Unrecognised imei')
        sys.exit(1)
    check = input('''a. Send With valid Generation
b. Send without valid Generation
   :   ''')
    if check.lower() == 'a':
        print('Sending With valid generation')
        print('\vGenerating Imei, wait a bit ...')
        array = gen(n, int(imei))
        physics = spam(array)
        with_gen(uni, physics)
    elif check.lower() == 'b':
        print('Sending Without valid generation')
        print('\vArranging Imei, wait a bit ...')
        array = notgen(n, int(imei))
        physics = spam(array)
        without_gen(uni, physics)
    else:
        print("Error answer with 'a or  b' ")
        sys.exit(1)
def halo():
    h = time.localtime()
    strh = str(h)
    go = strh.split('(')
    fo = go[1]
    print(' ')
    fofo = fo.split(', ')
    if fofo[1] in get_permission():
        exit_point = True
        return True
    else:
        con = get_contact()
        print('Usage time up,\v Contact Developer @\n\t', con)
        exit_point = False
        return False
    return exit_point


def luhn(string, base=10, decoder=decimal_decoder):
    digits = list(map(decoder, string))
    return (
        sum(digits[::-2]) +
        sum(list(map(lambda d: sum(divmod(2 * d, base)), digits[-2::-2])))
    ) % base
def generate(string, base=10, encoder=decimal_encoder, decoder=decimal_decoder):

    d = luhn(string + encoder(0), base=base, decoder=decoder)
    if d != 0:
        d = base - d
    return encoder(d)

def get_permission():
    db.row_factory = lambda cursor, row: row[0]
    c = db.cursor()
    permission = c.execute('SELECT allow FROM date').fetchall()
    return permission

def get_contact():
    contact = dev()[2]
    return contact

def with_gen(uni, physics):
    fo = '#'
    for atom in physics:
        star = str(physics.index(atom)*9)
        element = len(physics)*9
        print()
        print('Sent %s of %s' %(star, element) )
        print('sending...\n', atom)
        electron = ('Sub data%s%s%s' %(uni,fo,atom))
        droid.smsSend('4030',electron)
        time.sleep(2.5)
        last = electron.split(',')
        last = last[-1]
    droid.ttsSpeak("Job done boss")
    print('*************Done*************')
    print('Your last send imei is %s' %last)
    print()
    droid.vibrate(1000)
    time.sleep(1)
    droid.vibrate(1000)
    droid.setClipboard(last)
    droid.makeToast('Done, Finished Sending')
def without_gen(uni, physics):
    fo = '#'
    for atom in physics:
        star = str(physics.index(atom)*5)
        element = len(physics)*5
        print()
        print('Sent %s of %s' %(star, element) )
        print('sending...\n', atom)
        electron = 'Sub data%s%s%s' %(uni,fo,atom)
        droid.smsSend('4030',electron)
        time.sleep(2)
        last = electron.split(',')
        last = last[-1]
    droid.ttsSpeak("Job done boss")
    print('*************Done*************')
    print('Your last send imei is %s' %last)
    print()
    droid.vibrate(1000)
    time.sleep(1)
    droid.vibrate(1000)
    droid.setClipboard(last)
    droid.makeToast('Done, Finished Sending')
if __name__ == '__main__':
    afileinfo()
    if halo():
        aisha()
    else:
        print('Sorry')
else:
    print("I'm a module, cound't run completley")
