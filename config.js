/**
 * Configuration for Labour Market Intelligence Platform
 *
 * This file contains environment-specific configuration
 */

const CONFIG = {
  // API Configuration
  api: {
    // Production API URL (Render deployment)
    // ✅ Updated with actual deployed URL
    productionUrl: 'https://labour-market-intelligence-landing.onrender.com',

    // Local development URL
    developmentUrl: 'http://localhost:3002',

    // Automatically detect environment and use appropriate URL
    get baseUrl() {
      const hostname = window.location.hostname;

      // Local development
      if (hostname === 'localhost' || hostname === '127.0.0.1') {
        return this.developmentUrl;
      }

      // Production
      return this.productionUrl;
    },

    // API endpoints
    endpoints: {
      generateReport: '/api/generate-report',
      health: '/api/health',
      status: '/api/status'
    }
  },

  // Feature flags
  features: {
    enableAnalytics: true,
    enableCookieConsent: true,
    enableEmailReports: true
  },

  // Form configuration
  form: {
    // Required fields
    requiredFields: [
      'company',
      'email',
      'position',
      'sector',
      'location',
      'experienceLevel',
      'keySkills'
    ],

    // Salary range limits
    salaryRange: {
      min: 20000,
      max: 200000
    }
  }
};

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
  module.exports = CONFIG;
}
