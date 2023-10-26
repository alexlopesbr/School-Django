document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();
    const selectedRole = document.querySelector('#roleSelect').value;

    window.location.href = `/staff/user-list?role=${selectedRole}`;
});
