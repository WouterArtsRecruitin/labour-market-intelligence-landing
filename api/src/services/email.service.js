import nodemailer from 'nodemailer';
import logger from '../utils/logger.js';

class EmailService {
  constructor() {
    this.transporter = null;
    this.initialize();
  }

  /**
   * Initialize email transporter
   */
  initialize() {
    try {
      this.transporter = nodemailer.createTransport({
        host: process.env.EMAIL_HOST || 'smtp.gmail.com',
        port: parseInt(process.env.EMAIL_PORT) || 587,
        secure: process.env.EMAIL_SECURE === 'true',
        auth: {
          user: process.env.EMAIL_USER,
          pass: process.env.EMAIL_PASSWORD
        }
      });

      logger.info('Email service initialized', {
        host: process.env.EMAIL_HOST,
        port: process.env.EMAIL_PORT
      });
    } catch (error) {
      logger.error('Failed to initialize email service', { error: error.message });
    }
  }

  /**
   * Send market report via email
   * @param {string} recipientEmail - Recipient's email address
   * @param {Object} reportData - Report data and metadata
   * @returns {Promise<Object>} - Send result
   */
  async sendMarketReport(recipientEmail, reportData) {
    try {
      const { report, metadata, analysisData } = reportData;

      // Convert Markdown to basic HTML
      const htmlReport = this.markdownToHtml(report);

      const mailOptions = {
        from: process.env.EMAIL_FROM || '"Recruitin" <noreply@recruitin.com>',
        to: recipientEmail,
        subject: `🎯 Arbeidsmarkt Intelligence Rapport: ${analysisData.position}`,
        html: this.generateEmailTemplate(htmlReport, metadata, analysisData),
        text: this.generatePlainTextEmail(report, metadata, analysisData)
      };

      const info = await this.transporter.sendMail(mailOptions);

      logger.info('Market report email sent successfully', {
        recipient: recipientEmail,
        messageId: info.messageId,
        position: analysisData.position
      });

      return {
        success: true,
        messageId: info.messageId,
        recipient: recipientEmail
      };

    } catch (error) {
      logger.error('Failed to send market report email', {
        error: error.message,
        recipient: recipientEmail
      });

      throw new Error(`Email delivery failed: ${error.message}`);
    }
  }

  /**
   * Generate HTML email template
   * @param {string} htmlReport - HTML version of report
   * @param {Object} metadata - Report metadata
   * @param {Object} analysisData - Original analysis data
   * @returns {string} - Complete HTML email
   */
  generateEmailTemplate(htmlReport, metadata, analysisData) {
    return `
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arbeidsmarkt Intelligence Rapport</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #1F2937;
            background-color: #F9FAFB;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #FFFFFF;
        }
        .header {
            background: linear-gradient(135deg, #4B4F51 0%, #77797B 100%);
            color: white;
            padding: 40px 30px;
            text-align: center;
        }
        .header h1 {
            margin: 0 0 10px 0;
            font-size: 28px;
            font-weight: 700;
        }
        .header p {
            margin: 0;
            opacity: 0.9;
            font-size: 16px;
        }
        .meta-info {
            background-color: #FEF3C7;
            border-left: 4px solid #EF7D00;
            padding: 20px 30px;
            margin: 0;
        }
        .meta-info h3 {
            margin: 0 0 15px 0;
            color: #92400E;
            font-size: 18px;
        }
        .meta-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
            font-size: 14px;
        }
        .meta-label {
            font-weight: 600;
            color: #78350F;
        }
        .meta-value {
            color: #92400E;
        }
        .content {
            padding: 40px 30px;
        }
        .content h1 {
            color: #4B4F51;
            font-size: 26px;
            margin-top: 30px;
            margin-bottom: 15px;
            border-bottom: 3px solid #EF7D00;
            padding-bottom: 10px;
        }
        .content h2 {
            color: #4B4F51;
            font-size: 22px;
            margin-top: 25px;
            margin-bottom: 12px;
        }
        .content h3 {
            color: #1F2937;
            font-size: 18px;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .content p {
            margin-bottom: 15px;
            color: #374151;
        }
        .content ul, .content ol {
            margin-bottom: 15px;
            padding-left: 30px;
        }
        .content li {
            margin-bottom: 8px;
            color: #374151;
        }
        .content strong {
            color: #1F2937;
        }
        .footer {
            background-color: #F3F4F6;
            padding: 30px;
            text-align: center;
            border-top: 1px solid #E5E7EB;
        }
        .footer p {
            margin: 5px 0;
            color: #6B7280;
            font-size: 14px;
        }
        .footer a {
            color: #EF7D00;
            text-decoration: none;
        }
        .cta-button {
            display: inline-block;
            background-color: #EF7D00;
            color: white;
            padding: 12px 30px;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 600;
            margin: 20px 0;
        }
        .disclaimer {
            background-color: #FEE2E2;
            border-left: 4px solid #EF4444;
            padding: 15px 20px;
            margin: 20px 0;
            font-size: 13px;
            color: #991B1B;
        }
        @media only screen and (max-width: 600px) {
            .header {
                padding: 30px 20px;
            }
            .content {
                padding: 30px 20px;
            }
            .meta-row {
                flex-direction: column;
                gap: 4px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <h1>🎯 Arbeidsmarkt Intelligence Rapport</h1>
            <p>Gegenereerd door Recruitin AI-powered Platform</p>
        </div>

        <!-- Metadata -->
        <div class="meta-info">
            <h3>📊 Rapport Details</h3>
            <div class="meta-row">
                <span class="meta-label">Functie:</span>
                <span class="meta-value">${analysisData.position}</span>
            </div>
            <div class="meta-row">
                <span class="meta-label">Bedrijf:</span>
                <span class="meta-value">${analysisData.company}</span>
            </div>
            <div class="meta-row">
                <span class="meta-label">Sector:</span>
                <span class="meta-value">${analysisData.sector}</span>
            </div>
            <div class="meta-row">
                <span class="meta-label">Locatie:</span>
                <span class="meta-value">${analysisData.location}</span>
            </div>
            <div class="meta-row">
                <span class="meta-label">Gegenereerd op:</span>
                <span class="meta-value">${new Date(metadata.generatedAt).toLocaleString('nl-NL')}</span>
            </div>
            <div class="meta-row">
                <span class="meta-label">Generatie tijd:</span>
                <span class="meta-value">${metadata.generationTime}s</span>
            </div>
            <div class="meta-row">
                <span class="meta-label">AI Model:</span>
                <span class="meta-value">Claude ${metadata.model}</span>
            </div>
        </div>

        <!-- Report Content -->
        <div class="content">
            <div class="disclaimer">
                <strong>⚠️ BELANGRIJK:</strong> Dit rapport is gegenereerd door AI (Claude van Anthropic) en dient als hulpmiddel voor besluitvorming. Verifieer kritieke data altijd met actuele bronnen. Recruitin garandeert geen absolute nauwkeurigheid van alle voorspellingen en aanbevelingen.
            </div>

            ${htmlReport}

            <div style="margin-top: 40px; padding-top: 20px; border-top: 2px solid #E5E7EB; text-align: center;">
                <p style="color: #6B7280; margin-bottom: 20px;">Heeft u vragen over dit rapport?</p>
                <a href="mailto:info@recruitin.com" class="cta-button">Contact Recruitin</a>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <p><strong>Recruitin Labour Market Intelligence</strong></p>
            <p>AI-powered recruitment intelligence • 85% betrouwbaarheidsgarantie</p>
            <p style="margin-top: 15px;">
                <a href="https://recruitin.com">Website</a> |
                <a href="mailto:info@recruitin.com">Contact</a> |
                <a href="https://labour-market-intelligence.netlify.app/privacy.html">Privacy</a>
            </p>
            <p style="margin-top: 15px; font-size: 12px;">
                © ${new Date().getFullYear()} WouterArts Recruitin. Alle rechten voorbehouden.
            </p>
        </div>
    </div>
</body>
</html>
    `;
  }

