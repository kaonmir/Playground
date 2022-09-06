export abstract class LocalStorageService {
  abstract get(key: string): string | null;
  abstract set(key: string, value: string): void;
}
