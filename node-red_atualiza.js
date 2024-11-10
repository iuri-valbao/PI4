msg.payload = {
  temperatura: global.get('temperatura') || { media12: 0, media24: 0 },
  oxigenio: global.get('oxigenio') || { media12: 0, media24: 0 },
  ph: global.get('ph') || { media12: 0, media24: 0 }
};
return msg;