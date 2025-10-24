// Labour Market Intelligence - Landing Page Script
class LandingPageController {
  constructor() {
    this.selectedPlan = 'single';
    // Use production API URL or fallback to current ngrok
    this.apiUrl = window.location.hostname === 'localhost'
      ? 'http://localhost:3002'
      : 'https://del-untreadable-nonspeciously.ngrok-free.dev';

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

  // Pricing section removed - no longer needed

  async handleSubmit(event) {
    event.preventDefault();
    
    const submitButton = document.getElementById('submit-button');
    const originalText = submitButton.innerHTML;
    
    // Show loading state
    submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Verwerken...';
    submitButton.disabled = true;

    try {
      const formData = this.collectFormData();

      // Validate form data
      if (!this.validateFormData(formData)) {
        throw new Error('Please fill in all required fields');
      }

      // Generate report
      const reportResult = await this.generateReport(formData);

      if (reportResult.success) {
        this.showSuccessModal(reportResult);
      } else {
        throw new Error('Report generation failed');
      }

    } catch (error) {
      console.error('Form submission error:', error);
      this.showError(error.message || 'Er is een fout opgetreden. Probeer opnieuw.');
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
    
    // Add selected plan
    data.selectedPlan = this.selectedPlan;
    
    return data;
  }

  validateFormData(data) {
    const required = ['company', 'position', 'candidateName', 'candidateEmail', 'experience', 'skills'];
    
    for (let field of required) {
      if (!data[field] || data[field].trim() === '') {
        this.showError(`Veld '${field}' is verplicht`);
        return false;
      }
    }
    
    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(data.candidateEmail)) {
      this.showError('Voer een geldig email adres in');
      return false;
    }
    
    return true;
  }

  async generateReport(formData) {
    try {
      // Transform form data to API format
      const apiData = {
        company: formData.company,
        position: formData.position,
        candidate: {
          name: formData.candidateName,
          email: formData.candidateEmail,
          experience: formData.experience,
          skills: formData.skills.split(',').map(s => s.trim()),
          education: formData.education,
          location: formData.location || 'Nederland'
        },
        scores: {
          technical: parseInt(formData.technicalScore) || 7,
          communication: parseInt(formData.communicationScore) || 8,
          teamwork: parseInt(formData.teamworkScore) || 7,
          leadership: parseInt(formData.leadershipScore) || 6
        }
      };

      const response = await fetch(`${this.apiUrl}/demo-report`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(apiData)
      });

      if (!response.ok) {
        throw new Error('API request failed');
      }

      const result = await response.json();
      
      return {
        success: result.success,
        report: result.report,
        reportUrl: `data:text/html;charset=utf-8,${encodeURIComponent(this.formatReportAsHTML(result.report))}`,
        pdfUrl: this.generatePDFDataUrl(result.report, formData)
      };
      
    } catch (error) {
      console.error('Report generation error:', error);
      return { success: false, error: error.message };
    }
  }

  formatReportAsHTML(markdownReport) {
    // Simple markdown to HTML conversion for demo
    let html = markdownReport
      .replace(/# (.*)/g, '<h1>$1</h1>')
      .replace(/## (.*)/g, '<h2>$1</h2>')
      .replace(/### (.*)/g, '<h3>$1</h3>')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/- (.*)/g, '<li>$1</li>')
      .replace(/(\n\n)/g, '</p><p>')
      .replace(/\n/g, '<br>');
    
    return `
      <!DOCTYPE html>
      <html>
      <head>
        <title>Labour Market Intelligence Report</title>
        <style>
          body { font-family: Inter, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }
          h1, h2, h3 { color: #FF6B35; }
          .header { border-bottom: 3px solid #10B981; padding-bottom: 20px; margin-bottom: 30px; }
          .section { margin-bottom: 30px; }
          li { margin-bottom: 5px; }
        </style>
      </head>
      <body>
        <div class="header">
          <h1>🎯 RECRUITMENT ASSESSMENT REPORT</h1>
          <p><strong>Gegenereerd door Labour Market Intelligence Platform</strong></p>
        </div>
        <div class="content">
          ${html}
        </div>
      </body>
      </html>
    `;
  }

  generatePDFDataUrl(report, formData) {
    // In a real implementation, you'd generate a proper PDF
    // For demo purposes, return a data URL that downloads the HTML
    const htmlContent = this.formatReportAsHTML(report);
    const fileName = `rapport_${formData.candidateName.replace(/\s+/g, '_')}_${Date.now()}.html`;
    
    return `data:text/html;charset=utf-8,${encodeURIComponent(htmlContent)}`;
  }

  calculateTotal(plan) {
    const prices = {
      single: 59.00,
      monthly: 199.00,
      enterprise: 999.00
    };
    
    const basePrice = prices[plan] || 59.00;
    const vat = basePrice * 0.21;
    return basePrice + vat;
  }

  showSuccessModal(reportResult) {
    const modal = document.getElementById('success-modal');
    if (modal) {
      modal.style.display = 'block';
      modal.classList.add('success-animation');
      
      // Store report data for download/view actions
      this.lastReport = reportResult;
    }
  }

  closeModal() {
    const modal = document.getElementById('success-modal');
    if (modal) {
      modal.style.display = 'none';
      modal.classList.remove('success-animation');
    }
  }

  downloadReport() {
    if (this.lastReport && this.lastReport.pdfUrl) {
      const link = document.createElement('a');
      link.href = this.lastReport.pdfUrl;
      link.download = `recruitment_rapport_${Date.now()}.html`;
      link.click();
    }
  }

  viewReport() {
    if (this.lastReport && this.lastReport.reportUrl) {
      window.open(this.lastReport.reportUrl, '_blank');
    }
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