
// Function to calculate the difference in hours between time_in and time_out
function calculateHours() {
    var timeIn = document.getElementById('time_in').value;
    var timeOut = document.getElementById('time_out').value;

    if (timeIn && timeOut) {
        var timeInDate = new Date('1970-01-01T' + timeIn + 'Z');
        var timeOutDate = new Date('1970-01-01T' + timeOut + 'Z');

        var diffMs = timeOutDate - timeInDate; // difference in milliseconds
        var diffHrs = diffMs / (1000 * 60 * 60); // difference in hours

        // Handle cases where time_out is earlier than time_in (e.g., night shifts)
        if (diffHrs < 0) {
            diffHrs += 24;
        }

        document.getElementById('total_hours_day').value = diffHrs.toFixed(2);

        // Assuming each day has the same hours worked
        var daysWorked = document.getElementById('days_worked').value || 1;
        document.getElementById('total_hours_month').value = (diffHrs * daysWorked).toFixed(2);
    }
}
