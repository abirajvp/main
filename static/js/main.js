function load_call_log(logs){
    const logsTableBody = $(".callLogsTableBody");
    $(logsTableBody).empty();
    logs.forEach(log => {
        logsTableBody.append(
            `<tr>
                <td>${log.from_number}</td>
                <td>${log.to_number}</td>
                <td>${log.status}</td>
            </tr>`
        );
    });
}

function get_call_log(){
    $.ajax({
        url: `/fetch-call-log`,
        type: "GET",
        success: function (response) {
            load_call_log(response.logs);
        },
        error: function (error) {
            alert("Error loading log. Error: " + error);
        }
    });
}












function load_logs(logs){
    const logsTableBody = $(".logsTableBody");
    $(logsTableBody).empty();
    logs.forEach(log => {
        logsTableBody.append(
            `<tr>
                <td>${log}</td>
            </tr>`
        );
    });
}

function fetch_log(log_section){
    $.ajax({
        url: `/fetch-logs?log-section=${log_section}`,
        type: "GET",
        success: function (response) {
            load_logs(response.logs);
        },
        error: function (error) {
            console.log("Error loading log. Error: " + error);
        }
    });
}