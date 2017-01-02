# -*- coding: utf-8 -*-
import urllib.request,json,sys,subprocess
import key


def docomo(_utt,_context):
    url = "https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY="
#    api_key = "5534676c4151462f5875467370787576482e694538337a6864674e5255454a54552f62355866496a414730"
    key_class = key.Key()
    api_key = key_class.api
    if _context is None:
      context = ""
    else:
      context = _context

    method = "POST"
    headers = {"Content-Type":"application/json"}
    mode = "dialog"
    utt = _utt

    obj = {"utt":_utt,"mode":mode,"context":context}
    json_data = json.dumps(obj).encode("utf-8")

    request = urllib.request.Request(url+api_key,data=json_data,method=method,headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
#    print(response_body)
    json_obj = json.loads(response_body)
    keylist = json_obj.keys()
    for k in keylist:
      if k=="utt":
        _utt = (json_obj[k])
        print(json_obj[k])
      if k=="context":
        _context = (json_obj[k])
#        docomo(json_obj[k])
    else:
      subprocess.call("zunko/echoseika.exe -cv ZUNKO_EX "+_utt)
      _utt = input()
      if(_utt == "ばいばい"):
        return

      docomo(_utt,_context)
    





argvs = sys.argv
docomo(argvs[1],None)
