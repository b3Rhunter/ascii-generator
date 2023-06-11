// server.js
const express = require('express');
const cors = require('cors');
const figlet = require('figlet');

const app = express();

app.use(cors());
app.use(express.json());

app.post('/ascii', (req, res) => {
  const text = req.body.text;
  const font = req.body.font;
  
  figlet.text(text, { font: font }, function(err, data) {
    if (err) {
      console.error('Something went wrong...', err);
      return res.status(500).send(err);
    }
    res.send({ ascii: data });
  });
});

app.listen(3001, () => console.log('Server running on port 3001'));
