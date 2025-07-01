const $RefParser = require('@apidevtools/json-schema-ref-parser');
const fs = require('fs');

const input = process.argv[2];
const output = process.argv[3];

if (!input || !output) {
  console.error('Usage: node flatten.js input.json output.json');
  process.exit(1);
}

$RefParser.dereference(input)
  .then(schema => {
    fs.writeFileSync(output, JSON.stringify(schema, null, 2));
    console.log(`Flattened schema written to ${output}`);
  })
  .catch(err => {
    console.error(err);
    process.exit(1);
  }); 