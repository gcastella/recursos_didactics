DESC_CLASS = "recurs_desc_row"
//SPAN_DESC = "3"
//MY_DESC = " > Descripció super detallada i llarga del recurs que s'ha clicat, que quedarà desplegada aquí fins que no es torni a clicar el recurs per tancar-la..."

show_recurs = function(pare_tr){
//    desc_row = pare_tr.parentNode.insertRow(pare_tr.rowIndex)
//    desc_row.className = DESC_CLASS
//    desc_cell = desc_row.insertCell()
//    desc_cell.colSpan = SPAN_DESC
//    desc_cell.innerText = MY_DESC
    next_row = pare_tr.parentNode.rows[pare_tr.rowIndex]
    next_row.style.display = 'table-row'
}

hide_recurs = function(pare_tr){
    next_row = pare_tr.parentNode.rows[pare_tr.rowIndex]
    next_row.style.display = 'none'
//    next_row.remove()
}

document.addEventListener("click", function(e){
    pare = e.target.parentNode
    if(pare.tagName === "TR"){
        next_row = pare.parentNode.rows[pare.rowIndex]
        // Afegeix 'descripcio' si no esta desplegat i no te classe 'descripcio'.
        if((pare.className != DESC_CLASS && next_row === undefined) || (pare.className != DESC_CLASS && next_row.style.display === 'none')){
            show_recurs(pare_tr=pare)
        } else if(next_row.className === DESC_CLASS){
            hide_recurs(pare_tr=pare)
        }
    }
})