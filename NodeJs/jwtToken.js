const NodeRSA = require('node-rsa');
const jwt = require('jsonwebtoken');

function generateKeyPair() {
  const key = new NodeRSA({ b: 2048 });
  const privatePem = key.exportKey('pkcs1-private-pem');
  const publicPem = key.exportKey('pkcs1-public-pem');
  return { privateKey: privatePem, publicKey: publicPem };
}

function encodeJWT(payload, privateKey) {
  return jwt.sign(payload, privateKey, { algorithm: 'RS256' });
}

function decodeJWT(token, publicKey) {
  return jwt.verify(token, publicKey, { algorithms: ['RS256'] });
}

const { privateKey, publicKey } = generateKeyPair();
console.log("Private Key:\n", privateKey);
console.log("\nPublic Key:\n", publicKey);

const payload = { user_id: 123, phone_number: "9730614299" };

const encodedJWT = encodeJWT(payload, privateKey);
console.log("\nEncoded JWT:\n", encodedJWT);

const decodedPayload = decodeJWT(encodedJWT, publicKey);
console.log("\nDecoded Payload:\n", decodedPayload);

