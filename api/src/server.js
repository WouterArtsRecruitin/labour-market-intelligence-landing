import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import logger from './utils/logger.js';
import reportRoutes from './routes/report.routes.js';

// Load environment variables
dotenv.config();

// Get __dirname equivalent in ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3002;

// Security middleware
app.use(helmet({
  contentSecurityPolicy: false, // Allow flexibility for API responses
  crossOriginEmbedderPolicy: false
}));

// CORS configuration
const allowedOrigins = process.env.ALLOWED_ORIGINS
  ? process.env.ALLOWED_ORIGINS.split(',')
  : [
    'http://localhost:3000',
    'http://localhost:5500',
    'http://127.0.0.1:5500',
    'https://labour-market-intelligence.netlify.app'
  ];

app.use(cors({
  origin: (origin, callback) => {
    // Allow requests with no origin (mobile apps, Postman, etc.)
    if (!origin) return callback(null, true);

    if (allowedOrigins.includes(origin) || origin.includes('localhost')) {
      callback(null, true);
    } else {
      logger.warn('CORS blocked request', { origin });
      callback(new Error('Not allowed by CORS'));
    }
  },
  credentials: true,
  methods: ['GET', 'POST', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));

// Rate limiting
const limiter = rateLimit({
  windowMs: parseInt(process.env.RATE_LIMIT_WINDOW_MS) || 15 * 60 * 1000, // 15 minutes
  max: parseInt(process.env.RATE_LIMIT_MAX_REQUESTS) || 10, // Limit each IP to 10 requests per windowMs
  message: {
    success: false,
    error: 'Te veel verzoeken van dit IP-adres. Probeer het later opnieuw.'
  },
  standardHeaders: true,
  legacyHeaders: false,
});

// Apply rate limiting to API routes
app.use('/api/', limiter);

// Body parsing middleware
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// Request logging middleware
app.use((req, res, next) => {
  logger.info('Incoming request', {
    method: req.method,
    path: req.path,
    ip: req.ip,
    userAgent: req.get('user-agent')
  });
  next();
});

// Root endpoint
app.get('/', (req, res) => {
  res.json({
    service: 'Labour Market Intelligence API',
    version: '1.0.0',
    status: 'running',
    endpoints: {
      health: '/api/health',
      status: '/api/status',
      generateReport: 'POST /api/generate-report'
    },
    documentation: 'https://github.com/WouterArtsRecruitin/labour-market-intelligence-landing'
  });
});

// API routes
app.use('/api', reportRoutes);

// 404 handler
app.use((req, res) => {
  res.status(404).json({
    success: false,
    error: 'Endpoint not found',
    path: req.path
  });
});

// Global error handler
app.use((err, req, res, next) => {
  logger.error('Unhandled error', {
    error: err.message,
    stack: err.stack,
    path: req.path
  });

  res.status(err.status || 500).json({
    success: false,
    error: err.message || 'Internal server error',
    ...(process.env.NODE_ENV === 'development' && { stack: err.stack })
  });
});

// Start server
app.listen(PORT, () => {
  logger.info(`🚀 Labour Market Intelligence API started`, {
    port: PORT,
    environment: process.env.NODE_ENV || 'development',
    nodeVersion: process.version
  });

  // Log configuration status
  logger.info('Configuration status', {
    anthropicApiKey: !!process.env.ANTHROPIC_API_KEY ? '✓ Configured' : '✗ Missing',
    emailConfigured: !!process.env.EMAIL_USER ? '✓ Configured' : '✗ Missing',
    allowedOrigins: allowedOrigins.length
  });

  // Warn if important env vars are missing
  if (!process.env.ANTHROPIC_API_KEY) {
    logger.warn('⚠️  ANTHROPIC_API_KEY not set - report generation will fail');
  }
  if (!process.env.EMAIL_USER || !process.env.EMAIL_PASSWORD) {
    logger.warn('⚠️  Email not configured - reports will not be sent via email');
  }
});

// Graceful shutdown
process.on('SIGTERM', () => {
  logger.info('SIGTERM received, shutting down gracefully');
  process.exit(0);
});

process.on('SIGINT', () => {
  logger.info('SIGINT received, shutting down gracefully');
  process.exit(0);
});

// Uncaught exception handler
process.on('uncaughtException', (error) => {
  logger.error('Uncaught Exception', {
    error: error.message,
    stack: error.stack
  });
  process.exit(1);
});

// Unhandled rejection handler
process.on('unhandledRejection', (reason, promise) => {
  logger.error('Unhandled Rejection', {
    reason,
    promise
  });
});

export default app;
