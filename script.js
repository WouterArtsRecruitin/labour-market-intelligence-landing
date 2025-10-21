// Labour Market Intelligence - Landing Page Script
class LandingPageController {
  constructor() {
    this.selectedPlan = 'single';
    // API URL - will be configured for Claude AI backend
    this.apiUrl = window.location.hostname === 'localhost'
      ? 'http://localhost:3002'
      : '/api'; // Relative URL for production

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
    window.selectPlan = (plan) => this.selectPlan(plan);
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

  selectPlan(plan) {
    this.selectedPlan = plan;

    // Update UI to show selected plan
    const cards = document.querySelectorAll('.pricing-card');
    cards.forEach(card => card.classList.remove('selected'));

    // Add visual feedback
    const selectedCard = document.querySelector(`[onclick="selectPlan('${plan}')"]`).closest('.pricing-card');
    if (selectedCard) {
      selectedCard.classList.add('selected');
    }

    // Scroll to order form
    this.scrollToSection('order');
  }


  async handleSubmit(event) {
    event.preventDefault();

    const submitButton = document.getElementById('submit-button');
    const originalText = submitButton.innerHTML;

    // Show loading state
    submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Rapport wordt gegenereerd...';
    submitButton.disabled = true;

    try {
      const formData = this.collectFormData();

      // Validate form data
      if (!this.validateFormData(formData)) {
        throw new Error('Vul alle verplichte velden in');
      }

      // Generate report directly (no payment needed)
      const reportResult = await this.generateReport(formData);

      if (reportResult.success) {
        this.showSuccessModal(reportResult);
      } else {
        throw new Error(reportResult.error || 'Rapport generatie mislukt');
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
    // Required fields for market analysis
    const required = ['company', 'email', 'position', 'sector', 'location', 'experienceLevel', 'keySkills'];

    const fieldLabels = {
      company: 'Bedrijfsnaam',
      email: 'Email',
      position: 'Functietitel',
      sector: 'Sector/Industrie',
      location: 'Regio',
      experienceLevel: 'Ervaring Niveau',
      keySkills: 'Belangrijkste Vaardigheden'
    };

    for (let field of required) {
      if (!data[field] || data[field].trim() === '') {
        this.showError(`${fieldLabels[field]} is verplicht`);
        return false;
      }
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(data.email)) {
      this.showError('Voer een geldig email adres in');
      return false;
    }

    // Validate salary range if provided
    if (data.minSalary && data.maxSalary) {
      const min = parseInt(data.minSalary);
      const max = parseInt(data.maxSalary);
      if (min >= max) {
        this.showError('Maximum salaris moet hoger zijn dan minimum salaris');
        return false;
      }
    }

    return true;
  }

  async generateReport(formData) {
    try {
      // Transform form data to API format for Claude AI
      const apiData = {
        email: formData.email,
        company: formData.company,
        position: formData.position,
        sector: formData.sector,
        location: formData.location,
        experienceLevel: formData.experienceLevel,
        keySkills: formData.keySkills.split(',').map(s => s.trim()),
        salaryRange: {
          min: formData.minSalary ? parseInt(formData.minSalary) : null,
          max: formData.maxSalary ? parseInt(formData.maxSalary) : null
        },
        analysisFocus: formData.analysisFocus || '',
        priorities: {
          marketDemand: parseInt(formData.marketDemand) || 5,
          competitionAnalysis: parseInt(formData.competitionAnalysis) || 5,
          salaryBenchmarking: parseInt(formData.salaryBenchmarking) || 5,
          recruitmentStrategy: parseInt(formData.recruitmentStrategy) || 5
        },
        timestamp: new Date().toISOString()
      };

      console.log('Sending request to:', `${this.apiUrl}/generate-report`);
      console.log('Request data:', apiData);

      const response = await fetch(`${this.apiUrl}/generate-report`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(apiData)
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`API request failed: ${response.status} - ${errorText}`);
      }

      const result = await response.json();

      return {
        success: true,
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

// Cookie Consent Management
class CookieConsent {
  constructor() {
    this.cookieName = 'recruitin_cookie_consent';
    this.init();
  }

  init() {
    // Check if user has already made a choice
    const consent = this.getConsent();
    if (consent === null) {
      this.showBanner();
    }

    // Bind events
    document.getElementById('accept-cookies')?.addEventListener('click', () => this.acceptCookies());
    document.getElementById('decline-cookies')?.addEventListener('click', () => this.declineCookies());
  }

  showBanner() {
    const banner = document.getElementById('cookie-consent');
    if (banner) {
      banner.style.display = 'block';
      setTimeout(() => banner.classList.add('show'), 100);
    }
  }

  hideBanner() {
    const banner = document.getElementById('cookie-consent');
    if (banner) {
      banner.classList.remove('show');
      setTimeout(() => banner.style.display = 'none', 300);
    }
  }

  acceptCookies() {
    this.setConsent('accepted');
    this.hideBanner();
    console.log('Cookies accepted');
  }

  declineCookies() {
    this.setConsent('declined');
    this.hideBanner();
    console.log('Cookies declined');
  }

  setConsent(value) {
    const expiryDate = new Date();
    expiryDate.setFullYear(expiryDate.getFullYear() + 1); // 1 year
    document.cookie = `${this.cookieName}=${value}; expires=${expiryDate.toUTCString()}; path=/; SameSite=Strict`;
  }

  getConsent() {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      const [name, value] = cookie.trim().split('=');
      if (name === this.cookieName) {
        return value;
      }
    }
    return null;
  }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  new LandingPageController();
  new CookieConsent();
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
  const animateElements = document.querySelectorAll('.hero-stats, .feature, .testimonial, .pricing-card');
  animateElements.forEach(el => observer.observe(el));
});