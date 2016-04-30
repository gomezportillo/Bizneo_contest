#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests

counter = 1

while True:
    counter = counter + 2
    user = 'pedroma'+str(counter)

    s = requests.Session()
    token = s.get("http://161.67.212.131:3003/").text

    token = token.split('<meta name="csrf-token" content="')[1].split('"')[0]
    print token

    parameters_user = {'utf8':u'\xe2',
                  'authenticity_token':token,
                  'participant[email]':'pedroma@gmail.com',
                  'participant[password]':'12345678',
                  'commit':'Iniciar+sesion'}

    token = s.post("http://161.67.212.131:3003/participants/sign_in", params = parameters_user).text

    token = token.split('<meta name="csrf-token" content="')[1].split('"')[0]

    parameters_bot = {'utf8':u'\xe2','authenticity_token':token,
                      'user[participant_id]':'7',
                      'user[name]':user,
                      'user[email]':user+'@gmail.com',
                      'user[password]':'12345678',
                      'user[password_confirmation]':'12345678',
                      'commit':'Registrar+aliado'}

    b = s.post("http://161.67.212.131:3003/users", params = parameters_bot)
