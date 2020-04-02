import web
import fft
import toBase64
import json
import highPassFilter
import lowPassFilter

urls = (
    '/', 'Index',
    '/high', 'HighPass',
    '/low', 'LowPass'
)


class Index:

    def GET(self):
        web.header('Access-Control-Allow-Origin', '')
        return 2

    def POST(self):

        web.header('Access-Control-Allow-Origin', 'http://49.233.200.100:4001')
        web.header('content-type', 'json')

        file = web.input().get('file', '')
        high_frequency = int(web.input().get('high_frequency', ''))
        low_frequency = int(web.input().get('low_frequency', ''))
        if file == '' or high_frequency == '' or low_frequency == '':
            return
        print(file[0:100])
        file = file.split(',', maxsplit=1)[1]

        img = toBase64.to_image(file)

        fft_img = toBase64.to_base64(fft.fft(img))

        high_pass_img = toBase64.to_base64(highPassFilter.high_pass_filter(img, high_frequency))

        low_pass_img = toBase64.to_base64(lowPassFilter.low_pass_filter(img, low_frequency))

        data = {
            'fft': fft_img,
            'high_pass': high_pass_img,
            'low_pass': low_pass_img
        }
        return json.dumps(data)


class HighPass:

    def POST(self):

        web.header('Access-Control-Allow-Origin', 'http://49.233.200.100:4001')
        web.header('content-type', 'json')

        file = web.input().get('file', '')
        high_frequency = int(web.input().get('high_frequency', ''))
        if file == '' or high_frequency == '':
            return
        print(file[0:100])
        file = file.split(',', maxsplit=1)[1]

        img = toBase64.to_image(file)

        high_pass_img = toBase64.to_base64(highPassFilter.high_pass_filter(img, high_frequency))

        data = {
            'high_pass': high_pass_img
        }
        return json.dumps(data)


class LowPass:

    def POST(self):
        web.header('Access-Control-Allow-Origin', 'http://49.233.200.100:4001')
        web.header('content-type', 'json')

        file = web.input().get('file', '')
        low_frequency = int(web.input().get('low_frequency', ''))
        if file == '' or low_frequency == '':
            return
        print(file[0:100])
        file = file.split(',', maxsplit=1)[1]

        img = toBase64.to_image(file)

        low_pass_img = toBase64.to_base64(lowPassFilter.low_pass_filter(img, low_frequency))

        data = {
            'low_pass': low_pass_img
        }
        return json.dumps(data)


app = web.application(urls, globals())

application = app.wsgifunc()
