import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

const appEntry = document.getElementById('appEntry');
if (appEntry) {
  ReactDOM.render(<App />, appEntry);
}

// toggle dropdown menu item
function toggleDropDownMenu(menuEl) {
  menuEl.classList.toggle('open');
}

// add click listeners to userInfo nav options
const userInfo = document.querySelector('#userInfo');
if (userInfo) {
  const userNav = document.querySelector('#userNav');
  userInfo.addEventListener('click', () => {
    toggleDropDownMenu(userNav);
  });
}

// enable module movement within moduleWindow
const newPlacementButton = document.querySelector('#newPlacementButton');
const viewPlacementsButton = document.querySelector('#viewPlacementsButton');
const startModule = document.querySelector('#welcomeModule');

if (startModule) {
  // add advancement listener for new placement button
  const newPlacementMod = document.querySelector('#newPlacementModule');
  newPlacementButton.addEventListener('click', () => {
    startModule.classList.add('pushedLeft');
    newPlacementMod.classList.add('pushedLeft');
  });

  // add back options
  const newBackButton = newPlacementMod.querySelector('.backButton');
  newBackButton.addEventListener('click', () => {
    startModule.classList.remove('pushedLeft');
    newPlacementMod.classList.remove('pushedLeft');
  });

  if (viewPlacementsButton) {
    // ... and the same for viewing existing ones
    const placementsMod = document.querySelector('#existingPlacementsModule');
    viewPlacementsButton.addEventListener('click', () => {
      startModule.classList.add('pushedLeft');
      placementsMod.classList.add('pushedLeft');
    });
    // existing back options
    const viewBackButton = placementsMod.querySelector('.backButton');
    viewBackButton.addEventListener('click', () => {
      startModule.classList.remove('pushedLeft');
      placementsMod.classList.remove('pushedLeft');
    });
  }
}
