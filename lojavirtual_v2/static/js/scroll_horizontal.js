addEventListener('click', (event) => {
    if (event.target.id === 'next') {
      document.getElementById('scrollSection').scrollBy(500, 0);
    };
    if (event.target.id === 'back') {
      document.getElementById('scrollSection').scrollBy(-500, 0);
    };
  })