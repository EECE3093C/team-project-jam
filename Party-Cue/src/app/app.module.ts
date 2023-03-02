import { Component, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {RouterModule, Routes} from '@angular/router';


//Angular Material Components
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatSlideToggleModule} from '@angular/material/slide-toggle';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatButtonModule } from '@angular/material/button';

//Generated Components
import { AppComponent } from './app.component';
import { MasterViewComponent } from './master-view/master-view.component';
import { InviteViewComponent } from './invite-view/invite-view.component';
import { WelcomePageComponent } from './welcome-page/welcome-page.component';



@NgModule({
  declarations: [
    AppComponent,
    MasterViewComponent,
    InviteViewComponent,
    WelcomePageComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatSlideToggleModule,
    MatGridListModule,
    MatButtonModule,
    RouterModule.forRoot([
      {path: 'home', component: WelcomePageComponent},
      {path: 'master', component: MasterViewComponent},
      {path: 'invited', component: InviteViewComponent},
      {path: '', redirectTo:'/home', pathMatch: 'full'},
    ]),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
