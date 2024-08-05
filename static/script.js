function submitForm() {
    const form = document.getElementById('prediction-form');
    const formData = new FormData(form);

    const datanumerica = [];
    formData.forEach((value) => {
        datanumerica.push(parseFloat(value) || 0); // Convert to float, or use 0 if not a number
    });

    console.log("Datos enviados:", datanumerica);  // Para depuración

    fetch('/predict_api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(datanumerica),
    })
    .then(response => response.json())
    .then(result => {
        console.log("Respuesta recibida:", result);  // Para depuración
        if (typeof result.prediction === 'number') {
            alert('The price predicted is : $' + Math.round(result.prediction,2));
        } else {
            console.error('Error: La predicción no es un número');
            alert('An error occurred. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });
}
