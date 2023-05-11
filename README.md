![Logo](https://drive.google.com/uc?id=1mtkvl1dHlS1i8084uPDKQv59sorBMnIe)  
The Premed Flash Focus is a Python-based tool that uses Tkinter, pandas, and requests to shuffle through a list of 75 medical terms. It is designed to help premed students learn and improve their knowledge of medical terminology. Definitions are sourced directly from an online medical dictionary via Merriam-Webster API.

## Demo

![image](https://github.com/lindajhk/premed-flash-focus/assets/106854298/3509ca7a-4ba5-42a4-95fd-01d1f0518bff)  
The app immediately runs upon start. After three seconds, the word will automatically flip to show the definition. The definition is directly sourced from Merriam-Webster to ensure accuracy and up to date information.  
The user can interact with the GUI with the 3 buttons on the bottom.
Red X icon means you do not know the word. Pressing this will add the word to the words_to_learn csv which will cycle the word back in.  
The blue restart icon means you want to start over with the 75 word list.  
The green checkmark icon means you know the word. Pressing this button will remove the word from your word bank so it will not show up again until restart is clicked.  
Pressing any of the buttons will move to the next card and start the 3-second timer.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY` This is your unique API Key for Merriam-Webster. Without this API, the definition will not show.

