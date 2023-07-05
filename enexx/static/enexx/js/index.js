const btnCart =document.querySelector('.container-cart-icon')
        const containerCartProducts = document.querySelector('.container-cart-products')
  btnCart.addEventListener('click',()=> {
          containerCartProducts.classList.toggle('hidden-cart')    
  })

  /************************************************************ */

  const cartInfo = document.querySelector('.cart-product')
  const rowProduct = document.querySelector('.row-product')

  //Lista de los contenedores de productos
  const productsList = document.querySelector('.contenedorJuegos')

  //Variable de arreglo de productos
  let allProducts = []
  const valorTotal = document.querySelector('.total-pagar')
  const countProducts = document.querySelector('#contador-productos')



window.onload = traerlocalstorage();
window.onload = showHTML();

function traerlocalstorage(){
  const guardarCarrito = localStorage.getItem('allProducts');
    if (guardarCarrito){
      allProducts = JSON.parse(guardarCarrito);

    }
}
function guardarElCarritoEnLocalstorage(){
  localStorage.setItem('allProducts', JSON.stringify(allProducts));
}
document.addEventListener('DOMContentLoaded', function() {
  if (productsList){
    productsList.addEventListener('click', e => {
        if (e.target.classList.contains('btn-add-cart')) {
          const product = e.target.parentElement;
          const infoProduct = {
            quantity: 1,
            title: product.querySelector('h5').textContent,
            price: product.querySelector('p').textContent
          };
          const exists = allProducts.some(product => product.title === infoProduct.title);
          if (exists) {
            const products = allProducts.map(product => {
              if (product.title === infoProduct.title) {
                product.quantity++;
                return product
              }else{
              return product
              }
            });
            allProducts = [...products]
          } else {
            allProducts = [...allProducts, infoProduct];
          }
          
          showHTML();
          
          guardarElCarritoEnLocalstorage();
        }
      });
  }
});

rowProduct.addEventListener('click',  e => {

        if(e.target.classList.contains('icon-close')){
          
                const product = e.target.parentElement
                const title = product.querySelector('p').textContent
                const itemIndex = allProducts.findIndex(item => item.title === title);
                if (itemIndex !== -1) {                
                    if (allProducts[itemIndex].quantity > 1) {
                        allProducts[itemIndex].quantity--;
                    } else {
                      allProducts.splice(itemIndex, 1);
                    }

                    
                    localStorage.setItem('allProducts', JSON.stringify(allProducts)); // Guarda el estado del carrito en localStorage
                    
                }
                
        }
        
        showHTML()
})
      

// funcion para mostrar HTML
function showHTML()  {

        if(!allProducts,length){
                containerCartProducts.innerHTML=`
                <p class= "cart-empty">El carrito Esta Vacio</p>
                `
        }

        //limpiar html
        rowProduct.innerHTML ='';

        let total =0;
        let totalOfProducts =0;
        

        
        allProducts.forEach(product =>{
                const containerProduct = document.createElement('div')
                containerProduct.classList.add('cart-product')
                        containerProduct.innerHTML = `
                        <div class ="info-cart-product">
                        <span class="cantidad-producto-carrito">${product.quantity}</span>
                        <p class="titulo-producto-carrito">${product.title}</p>
                        <span class="precio-producto-carrito">${product.price}</span>
                      </div>
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="icon-close">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                      </svg>
                        `

                                           
                
          rowProduct.append(containerProduct);
          total = total + parseInt(product.quantity*product.price.slice(1))
          totalOfProducts = totalOfProducts + product.quantity;
          
        })

        valorTotal.innerText = `$${total}`;
        countProducts.innerText = totalOfProducts;
        
        
}


function validarFormularioRegistro() {
  // Obtener los valores de email y contraseña
  var email = document.getElementById('RegistroInputEmail').value;
  var password = document.getElementById('RegistroInputPassword1').value;
  
  var confirmarpass = document.getElementById('RegistroInputPassword2').value;
  
  // Expresión regular para verificar el formato del email
  var verificadorEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  // Expresión regular para verificar la contraseña
  var verificadorPassword = /^(?=.*[0-9!@#$%^&*])(?=.*[a-zA-Z]).{8,}$/;

  // Validar el email y la contraseña
  if (!verificadorEmail.test(email)) {
    alert('Por favor, ingresa un email válido.');
    return;
  }

  if (!verificadorPassword.test(password)) {
    alert('La contraseña debe tener al menos 8 caracteres y contener al menos un número o símbolo especial.');
    return;
  }

  if (password !== confirmarpass) {
    alert('Las contraseñas no coinciden. Por favor, ingresa las mismas contraseñas en ambos campos.');
    return;
  }

  // Si la validación es exitosa.
  alert('¡Usuario ingresado correctamente!');
  window.location.href = 'index.html';
}

$(document).ready(function(){
  //agregando clase active
  $('.container .botonValor[id="todos"]').addClass('botonActivo');

  $('.botonValor').click(function(){
    
    //variable que almacene la id seleccionada
    var cardId = $(this).attr('id');
    console.log(cardId);
    
    //agregando clase active a item seleccionado
    $('.botonValor').removeClass('botonActivo');
    $(this).addClass('botonActivo');

    //ocultando productos
    $('.card').css('transform','scale(0)');
    function ocultaProducto(){
      $('.card').hide();
    }setTimeout(ocultaProducto(),400);
    

    //mostrando productos
    function mostrarProducto(){
      $('.'+cardId+'').show();
      $('.'+cardId+'').css('transform','scale(1)');
      
    }setTimeout(mostrarProducto(),400);
    

  });

  $('.botonValor[id="todos"]').click(function(){
    function mostrarTodo(){
      $('.card').show();
      $('.card').css('transform','scale(1)');
    }setTimeout(mostrarTodo(),400);
    
  })
});


function EliminarJuego(id){
  Swal.fire({
    title: '¿Estás seguro de eliminar el juego?',
    text: "No podrás revertir esto!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#dc3545',
    cancelButtonColor: '#17a2b8',
    confirmButtonText: 'Si, eliminarlo!'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Eliminado!',
        'El juego ha sido eliminado.',
        'success'
      )
      window.location.href = 'eliminarJuego/'+id;
    }
  })
}

