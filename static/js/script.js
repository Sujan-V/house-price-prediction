let chart;

async function predictPrice() {

    const data = {
        bedrooms: document.getElementById("bedrooms").value,
        bathrooms: document.getElementById("bathrooms").value,
        living_area: document.getElementById("living_area").value,
        floors: document.getElementById("floors").value,
        condition: document.getElementById("condition").value,
        grade: document.getElementById("grade").value,
        built_year: document.getElementById("built_year").value,
        zipcode: document.getElementById("zipcode").value,
        lat: document.getElementById("lat").value,
        long: document.getElementById("long").value,
        schools: document.getElementById("schools").value,
        airport: document.getElementById("airport").value
    };

    const response = await fetch("/predict", {
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(data)
    });

    const result = await response.json();

    const price = result.price;

    document.getElementById("price").innerHTML =
        `₹ ${price.toLocaleString()}`;

    let insight = "";

    if(price > 20000000){
        insight = "Luxury premium property with excellent valuation.";
    }
    else if(price > 10000000){
        insight = "High-value property in a strong location.";
    }
    else{
        insight = "Affordable property with growth potential.";
    }

    document.getElementById("insight").innerHTML = insight;

    renderChart(price);
}

function renderChart(price){

    const ctx = document.getElementById("priceChart");

    if(chart){
        chart.destroy();
    }

    chart = new Chart(ctx, {

        type:'bar',

        data:{
            labels:['Predicted Price'],
            datasets:[{
                label:'Price',
                data:[price]
            }]
        }
    });
}