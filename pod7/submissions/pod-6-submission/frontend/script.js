document.addEventListener('DOMContentLoaded', () => {
    fetch('http://localhost:3001/api/data')
      .then(response => response.json())
      .then(data => {
        const output = document.getElementById('output');
        output.textContent = `Received data from server: ${data.message}`;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        const output = document.getElementById('output');
        output.textContent = 'An error occurred while fetching data.';
      });
  });