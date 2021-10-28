# Nginx 에 Certbot을 통한 무료 SSL인증서 적용

## certbot을 설치 하기 위해 먼저 repository 를 등록
```linux
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
```

## certbot 설치
```linux
sudo apt-get install certbot
```


## Certbot nginx plugin 설치
```linux
sudo apt-get install python-certbot-nginx
```

## 인증서 발급

## 특정 도메인에 대하여 인증서 발급
```linux
sudo certbot --nginx -d www.example.com --email admin@example.com --agree-tos
```


## 적용된 서버 설정
```
cd /etc/nginx/sites-available

sudo chmod 777 default

vi default
```
위 명령어를 통해 nginx 서버블락이 설정된 default파일을 확인해보면 아래와 같다.
첫 번째 서버블락에는 http 요청이 들어오면 https로 리다이렉트를 해주는 부분이다.
http 기본포트 80
https 기본포트 443

```linux
Server {
    listen 80;
    server_name kdt-vm-0202011.koreacentral.cloudapp.azure.com/;
    charset utf-8;

    location / {
        return 307 https://kdt-vm-0202011.koreacentral.cloudapp.azure.com/$request_uri;
    }
}

server {
    listen 443;
    listen [::]:443;                                                                          ssl on;
    server_name kdt-vm-0202007.koreacentral.cloudapp.azure.com;                               ssl_certificate /etc/letsencrypt/live/kdt-vm-0202007.koreacentral.cloudapp.azure.com/fullchain.pem;                                                                                 ssl_certificate_key /etc/letsencrypt/live/kdt-vm-0202007.koreacentral.cloudapp.azure.com/privkey.pem;
    location / {                                                                                  proxy_set_header X-Forwarded-For $host;
        proxy_set_header X-Forwarded-Proto $scheme;                                               proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;

        root /app/build;
        index index.html index.htm;
        try_files $uri /index.html = 404;
    }

    location /api {          
            proxy_pass http://backend:5000/;                                            
        }                                                                                    
}
```



