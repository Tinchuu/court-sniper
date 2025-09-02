import { RawBooking } from '../types/booking';

export class BookingService {
  private static instance: BookingService;
  private pingInterval: NodeJS.Timeout | null = null;
  private readonly PING_INTERVAL_MS = 15000;
  private readonly API_BASE_URL = 'https://platform.aklbadminton.com/api/booking/feed';
  private currentData: RawBooking[] = [];
  private currentDateRange: { start: string; end: string } | null = null;

  private constructor() {}

  public static getInstance(): BookingService {
    if (!BookingService.instance) {
      BookingService.instance = new BookingService();
    }
    return BookingService.instance;
  }

  /**
   * Start the pinging system with optional date range
   */
  public startPinging(start?: string, end?: string): void {
    if (this.pingInterval) {
      console.log('Pinging system is already running');
      return;
    }

    // Set date range
    if (start && end) {
      this.currentDateRange = { start, end };
    } else {
      this.currentDateRange = this.getDefaultDateRange();
    }

    console.log(`Starting booking data pinging system for ${this.currentDateRange.start} to ${this.currentDateRange.end}...`);
    
    // Initial fetch
    this.ping();
    
    // Set up interval
    this.pingInterval = setInterval(() => {
      this.ping();
    }, this.PING_INTERVAL_MS);
  }

  /**
   * Stop the pinging system
   */
  public stopPinging(): void {
    if (this.pingInterval) {
      clearInterval(this.pingInterval);
      this.pingInterval = null;
      console.log('Pinging system stopped');
    }
  }

  /**
   * Update the date range for pinging
   */
  public setDateRange(start: string, end: string): void {
    this.currentDateRange = { start, end };
    console.log(`Date range updated to: ${start} to ${end}`);
  }

  /**
   * Get default date range (today to next month)
   */
  private getDefaultDateRange(): { start: string; end: string } {
    const today = new Date();
    const nextMonth = new Date(today);
    nextMonth.setMonth(today.getMonth() + 1);

    const start = today.toISOString().split('T')[0];
    const end = nextMonth.toISOString().split('T')[0];

    return { start, end };
  }

  /**
   * Single ping to fetch data
   */
  public async ping(): Promise<RawBooking[]> {
    try {
      if (!this.currentDateRange) {
        this.currentDateRange = this.getDefaultDateRange();
      }

      const { start, end } = this.currentDateRange;
      const url = `${this.API_BASE_URL}?start=${start}&end=${end}`;
      
      console.log(`Pinging: ${url}`);
      
      const response = await fetch(url, {
        headers: {
          'Accept': 'application/json',
          'User-Agent': 'Court-Sniper-Backend/1.0.0'
        }
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      this.currentData = Array.isArray(data) ? data : [];
      
      console.log(`Fetched ${this.currentData.length} booking records`);
      
      return this.currentData;
    } catch (error) {
      console.error('Error pinging API:', error);
      return [];
    }
  }

  /**
   * Get current raw booking data
   */
  public getCurrentData(): RawBooking[] {
    return this.currentData;
  }

  /**
   * Get current date range
   */
  public getCurrentDateRange(): { start: string; end: string } | null {
    return this.currentDateRange;
  }

  /**
   * Fetch data for specific date range (one-time fetch)
   */
  public async fetchDataForDateRange(start: string, end: string): Promise<RawBooking[]> {
    try {
      const url = `${this.API_BASE_URL}?start=${start}&end=${end}`;
      
      console.log(`One-time fetch: ${url}`);
      
      const response = await fetch(url, {
        headers: {
          'Accept': 'application/json',
          'User-Agent': 'Court-Sniper-Backend/1.0.0'
        }
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return Array.isArray(data) ? data : [];
    } catch (error) {
      console.error('Error fetching data for date range:', error);
      return [];
    }
  }
}