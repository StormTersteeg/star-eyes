import webview, os, sys
from Crypto.Cipher import AES
import base64

def on_closed():
  pass

def on_closing():
  pass

def on_shown():
  pass

def on_loaded():
  pass

class Api:
  def encrypt(self, data, key):
    data = bytes(data, 'utf-8')
    key = bytes(self.prepare_key(key), 'utf-8')

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    encrypted_lines = [ x for x in (cipher.nonce, tag, ciphertext) ]
    result = base64.b64encode(str(encrypted_lines).encode('utf-8'))
    return result.decode('utf-8')

  def decrypt(self, data, key):
    data = bytes(base64.b64decode(data).decode('utf-8'), 'utf-8')
    key = bytes(self.prepare_key(key), 'utf-8')

    nonce, tag, ciphertext = eval(data)

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data.decode('utf-8')

  def prepare_key(self, key):
    while len(key) < 32:
      key += key
    return base64.b64encode(key.encode('utf-8')).decode('utf-8')[0:32]

  def openChild(self, url):
    window.hide()
    webview.create_window(url, url)

  def minimize(self):
    window.minimize()

  def fullscreen(self):
    window.toggle_fullscreen()

  def close(self):
    window.destroy()

  def reload(self):
    os.startfile(sys.argv[0])
    self.close()

#!FLAG-HTML

if __name__ == '__main__':
  api = Api()
  window = webview.create_window("{settings.app_name}", html=html, js_api=api, width={settings.app_proportions[0]}, height={settings.app_proportions[1]}, confirm_close={settings.app_confirm_close}, frameless={settings.app_frameless}, fullscreen={settings.app_fullscreen}, resizable={settings.app_resizable})
  window.events.closed += on_closed
  window.events.closing += on_closing
  window.events.shown += on_shown
  window.events.loaded += on_loaded
  webview.start(gui="{settings.app_web_engine}", debug={settings.app_allow_inspect})