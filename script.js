// Labour Market Intelligence - Landing Page Script
class LandingPageController {
  constructor() {
    // JotForm handles Zapier webhook integration directly
    this.init();
  }

  async init() {
    this.bindEvents();
    this.initSliders();
  }

  bindEvents() {
    // JotForm handles its own submission - no custom form handling needed
    
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

  // JotForm handles submission automatically - no custom submission methods needed

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