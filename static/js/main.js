function loadMMR() {
    d3.json("/api/cdc-mmr").then(data => {
        var listGroup = d3.select('#mmr');
        listGroup.html("");
        data.forEach(mmr => {
            var listItem = listGroup.append("li");
            listItem.text(mmr.State);
            listItem.attr("class", "list-group-item");

            var button = listItem.append("button");
            button.attr("class", "btn btn-danger");
            button.style("float", "right");
            button.text("delete");
            button.on("click", function() {
                deleteState(mmr);
            });
        });
    });
}

loadMMR();

function addState(event) {
    event.preventDefault();
        var input = d3.select("#stateControl")
        var value = input.property("value");

        var data = {
          State: value,  
        };

        d3.json('/api/cdc-mmr', {
            method: 'POST', 
            body: JSON.stringify(data),
        }).then(() => {
            loadMMR();
            input.property("value", "");
        });
        
}

function deleteState(MMR) {
    d3.json(`/api/cdc-mmr/${MMR.id}`, {
        method: 'DELETE'
    }).then(() => {
        loadMMR();
    });
}

d3.select("#stateForm").on("submit", addState);