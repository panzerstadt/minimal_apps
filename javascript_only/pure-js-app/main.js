/* jshint esversion: 6 */

// notes for the code

// code from https://medium.com/codingthesmartway-com-blog/pure-javascript-building-a-real-world-application-from-scratch-5213591cfcd6

/*
1. important stuff
- all input elements and the main <form> element itself get an id assigned
- the html code needed to output the list of existing issues is not included
    in the index.html


*/

document.getElementById('issueInputForm').addEventListener('submit', saveIssue);

// this function is called everytime the body has finished loading (using onload="fetchIssues()")

// fetches data from Local Storage
function fetchIssues() {

    // 1. load all issues from Local Storage
	var issues = JSON.parse(localStorage.getItem('issues'));
    var issuesList = document.getElementById('issuesList');

    // declare empty html container for output
    issuesList.innerHTML = '';
    
    for (var i = 0; i < issues.length; i++) {
        var id = issues[i].id;
        var desc = issues[i].description;
        var severity = issues[i].severity;
        var assignedTo = issues[i].assignedTo;
        var status = issues[i].status;

		// 2. generate the html output for the issues list
		// 	  and attach the output to the DOM
        // concat this stuff in!
        issuesList.innerHTML += `
        <div class="well">
            <h6>Issues ID: ${ id }</h6>
            <p><span class="label label-info">${ status }</span></p>
            <h3>${ desc }</h3>
			<p>
				<span class="glyphicon glyphicon-time"></span> ${ severity } 
				<span class="glyphicon glyphicon-user"></span> ${ assignedTo }
			</p>
			<a href="#" class="btn btn-warning" onclick="setStatusClosed('${ id }')">Close</a>
			<a href="#" class="btn btn-danger" onclick="deleteIssue('${ id }')">Delete</a>
		</div>
        `;
	}
}

// Saves data to Local Storage
function saveIssue(e) {
	var issueId = chance.guid();
	var issueDesc = document.getElementById('issueDescInput').value;
	var issueSeverity = document.getElementById('issueSeverityInput').value;
	var issueAssignedTo = document.getElementById('issueAssignedToInput').value;
	var issueStatus = 'Open';

	var issue = {
		id: issueId,
		description: issueDesc,
		severity: issueSeverity,
		assignedTo: issueAssignedTo,
		status: issueStatus
	};

	if (localStorage.getItem('issues') == null) {
		// make new list, push and save
		var issues = [];
		issues.push(issue);
		localStorage.setItem('issues', JSON.stringify(issues));
	} else {
		// remake list, push and save
		var issues = JSON.parse(localStorage.getItem('issues'));
		issues.push(issue);
		localStorage.setItem('issues', JSON.stringify(issues));
	}

	// clear input form
	document.getElementById('issueInputForm').reset();

	// regenerate output list
	fetchIssues();

	// prevents the default submission from taking place
	e.preventDefault();

}

function setStatusClosed(id) {
	var issues = JSON.parse(localStorage.getItem('issues'));

	// set status from issue to closed
	for(var i = 0; i < issues.length; i++) {
		// double equals cause they're strings and/or numbers?
		if (issues[i].id == id) {
			issues[i].status = "Closed";
		}
	}

	// save the updated issues list
	localStorage.setItem('issues', JSON.stringify(issues));

	// regenerate output list
	fetchIssues();
}

function deleteIssue(id) {
	var issues = JSON.parse(localStorage.getItem('issues'));

	// delete index, like python's remove()
	//'a string'.splice(index, deleteCount)
	for(var i=0; i < issues.length; i++) {
		if (issues[i].id == id) {
			issues.splice(i, 1);  // the f is this
		}
	}

	// save the updated issues list
	localStorage.setItem('issues', JSON.stringify(issues));

	// regenerate output list
	fetchIssues();
}