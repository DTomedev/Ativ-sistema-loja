function mostrarFormulario() {
    const blocoBotao = document.getElementById('bloco-botao');
    const blocoFormulario = document.getElementById('bloco-formulario');
    
    if (blocoBotao && blocoFormulario) {
        blocoBotao.style.display = 'none';
        blocoFormulario.style.display = 'block';
    }
}

function esconderFormulario() {
    const blocoBotao = document.getElementById('bloco-botao');
    const blocoFormulario = document.getElementById('bloco-formulario');
    
    if (blocoBotao && blocoFormulario) {
        blocoFormulario.style.display = 'none';
        blocoBotao.style.display = 'block';
    }
}