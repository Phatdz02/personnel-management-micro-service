document.addEventListener('DOMContentLoaded', function () {
    const createCampaignForm = document.getElementById('create-campaign-form');
    const addEmployeeForm = document.getElementById('add-employee-form');
    const campaignSelect = document.getElementById('campaign-select');
    const campaignSelectForEmployees = document.getElementById('campaign-select-for-employees');
    const campaignsList = document.getElementById('campaign-list').getElementsByTagName('tbody')[0];
    const employeesList = document.getElementById('employee-list').getElementsByTagName('tbody')[0];
    const resultsTable = document.getElementById('results-table').getElementsByTagName('tbody')[0];

    // Create Campaign
    createCampaignForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const campaignName = document.getElementById('campaign-name').value;
        const startDate = document.getElementById('start-date').value;
        const endDate = document.getElementById('end-date').value;

        fetch('http://localhost:5001/campaigns', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: campaignName,
                start_date: startDate,
                end_date: endDate
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Campaign created:', data);
            loadCampaigns();
        });
    });

    // Add Employee to Campaign
    addEmployeeForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const employeeId = document.getElementById('employee-id').value;
        const campaignId = campaignSelect.value;

        fetch('http://localhost:5002/employees', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                employee_id: employeeId,
                campaign_id: campaignId
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Employee added:', data);
            loadEmployeesInCampaign(campaignId);
        });
    });

    // Load Campaigns
    function loadCampaigns() {
        fetch('http://localhost:5001/campaigns')
            .then(response => response.json())
            .then(campaigns => {
                campaignsList.innerHTML = '';
                campaignSelect.innerHTML = '';
                campaignSelectForEmployees.innerHTML = '';

                campaigns.forEach((campaign, index) => {
                    // Add to Campaign List
                    const row = campaignsList.insertRow();
                    row.insertCell(0).textContent = index + 1;
                    row.insertCell(1).textContent = campaign.name;
                    row.insertCell(2).textContent = campaign.start_date;
                    row.insertCell(3).textContent = campaign.end_date;

                    // Add to Select Options
                    const option = document.createElement('option');
                    option.value = campaign._id;
                    option.textContent = campaign.name;
                    campaignSelect.appendChild(option);
                    campaignSelectForEmployees.appendChild(option.cloneNode(true));
                });
            });
    }

    // Load Employees in Campaign
    function loadEmployeesInCampaign(campaignId) {
        fetch(`http://localhost:5002/employees/${campaignId}`)
            .then(response => response.json())
            .then(employees => {
                employeesList.innerHTML = '';

                employees.forEach((employee, index) => {
                    const row = employeesList.insertRow();
                    row.insertCell(0).textContent = index + 1;
                    row.insertCell(1).textContent = employee.employee_id;
                });
            });
    }

    // Load Results
    function loadResults() {
        fetch('http://localhost:5003/results')
            .then(response => response.json())
            .then(results => {
                resultsTable.innerHTML = '';

                results.forEach((result, index) => {
                    fetch(`http://localhost:5001/campaigns/${result.campaign_id}`)
                        .then(response => response.json())
                        .then(campaign => {
                            const row = resultsTable.insertRow();
                            row.insertCell(0).textContent = index + 1;
                            row.insertCell(1).textContent = result.employee_id;
                            row.insertCell(2).textContent = campaign.name;
                            row.insertCell(3).textContent = campaign.start_date;
                            row.insertCell(4).textContent = campaign.end_date;
                            row.insertCell(5).textContent = result.distance || '';
                        });
                });
            });
    }

    loadCampaigns();
    loadResults();
});
