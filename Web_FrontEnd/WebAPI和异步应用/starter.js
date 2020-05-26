projectData = {};

const express = require('express')
const app = express();
const bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());

const cors = require
app.use(express.static('website'));

const port = 3000;