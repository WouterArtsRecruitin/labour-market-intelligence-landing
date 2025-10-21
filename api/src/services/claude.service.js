import Anthropic from '@anthropic-ai/sdk';
import logger from '../utils/logger.js';
import { generateMarketAnalysisPrompt, generateQuickAnalysisPrompt } from '../prompts/market-analysis.js';

class ClaudeService {
  constructor() {
    if (!process.env.ANTHROPIC_API_KEY) {
      throw new Error('ANTHROPIC_API_KEY is not set in environment variables');
    }

    this.client = new Anthropic({
      apiKey: process.env.ANTHROPIC_API_KEY,
    });

    // Claude model configuration
    this.model = 'claude-3-5-sonnet-20241022'; // Latest and most capable model
    this.maxTokens = 8000; // Enough for comprehensive reports
    this.temperature = 0.7; // Balance between creativity and consistency
  }

  /**
   * Generate a comprehensive labour market intelligence report
   * @param {Object} analysisData - Market analysis parameters
   * @param {boolean} quickMode - If true, generate shorter report
   * @returns {Promise<Object>} - Generated report and metadata
   */
  async generateMarketReport(analysisData, quickMode = false) {
    try {
      logger.info('Starting market report generation', {
        company: analysisData.company,
        position: analysisData.position,
        quickMode
      });

      // Select appropriate prompt based on mode
      const prompt = quickMode
        ? generateQuickAnalysisPrompt(analysisData)
        : generateMarketAnalysisPrompt(analysisData);

      const startTime = Date.now();

      // Call Claude API
      const response = await this.client.messages.create({
        model: this.model,
        max_tokens: quickMode ? 4000 : this.maxTokens,
        temperature: this.temperature,
        messages: [
          {
            role: 'user',
            content: prompt
          }
        ]
      });

      const endTime = Date.now();
      const generationTime = ((endTime - startTime) / 1000).toFixed(2);

      // Extract report text from response
      const reportContent = response.content[0].text;

      logger.info('Market report generated successfully', {
        generationTime: `${generationTime}s`,
        tokens: response.usage.output_tokens,
        model: this.model
      });

      return {
        success: true,
        report: reportContent,
        metadata: {
          generatedAt: new Date().toISOString(),
          generationTime: parseFloat(generationTime),
          model: this.model,
          tokenUsage: {
            input: response.usage.input_tokens,
            output: response.usage.output_tokens,
            total: response.usage.input_tokens + response.usage.output_tokens
          },
          analysisType: quickMode ? 'quick' : 'comprehensive',
          company: analysisData.company,
          position: analysisData.position,
          location: analysisData.location
        }
      };

    } catch (error) {
      logger.error('Error generating market report', {
        error: error.message,
        stack: error.stack,
        analysisData: {
          company: analysisData.company,
          position: analysisData.position
        }
      });

      // Handle specific Anthropic API errors
      if (error.status === 401) {
        throw new Error('Invalid Anthropic API key');
      } else if (error.status === 429) {
        throw new Error('API rate limit exceeded. Please try again later.');
      } else if (error.status === 500) {
        throw new Error('Anthropic API server error. Please try again later.');
      }

      throw new Error(`Failed to generate report: ${error.message}`);
    }
  }

  /**
   * Validate analysis data before sending to Claude
   * @param {Object} analysisData - Data to validate
   * @returns {Object} - Validation result
   */
  validateAnalysisData(analysisData) {
    const errors = [];
    const required = ['company', 'position', 'sector', 'location', 'experienceLevel', 'keySkills'];

    for (const field of required) {
      if (!analysisData[field]) {
        errors.push(`Missing required field: ${field}`);
      }
    }

    // Validate skills format
    if (analysisData.keySkills) {
      if (Array.isArray(analysisData.keySkills) && analysisData.keySkills.length === 0) {
        errors.push('keySkills array cannot be empty');
      }
    }

    // Validate salary range if provided
    if (analysisData.salaryRange) {
      const { min, max } = analysisData.salaryRange;
      if (min && max && min >= max) {
        errors.push('Salary min must be less than max');
      }
    }

    return {
      valid: errors.length === 0,
      errors
    };
  }

  /**
   * Get service health status
   * @returns {Promise<Object>} - Health status
   */
  async getHealthStatus() {
    try {
      // Test API connection with minimal request
      const response = await this.client.messages.create({
        model: this.model,
        max_tokens: 10,
        messages: [
          {
            role: 'user',
            content: 'test'
          }
        ]
      });

      return {
        status: 'healthy',
        model: this.model,
        apiConnected: true,
        timestamp: new Date().toISOString()
      };
    } catch (error) {
      logger.error('Claude service health check failed', { error: error.message });
      return {
        status: 'unhealthy',
        error: error.message,
        apiConnected: false,
        timestamp: new Date().toISOString()
      };
    }
  }
}

// Export singleton instance
export default new ClaudeService();
