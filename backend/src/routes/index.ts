import { Router } from 'express';
import healthRoutes from './health';
import bookingRoutes from './bookings';

const router: Router = Router();

router.use('/health', healthRoutes);
router.use('/api/bookings', bookingRoutes);

router.get('/api', (req, res) => {
  res.json({ 
    message: 'Welcome to the Backend API',
    version: '1.0.0',
    endpoints: {
      health: '/health',
      bookings: '/api/bookings',
      days: '/api/days'
    }
  });
});

export default router;