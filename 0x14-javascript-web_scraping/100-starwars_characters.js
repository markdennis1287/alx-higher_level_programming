const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a valid Movie ID as an argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    if (characters.length === 0) {
      console.log('No characters found for this movie.');
    } else {
      getCharacterNames(characters, 0);
    }
  } else {
    console.error('Error fetching movie data:', error);
  }
});

function getCharacterNames(characters, index) {
  if (index < characters.length) {
    request(characters[index], (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        getCharacterNames(characters, index + 1);
      } else {
        console.error('Error fetching character data:', error);
      }
    });
  }
}
