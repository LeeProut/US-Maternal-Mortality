function loadMMR() {
    d3.json("/api/cdc-mmr").then(data => {
        data.forEach(mmr => {
            var listGroup = d3.select('#mmr');
            var listItem = listGroup.append("li");
            listItem.text(mmr.State);
            listItem.attr("class", "list-group-item");
        });
    });
}

loadMMR();

