/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html" // This tells Tailwind to scan all .html files in the templates folder
  ],
  theme: {
    extend: {
      fontFamily: {
        // Add Inter font to the 'sans' family
        sans: ['Noto Sans', 'sans-serif'],
      },
    },
  },
  plugins: [],
}