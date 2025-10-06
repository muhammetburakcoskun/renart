# Renart - Jewelry Product Showcase

A modern, responsive jewelry product showcase application built with Next.js and FastAPI.

## 🌟 Features

- **Responsive Design**: Beautiful, mobile-first design that works on all devices
- **Product Gallery**: Interactive product cards with color variations
- **Smooth Navigation**: Horizontal scrolling with navigation arrows
- **Real-time Pricing**: Dynamic price calculation based on popularity and weight
- **Color Selection**: Interactive color picker for different metal types (Yellow Gold, Rose Gold, White Gold)
- **Rating System**: Visual star ratings for product popularity
- **Modern UI**: Clean, elegant design with custom fonts (Avenir, Montserrat)

## 🚀 Live Demo

**Frontend (Vercel)**: https://renart-kmxuvl5a2-muhammet-burak-coskuns-projects.vercel.app

**Backend API (Railway)**: https://renartbackend-production.up.railway.app

## 🛠️ Tech Stack

### Frontend
- **Next.js 15.5.4** - React framework with App Router
- **React 19.1.0** - Latest React with concurrent features
- **TypeScript** - Type-safe development
- **TailwindCSS 4** - Utility-first CSS framework
- **Vercel** - Deployment platform

### Backend
- **FastAPI** - Modern Python web framework
- **Python 3.x** - Backend runtime
- **Railway** - Backend deployment platform
- **CORS** - Cross-origin resource sharing enabled

## 📁 Project Structure

```
renart/
├── frontend/                 # Next.js frontend application
│   ├── src/app/
│   │   ├── page.tsx         # Main product showcase page
│   │   ├── layout.tsx       # Root layout component
│   │   └── globals.css      # Global styles and custom CSS
│   ├── public/              # Static assets
│   ├── next.config.ts       # Next.js configuration
│   ├── tailwind.config.ts   # TailwindCSS configuration
│   └── package.json         # Frontend dependencies
├── backend/                 # FastAPI backend application
│   ├── main.py             # FastAPI application
│   ├── products.json       # Product data
│   ├── requirements.txt    # Python dependencies
│   └── Procfile           # Railway deployment config
└── products.json           # Shared product data
```

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ 
- Python 3.8+
- npm or yarn

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run FastAPI server:
```bash
python main.py
```

4. API will be available at [http://localhost:8000](http://localhost:8000)

## 📊 API Endpoints

### Products
- **GET** `/products` - Retrieve all products with calculated pricing
- **GET** `/` - Health check endpoint

### Response Format
```json
[
  {
    "name": "Engagement Ring 1",
    "price": 189.0,
    "popularityScoreOutOf5": 4.2,
    "images": {
      "yellow": "https://cdn.shopify.com/...",
      "rose": "https://cdn.shopify.com/...",
      "white": "https://cdn.shopify.com/..."
    }
  }
]
```

## 🎨 Design Features

- **Custom Fonts**: Avenir for headings, Montserrat for body text
- **Color Palette**: Elegant gold tones and neutral colors
- **Interactive Elements**: Hover effects, smooth transitions
- **Responsive Grid**: 4 products visible on desktop, adaptive on mobile
- **Smooth Scrolling**: Horizontal product navigation

## 🚀 Deployment

### Frontend (Vercel)
1. Connect your GitHub repository to Vercel
2. Deploy automatically on push to main branch
3. Environment variables are automatically configured

### Backend (Railway)
1. Connect your GitHub repository to Railway
2. Railway automatically detects Python/FastAPI
3. Deploys with zero configuration

## 🔧 Configuration

### Environment Variables
- `NODE_ENV`: Set to 'production' for production builds
- Backend URL is automatically configured for production

### Customization
- Product data: Edit `products.json` files
- Styling: Modify `globals.css` and Tailwind classes
- API endpoints: Update `main.py` for backend changes

## 📱 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is created for demonstration purposes.

## 👨‍💻 Author

**Muhammet Burak Coşkun**
- Email: burakcskn44@gmail.com
- GitHub: [@burakcskn44](https://github.com/burakcskn44)

---

**Live Demo**: https://renart-kmxuvl5a2-muhammet-burak-coskuns-projects.vercel.app
