
//Envio de archivos CSV
function enviarArchivo(endpoint, archivo) {
    const formData = new FormData();
    formData.append('archivo', archivo);

    return fetch(endpoint, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al cargar los datos');
        }
        return response.json();
    })
    .then(data => {
		alert('Datos cargados con exito');
        console.log('Datos cargados con éxito:', data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

//Evento primer boton
document.getElementById('enviar1S').addEventListener('click', () => {
    const archivo = document.getElementById('primerSemestre').files[0];
    enviarArchivo('http://localhost:5000'+ '/api/data/cargar1S', archivo);
});

//Evento segundo boton
document.getElementById('enviar2S').addEventListener('click', () => {
    const archivo = document.getElementById('segundoSemestre').files[0];
    enviarArchivo('http://localhost:5000'+ '/api/data/cargar2S', archivo);
});

//Evento tercer boton
document.getElementById('enviar3S').addEventListener('click', () => {
    const archivo = document.getElementById('tercerSemestre').files[0];
    enviarArchivo('http://localhost:5000'+ '/api/data/cargar3S', archivo);
});



//Consulta de cursos aprobados
document.addEventListener('DOMContentLoaded', () => {
  const fetchDataButton = document.getElementById('aprobados');
  fetchDataButton.addEventListener('click', fetchData);
});

async function fetchData() {
  try {
    const response = await fetch('http://localhost:5000/api/data/consulta1');
    const data = await response.json();
    llenarCursosHTML(data);
  } catch (error) {
    console.error('Error:', error);
  }
}


function llenarCursosHTML(data) {
    var etiquetas = "\n\t\t<div class=\"container\">\n\t\t<div class=\"row\">\n\t\t\t";
 	data.forEach(item => {
            etiquetas += `<div class="col-lg-4 col-md-6 icon-box" data-aos="fade-up">
                            <div class="icon"><i class="bi bi-briefcase"></i></div>
                            <h4 class="title"><a href=""> Codigo: ${item.codigo}</a></h4>
                            <h6><a href=""><b>${item.Nombre}</b></a></h6>
                            <p class="description">Créditos: ${item.Creditos}</p>
                            <h6><b>Estado: ${item.Estado}</b></h6>
                          </div>`
	});
        etiquetas += `</div>
                     </div>`;
        document.getElementById("cursosHTML").innerHTML = etiquetas;
    }

//ver info de un curso
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('viewInfo');
  form.addEventListener('submit', handleSubmit);
});

async function handleSubmit(event) {
  event.preventDefault(); //Evita que cuando se envie el formulario se nos vuelva a recargar la pagina

  const courseCode = document.getElementById('codigoCurso').value;

  try {
    const response = await fetch('http://localhost:5000/api/data/verInfoCurso', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ courseCode })
    });
    const data = await response.json();
	console.log(data);
    llenarInfoCurso(data);
  } catch (error) {
    console.error('Error:', error);
  }
}

function llenarInfoCurso(data) {
    var etiquetas = "\n\t\t<div class=\"container\">\n\t\t<div class=\"row\">\n\t\t\t";
 	data.forEach(item => {
            etiquetas += `<div class="col-lg-4 col-md-6 icon-box" data-aos="fade-up">
                            <div class="icon"><i class="bi bi-briefcase"></i></div>
                            <h4 class="title"><a href=""> Codigo: ${item.codigo}</a></h4>
                            <h6 class="title"><a href=""><b>${item.Nombre}</b></a></h6>
                            <p class="description">Créditos: ${item.Creditos}</p>
                            <h6><b>Estado: ${item.Estado}</b></h6>
                          </div>`
	});
        etiquetas += `</div>
                     </div>`;
        document.getElementById("infoC").innerHTML = etiquetas;
    }
    
//TOp 5 cursos con mas crditos

//Consulta de cursos aprobados
document.addEventListener('DOMContentLoaded', () => {
  const fetchDataButton = document.getElementById('top5'); //Id del boton = top5
  fetchDataButton.addEventListener('click', fetchData1);
});

async function fetchData1() {
  try {
    const response = await fetch('http://localhost:5000/api/data/consulta2');
    const data = await response.json();
    llenarTopCursos(data);
  } catch (error) {
    console.error('Error:', error);
  }
}


function llenarTopCursos(data) {
    var etiquetas = "\n\t\t<div class=\"container\">\n\t\t<div class=\"row\">\n\t\t\t";
 	data.forEach(item => {
            etiquetas += `<div class="col-lg-4 col-md-6 icon-box" data-aos="fade-up">
                            <div class="icon"><i class="bi bi-briefcase"></i></div>
                            <h6><a href=""><b>${item.Nombre}</b></a></h6>
                            <p class="description">Créditos: ${item.Creditos}</p>
                          </div>`
	});
        etiquetas += `</div>
                     </div>`;
        document.getElementById("top5Cursos").innerHTML = etiquetas;
    }
