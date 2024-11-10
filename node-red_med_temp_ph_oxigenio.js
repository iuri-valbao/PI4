// Inicialize a memória de leituras do sensor se ainda não existir
if (!context.leituras) context.leituras = [];

// Adiciona a nova leitura ao array de leituras
context.leituras.push(parseFloat(msg.payload));

// Limite o histórico para as últimas 24 leituras
if (context.leituras.length > 24) context.leituras.shift();

// Calcula a média das últimas 12 e 24 leituras
const ultimas12 = context.leituras.slice(-12);
const ultimas24 = context.leituras.slice(-24);

const media12 = ultimas12.reduce((a, b) => a + b, 0) / ultimas12.length || 0;
const media24 = ultimas24.reduce((a, b) => a + b, 0) / ultimas24.length || 0;

// Envia a média como payload
msg.payload = { media12, media24 };
return msg;