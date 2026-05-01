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

/* confirmação de exclusão na tabela */
function pedirConfirmacao(id) {
    // Esconde os ícones normais da linha específica
    document.getElementById('acoes-normais-' + id).style.display = 'none';
    // Mostra os botões de Sim/Não da linha específica
    document.getElementById('confirmacao-' + id).style.display = 'flex';
}

function cancelarExclusao(id) {
    // Esconde os botões de Sim/Não
    document.getElementById('confirmacao-' + id).style.display = 'none';
    // Mostra os ícones normais novamente
    document.getElementById('acoes-normais-' + id).style.display = 'flex';
}