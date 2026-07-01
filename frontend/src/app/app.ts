import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

import { ApiService } from './services/api.service';
import { OnInit } from '@angular/core';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    FormsModule,
    CommonModule
  ],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {

  apiResult: any = null;
  crops: string[] = [];
  states: string[] = [];
  seasons: string[] = [];

  loading = false;
  userInput = {
    crop: '',
    crop_year: 2026,
    season: '',
    state: '',
    area: 0,
    production: 0,
    method: 'mean'
  };
  
  constructor(
    private api: ApiService
  ) {}
  ngOnInit() {
  this.api.getDropdowns().subscribe((data: any) => {
    this.crops = data.crops;
    this.states = data.states;
    this.seasons = data.seasons;
  });
}
  makePrediction() {

  this.loading = true;
  this.apiResult = null;

  this.api.predict(this.userInput)
    .subscribe({
      next: (response) => {
        console.log(response);
        this.apiResult = response;
        this.loading = false;
      },

      error: (error) => {
        console.error(error);
        this.loading = false;
      }
    });
}
}