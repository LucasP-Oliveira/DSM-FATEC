$(document).ready(function() {
    // Função para buscar dados da API quando o botão for clicado
    $("#btnPesquisar").click(function() {
        // Obter os valores dos campos
        const pesquisa = $("#txtPesquisa").val();
        const recurso = $("#selRecurso").val();
        
        // Mostrar mensagem de carregamento
        $("#resultadoAPI").html(`
            <div class="alert alert-info" role="alert">
                <i class="bi bi-hourglass-split"></i> Buscando dados...
            </div>
        `);
        
        // Construir a URL da API
        let url = `https://jsonplaceholder.typicode.com/${recurso}`;
        
        // Se houver um ID específico na pesquisa e for um número
        if (pesquisa && !isNaN(pesquisa)) {
            url += `/${pesquisa}`;
        }
        
        // Fazer a requisição à API
        $.ajax({
            url: url,
            method: "GET",
            dataType: "json",
            success: function(data) {
                // Verificar se a API retornou dados
                if (!data || (Array.isArray(data) && data.length === 0)) {
                    $("#resultadoAPI").html(`
                        <div class="alert alert-warning" role="alert">
                            <i class="bi bi-exclamation-triangle"></i> Nenhum resultado encontrado.
                        </div>
                    `);
                    return;
                }
                
                // Converter para array se for um objeto único
                const items = Array.isArray(data) ? data : [data];
                
                // Limitar a quantidade de resultados para não sobrecarregar a página
                const limitedItems = items.slice(0, 10);
                
                // Iniciar o HTML dos resultados
                let resultadoHTML = `
                    <h4 class="mt-3 mb-4">Resultados da Pesquisa (${limitedItems.length} de ${items.length})</h4>
                    <div class="row">
                `;
                
                // Gerar cards para cada item
                limitedItems.forEach(item => {
                    // Determinar o conteúdo do card com base no tipo de recurso
                    let cardTitle = '';
                    let cardBody = '';
                    
                    switch(recurso) {
                        case 'posts':
                            cardTitle = item.title || 'Post';
                            cardBody = item.body || 'Sem conteúdo';
                            break;
                        case 'comments':
                            cardTitle = item.name || 'Comentário';
                            cardBody = item.body || 'Sem conteúdo';
                            break;
                        case 'albums':
                            cardTitle = item.title || 'Álbum';
                            cardBody = `ID do usuário: ${item.userId || 'N/A'}`;
                            break;
                        case 'photos':
                            cardTitle = item.title || 'Foto';
                            cardBody = `<img src="${item.thumbnailUrl}" alt="Thumbnail" class="img-fluid mb-2">`;
                            break;
                        case 'todos':
                            cardTitle = item.title || 'Tarefa';
                            cardBody = `Status: ${item.completed ? 'Concluída' : 'Pendente'}`;
                            break;
                        case 'users':
                            cardTitle = item.name || 'Usuário';
                            cardBody = `
                                <strong>Username:</strong> ${item.username || 'N/A'}<br>
                                <strong>Email:</strong> ${item.email || 'N/A'}<br>
                                <strong>Telefone:</strong> ${item.phone || 'N/A'}<br>
                                <strong>Website:</strong> ${item.website || 'N/A'}
                            `;
                            break;
                        default:
                            cardTitle = 'Item';
                            cardBody = 'Sem detalhes disponíveis';
                    }
                    
                    // Adicionar o card ao HTML
                    resultadoHTML += `
                        <div class="col-md-6 col-lg-4 mb-4">
                            <div class="card h-100">
                                <div class="card-header bg-primary text-white">
                                    <h5 class="card-title mb-0">${cardTitle}</h5>
                                </div>
                                <div class="card-body">
                                    <p class="card-text">${cardBody}</p>
                                </div>
                                <div class="card-footer">
                                    <small class="text-muted">ID: ${item.id}</small>
                                </div>
                            </div>
                        </div>
                    `;
                });
                
                // Fechar a div de linha
                resultadoHTML += '</div>';
                
                // Se houver mais resultados do que o limite, mostrar mensagem
                if (items.length > limitedItems.length) {
                    resultadoHTML += `
                        <div class="alert alert-info mt-3" role="alert">
                            <i class="bi bi-info-circle"></i> Mostrando os primeiros ${limitedItems.length} resultados de ${items.length}.
                        </div>
                    `;
                }
                
                // Exibir os resultados
                $("#resultadoAPI").html(resultadoHTML);
            },
            error: function(xhr, status, error) {
                // Em caso de erro na requisição
                $("#resultadoAPI").html(`
                    <div class="alert alert-danger" role="alert">
                        <i class="bi bi-exclamation-triangle"></i> Erro ao consultar a API: ${error}
                    </div>
                `);
            }
        });
    });
    
    // Adicionar evento para permitir busca ao pressionar Enter no campo de pesquisa
    $("#txtPesquisa").keypress(function(e) {
        if (e.which === 13) { // Código da tecla Enter
            $("#btnPesquisar").click();
        }
    });
});
