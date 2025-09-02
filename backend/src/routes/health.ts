import { Router, Request, Response } from 'express';

const router: Router = Router();

// Health check endpoint
router.get('/', (req: Request, res: Response) => {
  res.status(200).json({ 
    status: 'OK', 
    timestamp: new Date().toISOString(),
    service: 'Backend API'
  });
});

export default router;