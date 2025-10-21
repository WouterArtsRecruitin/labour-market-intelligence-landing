import express from 'express';
import claudeService from '../services/claude.service.js';
import emailService from '../services/email.service.js';
import logger from '../utils/logger.js';

const router = express.Router();

/**
 * POST /api/generate-report
 * Generate a labour market intelligence report using Claude AI
 */
router.post('/generate-report', async (req, res) => {
  try {
    const analysisData = req.body;

    logger.info('Received report generation request', {
      company: analysisData.company,
      position: analysisData.position,
      email: analysisData.email,
      ip: req.ip
    });

    // Validate request data
    const validation = claudeService.validateAnalysisData(analysisData);
    if (!validation.valid) {
      logger.warn('Invalid analysis data', { errors: validation.errors });
      return res.status(400).json({
        success: false,
        error: 'Invalid request data',
        details: validation.errors
      });
    }

    // Validate email
    if (!analysisData.email || !isValidEmail(analysisData.email)) {
      return res.status(400).json({
        success: false,
        error: 'Valid email address is required'
      });
    }

    // Determine analysis mode (quick vs comprehensive)
    // For demo purposes, we'll use comprehensive mode
    const quickMode = false;

    // Generate report using Claude AI
    const reportResult = await claudeService.generateMarketReport(analysisData, quickMode);

    if (!reportResult.success) {
      throw new Error('Report generation failed');
    }

    // Send report via email (async, don't wait)
    emailService.sendMarketReport(analysisData.email, {
      report: reportResult.report,
      metadata: reportResult.metadata,
      analysisData
    }).catch(error => {
      logger.error('Email delivery failed (async)', {
        error: error.message,
        email: analysisData.email
      });
    });

    // Return success response immediately
    res.json({
      success: true,
      message: 'Rapport succesvol gegenereerd en verzonden naar uw email',
      report: reportResult.report,
      metadata: {
        generatedAt: reportResult.metadata.generatedAt,
        generationTime: reportResult.metadata.generationTime,
        emailSentTo: analysisData.email,
        reportId: generateReportId()
      }
    });

    logger.info('Report generated successfully', {
      company: analysisData.company,
      position: analysisData.position,
      generationTime: reportResult.metadata.generationTime
    });

  } catch (error) {
    logger.error('Error in generate-report endpoint', {
      error: error.message,
      stack: error.stack
    });

    res.status(500).json({
      success: false,
      error: 'Failed to generate report',
      message: error.message
    });
  }
});

/**
 * GET /api/health
 * Health check endpoint
 */
router.get('/health', async (req, res) => {
  try {
    const claudeHealth = await claudeService.getHealthStatus();
    const emailHealth = await emailService.testConnection();

    const overallHealthy = claudeHealth.status === 'healthy' && emailHealth;

    res.json({
      status: overallHealthy ? 'healthy' : 'degraded',
      timestamp: new Date().toISOString(),
      services: {
        claude: claudeHealth,
        email: {
          status: emailHealth ? 'healthy' : 'unhealthy',
          configured: !!process.env.EMAIL_USER
        }
      },
      version: '1.0.0'
    });
  } catch (error) {
    res.status(500).json({
      status: 'unhealthy',
      error: error.message,
      timestamp: new Date().toISOString()
    });
  }
});

/**
 * GET /api/status
 * Simple status check (no external dependencies)
 */
router.get('/status', (req, res) => {
  res.json({
    status: 'ok',
    message: 'Labour Market Intelligence API is running',
    timestamp: new Date().toISOString()
  });
});

// Helper functions

/**
 * Validate email address format
 * @param {string} email - Email to validate
 * @returns {boolean} - Valid or not
 */
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Generate unique report ID
 * @returns {string} - Report ID
 */
function generateReportId() {
  return `RPT-${Date.now()}-${Math.random().toString(36).substr(2, 9).toUpperCase()}`;
}

export default router;
