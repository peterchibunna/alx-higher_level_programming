#!/usr/bin/node
const fs1 = require('fs');
const a = fs1.readFileSync(process.argv[2], 'utf8');
const b = fs1.readFileSync(process.argv[3], 'utf8');
fs1.writeFileSync(process.argv[4], a + b);
