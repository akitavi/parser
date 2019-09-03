#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--error_code', action="store_true",
                    help='Print only error code')
parser.add_argument('-a', '--all', action="store_true",
                    help='Print all info')
parser.add_argument('-H', '--headers', action="store_true",
                    help='Print only headers')
parser.add_argument('-c', '--cookies', action="store_true",
                    help='Print only cookies')
parser.add_argument('-t', '--time', action="store_true",
                    help='Print page load time ')
parser.add_argument('-u', '--url', nargs='*', type=str,
                    required=True, help='This url will be pars')
res = parser.parse_args()


timeout = 10

if res.all:
    for i in res.url:
        print('URL: ' + str(i))
        try:
            start = time.time()
            r = requests.get(i, timeout=timeout)
            stop_time = time.time()
            full_time = stop_time - start
            print('URL: ' + str(i))
            print('\n' + 'Total time: ' + str(round(full_time, 2)) + ' sec.')
            print('\n' + 'НTTP Headers found: ')
            for i in r.headers.items():
                print('   ' + str(i))

            print('\n' + 'Сookies found: \n' + str(r.cookies.items()))
            print('\n' + 'Error code: ' + str(r.status_code) +
                  '\n\n **************************** \n')
        except requests.exceptions.ConnectTimeout:
            print('Timeout')
        except requests.exceptions.ConnectionError as e:
            print('Connection error to: ' + str(i) + '\n')

elif res.error_code:
    for i in res.url:
        print('URL: ' + str(i))
        try:
            start = time.time()
            r = requests.get(i, timeout=timeout)
            stop_time = time.time()
            full_time = stop_time - start
            print('\n' + 'Error code: ' + str(r.status_code) +
                  '\n\n ********* \n')
        except requests.exceptions.ConnectTimeout:
            rint('Connect Timeout to: ' + str(i))
        except requests.exceptions.ConnectionError as e:
            print('Connection error to: ' + i + '\n ********* \n')

elif res.headers:
    for i in res.url:
        print('URL: ' + str(i))
        try:
            start = time.time()
            r = requests.get(i, timeout=timeout)
            stop_time = time.time()
            full_time = stop_time - start
            print('НTTP Headers found: ' + '\n')
            for n in r.headers.items():
                print('   ' + str(n))
            print('*********' + '\n')
        except requests.exceptions.ConnectTimeout:
            print('Connect Timeout to: ' + str(i) + '\n ********* \n')
        except requests.exceptions.MissingSchema:
            print('Wrong URLs: ' + str(i) + '\n ********* \n')
        except requests.exceptions.ConnectionError as e:
            print('Connection error to: ' + i + '\n ********* \n')

elif res.cookies:
    for i in res.url:
        i = str(i)
        try:
            start = time.time()
            r = requests.get(i, timeout=timeout)
            stop_time = time.time()
            full_time = stop_time - start
            print('URL: ' + i)
            print('\n' + 'Сookies found: \n' + str(r.cookies.items()))
            print('*********' + '\n')
        except requests.exceptions.ConnectTimeout:
            print('Connect Timeout to: ' + str(i) + '\n ********* \n')
        except requests.exceptions.MissingSchema:
            print('Wrong URLs: ' + str(i) + '\n ********* \n')
        except requests.exceptions.ConnectionError as e:
            print('Connection error to: ' + i + '\n ********* \n')

elif res.time:
    for i in res.url:
        print('URL: ' + str(i))
        try:
            start = time.time()
            r = requests.get(i, timeout=timeout)
            stop_time = time.time()
            full_time = stop_time - start
            print('Loading time: ' + str(round(full_time, 2)) + ' sec.')
            print('*********' + '\n')
        except requests.exceptions.ConnectTimeout:
            print('Connect Timeout to: ' + str(i) + '\n ********* \n')
        except requests.exceptions.MissingSchema:
            print('Wrong URLs: ' + str(i) + '\n ********* \n')
        except requests.exceptions.ConnectionError as e:
            print('Connection error to: ' + str(i) + '\n ********* \n')


else:
    for i in res.url:
        try:
            start = time.time()
            r = requests.get(i, timeout=timeout)
            stop_time = time.time()
            full_time = stop_time - start
            if r.status_code == 200:
                print('0')
            else:
                print(str(r.status_code))

        except requests.exceptions.ConnectTimeout:
            print('1')
        except requests.exceptions.MissingSchema:
            print('2')
        except requests.exceptions.RequestException as e:
            print('3')
