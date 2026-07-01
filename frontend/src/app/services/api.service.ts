import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  predict(data: any) {
    return this.http.post(
      `${this.apiUrl}/predict`,
      data
    );
  }

  getDropdowns() {
    return this.http.get(
      `${this.apiUrl}/dropdowns`
    );
  }

}