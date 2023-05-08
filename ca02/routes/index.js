const router = require("express").Router();
// define relevant routes
const pw_auth_router = require('./pwauth')
const homeRouter = require('./home');
const aboutRouter = require('./about');
const teamRouter = require('./team');
const jokeRouter = require('./joke');
const horrorRouter = require('./horror');
const rapRouter = require('./rap');
const grammarRouter = require('./grammar');
const movieRouter = require('./movie');


// configure router to use above routes
router.use(pw_auth_router);
router.use(homeRouter);
router.use(aboutRouter);
router.use(teamRouter);
router.use(jokeRouter);
router.use(horrorRouter);
router.use(rapRouter);
router.use(grammarRouter);
router.use(movieRouter);

module.exports = router;