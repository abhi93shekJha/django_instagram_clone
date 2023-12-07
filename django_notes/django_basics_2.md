### Server Side Rendering (SSR) and client Side Rendering (CSR)
- In SSR, the server itself creates an HTML page and loads the data into it and sends it to client only to display.
- Initial page loading is faster and SEO will be better in SSR.
- In CSR, server sends data to client and client renders the user interface using the data.
- Apps are more interactive. CSR is now used everywhere, where server side developer shares API to frontend developers.

### Few points when developing SSR
- We will have to create a template folder inside app that keeps html files.
- Floder structure should be template/app_name/html_file.html (notice here the app_name folder inside template directory).
- This keeps away conflit among multiple templates present as projects grow bigger.
- 
