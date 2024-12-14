const precos = {
    'Altiplano': 100,
    'Centro': 150,
    'Valentina': 20,
    'Santa Rita': 110
};

let listaCorridas = [];

function calcularPreco(bairro) {
    return precos[bairro] || 50;
}

document.getElementById('adicionarCorrida').addEventListener('click', () => {
    const destino = document.getElementById('destino').value;
    const bairro = document.getElementById('bairro').value;
    const voucher = document.getElementById('voucher').value;
    
    if (!destino && !bairro && !voucher) {
        alert('Por favor, preencha pelo menos um campo!');
        return;
    }

    const preco = calcularPreco(bairro);
    const corrida = {
        "Voucher": voucher || "Não Informado",
        "Bairro": bairro || "Não Informado",
        "Preço (R$)": preco,
        "Destino": destino || "Não Informado"
    };
    
    listaCorridas.push(corrida);

    const tbody = document.querySelector('#tabelaCorridas tbody');
    const tr = document.createElement('tr');
    tr.innerHTML = `
        <td>${corrida.Voucher}</td>
        <td>${corrida.Bairro}</td>
        <td>${corrida["Preço (R$)"]}</td>
        <td>${corrida.Destino}</td>
    `;
    tbody.appendChild(tr);
    
    // Limpar os campos após adicionar a corrida
    document.getElementById('destino').value = '';
    document.getElementById('bairro').value = '';
    document.getElementById('voucher').value = '';
});

document.getElementById('finalizar').addEventListener('click', () => {
    if (listaCorridas.length === 0) {
        alert('Nenhuma corrida registrada!');
        return;
    }

    document.getElementById('downloadButton').style.display = 'inline-block';
});

document.getElementById('downloadButton').addEventListener('click', () => {
    const ws_data = [
        ["Voucher", "Bairro", "Preço (R$)", "Destino"], // Cabeçalho em negrito
        ...listaCorridas.map(corrida => [corrida.Voucher, corrida.Bairro, corrida["Preço (R$)"], corrida.Destino])
    ];

    const ws = XLSX.utils.aoa_to_sheet(ws_data);

    // Estilos
    const headerStyle = {
        font: { bold: true },
        alignment: { horizontal: "center" }
    };

    for (let col = 0; col < 4; col++) {
        const cell = ws[XLSX.utils.encode_cell({ r: 0, c: col })];
        if (cell) {
            cell.s = headerStyle;
        }
    }

    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, "Corridas");

    XLSX.writeFile(wb, "planilha_corridas.xlsx");
});
