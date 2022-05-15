import os , requests , time , random , user_agent
abc ='ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'
abc1 ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cho='5' #input("Input numper: ")


tok = input(' [?] التوكن ياقلب امك -> ')
ID = input(' [?] الايدى ياقلب امك -> ')

if cho == '5'or cho =='05':
    while True:
        user = str(''.join((random.choice(abc) for i in range(4))))
        url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
        head = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '1176',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
'origin': 'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': user_agent.generate_user_agent(),
'x-asbd-id':'198387' ,
'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
'x-instagram-ajax': '72bda6b1d047',
'x-requested-with': 'XMLHttpRequest'
}
        data = {
'email' : 'a@gmail.com',
'username': (f'{user}'),
'first_name': 'AA',
'opt_into_one_tap': 'false'
}  
        uS = requests.post(url, headers=head, data=data).text
        Uss =  ('{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}')
        if Uss in uS:
            requests.get(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=(<^>) user instagram ~> {user}\n\nby :  @vvvvvnm9')
            print(f' \033[1;32m {user}')
        else:
            time.sleep(1)
            print(f' \033[1;31m NOT AVAILABLE : {user}')