  /**
   * Generate plain text email version
   * @param {string} report - Markdown report
   * @param {Object} metadata - Report metadata
   * @param {Object} analysisData - Original analysis data
   * @returns {string} - Plain text email
   */
  generatePlainTextEmail(report, metadata, analysisData) {
    return `
═══════════════════════════════════════════════════════════
🎯 ARBEIDSMARKT INTELLIGENCE RAPPORT
═══════════════════════════════════════════════════════════

RAPPORT DETAILS:
────────────────────────────────────────────────────────────
Functie:        ${analysisData.position}
Bedrijf:        ${analysisData.company}
Sector:         ${analysisData.sector}
Locatie:        ${analysisData.location}
Gegenereerd:    ${new Date(metadata.generatedAt).toLocaleString('nl-NL')}
Generatie tijd: ${metadata.generationTime}s
AI Model:       Claude ${metadata.model}

⚠️ DISCLAIMER: Dit rapport is gegenereerd door AI en dient als
hulpmiddel voor besluitvorming. Verifieer kritieke data altijd
met actuele bronnen.

═══════════════════════════════════════════════════════════

${report}

═══════════════════════════════════════════════════════════
CONTACT
═══════════════════════════════════════════════════════════

Vragen over dit rapport?
Email: info@recruitin.com
Website: https://recruitin.com

© ${new Date().getFullYear()} WouterArts Recruitin
    `.trim();
  }

  /**
   * Convert Markdown to basic HTML
   * @param {string} markdown - Markdown text
   * @returns {string} - HTML text
   */
  markdownToHtml(markdown) {
    return markdown
      // Headers
      .replace(/^### (.*$)/gim, '<h3>$1</h3>')
      .replace(/^## (.*$)/gim, '<h2>$1</h2>')
      .replace(/^# (.*$)/gim, '<h1>$1</h1>')
      // Bold
      .replace(/\*\*\*(.+?)\*\*\*/g, '<strong><em>$1</em></strong>')
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      // Italic
      .replace(/\*(.+?)\*/g, '<em>$1</em>')
      // Links
      .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>')
      // Line breaks
      .replace(/\n\n/g, '</p><p>')
      // Lists (simple conversion)
      .replace(/^\s*[-*]\s+(.+)$/gim, '<li>$1</li>')
      .replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>')
      // Wrap in paragraphs
      .split('\n\n')
      .map(block => {
        if (block.startsWith('<h') || block.startsWith('<ul') || block.startsWith('<ol')) {
          return block;
        }
        return `<p>${block}</p>`;
      })
      .join('\n');
  }

  /**
   * Test email configuration
   * @returns {Promise<boolean>} - Test result
   */
  async testConnection() {
    try {
      await this.transporter.verify();
      logger.info('Email service connection verified');
      return true;
    } catch (error) {
      logger.error('Email service connection test failed', { error: error.message });
      return false;
    }
  }
}

// Export singleton instance
export default new EmailService();
