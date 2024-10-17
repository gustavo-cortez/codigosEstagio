const express = require('express');
const router = express.Router();
const dogsController = require('../Controller/dogController');

router.get('/:breed', dogsController.getDogImage);

module.exports = router;
