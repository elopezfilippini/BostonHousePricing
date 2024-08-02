function submitForm() {
    console.log("aqui estoy ")
    const form = document.getElementById('prediction-form');
    const formData = new FormData(form);

    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

 
    const datanumerica = [];
    formData.forEach((value) => {
        datanumerica.push(parseFloat(value) || 0); // Convert to float, or use 0 if not a number
    });

    console.log("la data numerica es ", datanumerica);

    fetch('/predict_api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(datanumerica),
    })
    .then(response => response.json())
    .then(result => {
        alert('Prediction: ' + (result || 'No prediction returned'));
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });
}