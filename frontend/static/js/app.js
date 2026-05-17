// Basic JavaScript for the wishlist application

// Utility functions
function showMessage(message, type = 'info') {
    const msgDiv = document.createElement('div');
    msgDiv.className = type;
    msgDiv.textContent = message;
    msgDiv.style.cssText = `
        padding: 10px;
        margin: 10px 0;
        border-radius: 4px;
        ${type === 'error' ? 'background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb;' :
          type === 'success' ? 'background: #d4edda; color: #155724; border: 1px solid #c3e6cb;' :
          'background: #d1ecf1; color: #0c5460; border: 1px solid #bee5eb;'}
    `;

    const container = document.querySelector('.container') || document.body;
    container.insertBefore(msgDiv, container.firstChild);

    setTimeout(() => msgDiv.remove(), 5000);
}

// Form validation
function validateForm(form) {
    const inputs = form.querySelectorAll('input[required]');
    for (let input of inputs) {
        if (!input.value.trim()) {
            showMessage(`${input.name} is required`, 'error');
            input.focus();
            return false;
        }
    }
    return true;
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Add form validation to all forms
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(form)) {
                e.preventDefault();
            }
        });
    });

    console.log('Wishlist app initialized');
});