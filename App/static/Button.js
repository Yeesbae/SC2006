const nameList = [
  'Time', 'Past', 'Future', 'Dev',
  'Fly', 'Flying', 'Soar', 'Soaring', 'Power', 'Falling',
  'Fall', 'Jump', 'Cliff', 'Mountain', 'Rend', 'Red', 'Blue',
  'Green', 'Yellow', 'Gold', 'Demon', 'Demonic', 'Panda', 'Cat',
  'Kitty', 'Kitten', 'Zero', 'Memory', 'Trooper', 'XX', 'Bandit',
  'Fear', 'Light', 'Glow', 'Tread', 'Deep', 'Deeper', 'Deepest',
  'Mine', 'Your', 'Worst', 'Enemy', 'Hostile', 'Force', 'Video',
  'Game', 'Donkey', 'Mule', 'Colt', 'Cult', 'Cultist', 'Magnum',
  'Gun', 'Assault', 'Recon', 'Trap', 'Trapper', 'Redeem', 'Code',
  'Script', 'Writer', 'Near', 'Close', 'Open', 'Cube', 'Circle',
  'Geo', 'Genome', 'Germ', 'Spaz', 'Shot', 'Echo', 'Beta', 'Alpha',
  'Gamma', 'Omega', 'Seal', 'Squid', 'Money', 'Cash', 'Lord', 'King',
  'Duke', 'Rest', 'Fire', 'Flame', 'Morrow', 'Break', 'Breaker', 'Numb',
  'Ice', 'Cold', 'Rotten', 'Sick', 'Sickly', 'Janitor', 'Camel', 'Rooster',
  'Sand', 'Desert', 'Dessert', 'Hurdle', 'Racer', 'Eraser', 'Erase', 'Big',
  'Small', 'Short', 'Tall', 'Sith', 'Bounty', 'Hunter', 'Cracked', 'Broken',
  'Sad', 'Happy', 'Joy', 'Joyful', 'Crimson', 'Destiny', 'Deceit', 'Lies',
  'Lie', 'Honest', 'Destined', 'Bloxxer', 'Hawk', 'Eagle', 'Hawker', 'Walker',
  'Zombie', 'Sarge', 'Capt', 'Captain', 'Punch', 'One', 'Two', 'Uno', 'Slice',
  'Slash', 'Melt', 'Melted', 'Melting', 'Fell', 'Wolf', 'Hound',
  'Legacy', 'Sharp', 'Dead', 'Mew', 'Chuckle', 'Bubba', 'Bubble', 'Sandwich',
  'Smasher', 'Extreme', 'Multi', 'Universe', 'Ultimate', 'Death', 'Ready', 'Monkey',
  'Elevator', 'Wrench', 'Grease', 'Head', 'Theme', 'Grand', 'Cool', 'Kid', 'Boy', 'Girl', 'Vortex', 'Paradox'
];

function randomName() {
  const firstName = nameList[Math.floor(Math.random() * nameList.length)];
  const lastName = nameList[Math.floor(Math.random() * nameList.length)];
  return {first: firstName, last: lastName};
}

function addDummy() {
    // alert("Hello from a static file!");
    const name = randomName();

    const data = {
      username: "testuser",
      password: "testpassword",
      email: "test@example.com",
      // first_name: name.first,
      // last_name: name.last,
      first_name: "Test",
      last_name: "Test",
      date_of_birth: "1990-01-01"
    }

    console.log('Updated Data:', data);

  fetch('api/create-user/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
  },
      body: JSON.stringify(data)
  })

  .then(response => response.json())

  .then(data => {
    console.log('Success:', data);
    // alert('Data saved successfully');
  })

  .catch((error) => {
    console.error('Error:', error);
    // alert('Failed to save data');
  });
}

function deleteLatestEntry() {
  fetch('/api/delete-latest/', {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    }
  })

  .then(response => response.json())
  
  .then(data => {
    if (data.status === 'success') {
      console.log('Latest entry deleted successfully');
      // alert('Latest entry deleted successfully');
    } else {
      console.log('Nothing to delete');
      // alert('Nothing to delete');
    }
  })

  .catch((error) => {
    console.error('Error:', error);
    // alert('Failed to delete entry.');
  });
}

function deleteAllEntry() {
  fetch('/api/delete-all/', {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    }
  })

  .then(response => response.json())

  .then(data => {
    if (data.status === 'success') {
      console.log('All entries deleted successfully');
      // alert('All entries deleted successfully');
    } else {
      console.log('Nothing to delete');
      // alert('Nothing to delete');
    }
  })

  .catch((error) => {
      console.error('Error:', error);
      // alert('Failed to delete entries');
  });
}

function deleteSpecificEntry() {
  fetch('/api/delete-user/', {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    }
  })

  .then(response => response.json())

  .then(data => {
    if (data.status === 'success') {
      console.log('User deleted successfully');
      // alert('All entries deleted successfully');
    } else {
      console.log('Nothing to delete');
      // alert('Nothing to delete');
    }
  })

  .catch((error) => {
    console.error('Error:', error);
    // alert('Failed to delete entries');
  });
}

function getApiData() {

}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.startsWith(name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
      }
  }
  return cookieValue;
}