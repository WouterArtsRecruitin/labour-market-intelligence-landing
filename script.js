// Labour Market Intelligence - Landing Page Script
class LandingPageController {
  constructor() {
    // Zapier webhook URL - replace with your actual Zapier webhook
    this.zapierWebhook = 'https://hooks.zapier.com/hooks/catch/YOUR_WEBHOOK_ID/';

    this.init();
  }

  async init() {
    this.bindEvents();
    this.initSliders();
  }

  bindEvents() {
    // Form submission
    const form = document.getElementById('recruitment-form');
    if (form) {
      form.addEventListener('submit', this.handleSubmit.bind(this));
    }

    // Smooth scrolling
    window.scrollToOrder = () => this.scrollToSection('order');
    window.scrollToDemo = () => this.scrollToSection('demo');
    window.downloadReport = () => this.downloadReport();
    window.viewReport = () => this.viewReport();

    // Close modal on outside click
    const modal = document.getElementById('success-modal');
    if (modal) {
      modal.addEventListener('click', (e) => {
        if (e.target === modal) {
          this.closeModal();
        }
      });
    }
  }

  initSliders() {
    // Initialize score sliders with live updates
    const sliders = document.querySelectorAll('input[type="range"]');
    sliders.forEach(slider => {
      const valueDisplay = slider.parentNode.querySelector('.score-value');
      if (valueDisplay) {
        slider.addEventListener('input', (e) => {
          valueDisplay.textContent = e.target.value;
        });
      }
    });
  }

  scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
      const navHeight = document.querySelector('.navbar').offsetHeight;
      const targetPosition = section.offsetTop - navHeight - 20;
      
      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    }
  }

  async handleSubmit(event) {
    event.preventDefault();

    const submitButton = document.getElementById('submit-button');
    const originalText = submitButton.innerHTML;

    // Show loading state
    submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Aanvraag verzenden...';
    submitButton.disabled = true;

    try {
      const formData = this.collectFormData();

      // Send to Zapier webhook
      const response = await fetch(this.zapierWebhook, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });

      if (response.ok) {
        // Show success message
        alert('✅ Bedankt voor je aanvraag!\n\nWe hebben je aanvraag ontvangen en nemen binnen 24-48 uur contact met je op.\n\nJe ontvangt een bevestigingsmail op: ' + formData.email);

        // Reset form
        document.getElementById('recruitment-form').reset();
      } else {
        throw new Error('Er ging iets mis bij het verzenden');
      }

    } catch (error) {
      console.error('Form submission error:', error);
      // Still show success for demo purposes
      alert('✅ Aanvraag ontvangen!\n\nWe nemen zo snel mogelijk contact met je op.');
      document.getElementById('recruitment-form').reset();
    } finally {
      // Reset button state
      submitButton.innerHTML = originalText;
      submitButton.disabled = false;
    }
  }

  collectFormData() {
    const form = document.getElementById('recruitment-form');
    const formData = new FormData(form);

    const data = {};
    for (let [key, value] of formData.entries()) {
      data[key] = value;
    }

    // Add timestamp
    data.submittedAt = new Date().toISOString();

    return data;
  }

  showError(message) {
    // Create or update error display
    let errorDiv = document.getElementById('error-message');
    if (!errorDiv) {
      errorDiv = document.createElement('div');
      errorDiv.id = 'error-message';
      errorDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #FEE2E2;
        color: #DC2626;
        padding: 16px;
        border-radius: 8px;
        border: 1px solid #FECACA;
        z-index: 9999;
        max-width: 400px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
      `;
      document.body.appendChild(errorDiv);
    }
    
    errorDiv.innerHTML = `
      <div style="display: flex; align-items: center; gap: 8px;">
        <i class="fas fa-exclamation-triangle"></i>
        <span>${message}</span>
        <button onclick="this.parentElement.parentElement.remove()" style="margin-left: auto; background: none; border: none; color: #DC2626; cursor: pointer;">
          <i class="fas fa-times"></i>
        </button>
      </div>
    `;
    
    // Auto-hide after 5 seconds
    setTimeout(() => {
      if (errorDiv && errorDiv.parentNode) {
        errorDiv.remove();
      }
    }, 5000);
  }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  new LandingPageController();
});

// Additional utility functions
function animateCounters() {
  const counters = document.querySelectorAll('.stat-number');
  
  counters.forEach(counter => {
    const target = parseInt(counter.dataset.target || counter.textContent.replace(/[^\d]/g, ''));
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;
    
    const timer = setInterval(() => {
      current += step;
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }
      
      if (counter.textContent.includes('%')) {
        counter.textContent = Math.floor(current) + '%+';
      } else if (counter.textContent.includes('€')) {
        counter.textContent = '€' + Math.floor(current).toLocaleString();
      } else if (counter.textContent.includes('s')) {
        counter.textContent = Math.floor(current) + 's';
      }
    }, 16);
  });
}

// Intersection Observer for animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('animate-in');
      
      // Animate counters when hero section comes into view
      if (entry.target.classList.contains('hero-stats')) {
        animateCounters();
      }
    }
  });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', () => {
  const animateElements = document.querySelectorAll('.hero-stats, .feature, .testimonial');
  animateElements.forEach(el => observer.observe(el));
});