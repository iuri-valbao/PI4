msg.payload = {
  temperatura: global.get('temperatura') || { media12: 0, media24: 0 },
  umidade: global.get('umidade') || { media12: 0, media24: 0 },
  ph: global.get('ph') || { media12: 0, media24: 0 }
};
return msg;