from flask import Flask, redirect, abort

app = Flask(__name__)

@app.route('/<channel_slug>')
def channel_redirect(channel_slug):
    # channel_slug içinde güvenlik veya geçersiz karakter kontrolü yapılabilir,
    # ancak doğrudan istediğin mantığı uyguluyoruz:
    
    if '_' not in channel_slug:
        # Alt çizgi yoksa TR yoluna yönlendir
        target_url = f"http://exchange.cdnrdn.com:9090/TR/{channel_slug}-tr/index.m3u8?token=filbox_oztnvqmfK83KS"
    else:
        # Alt çizgi varsa TR-N yoluna yönlendir
        target_url = f"http://exchange.cdnrdn.com:9090/TR-N/{channel_slug}-tr/index.m3u8?token=filbox_oztnvqmfK83KS"
        
    # 302 (Geçici) veya 301 (Kalıcı) yönlendirme yapabiliriz. 
    # M3U8 oynatıcılar genellikle geçici yönlendirmeyi (302) daha iyi destekler.
    return redirect(target_url, code=302)

if __name__ == '__main__':
    # Flask uygulamasını yerelde 5000 portunda başlatır
    app.run(host='0.0.0.0', port=5000, debug=True)
