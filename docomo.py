# -*- coding: utf-8 -*-
import urllib.request,json,sys
import key


def docomo(_mode):
    url = "https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY="
#    api_key = "5534676c4151462f5875467370787576482e694538337a6864674e5255454a54552f62355866496a414730"
    key_class = key.Key()
    api_key = key_class.api

    method = "POST"
    headers = {"Content-Type":"application/json"}
    mode = _mode


    obj = {"utt":"元気","mode":mode}
    json_data = json.dumps(obj).encode("utf-8")

    request = urllib.request.Request(url+api_key,data=json_data,method=method,headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
    print(response_body)


argvs = sys.argv
docomo(argvs[1])
