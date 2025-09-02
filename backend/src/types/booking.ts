export interface RawBooking {
    id: number;
    occurrenceId: number;
    resourceId: number;
    start: string;
    end: string;
    title: string;
    rate: number;
    status: string;
    isCasual: boolean;
    related_model: string;
    related_id: number;
}

