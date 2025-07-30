# 🛫 SkyPort - Airline Booking System

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![Next.js](https://img.shields.io/badge/Next.js-13+-black.svg)](https://nextjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-4.5+-blue.svg)](https://typescriptlang.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)](https://postgresql.org)

A modern, full-stack airline booking system that simplifies flight search, booking, and management with a seamless user experience and robust administrative controls.

## 📄 Abstract

SkyPort is a comprehensive airline booking platform designed to modernize air travel booking experience. Built with Next.js and TypeScript for the frontend, Flask for the backend API, and PostgreSQL for data persistence, it provides an efficient solution for both travelers and administrators. The system handles everything from flight searches and seat selection to payment processing and ticket generation.

## ✨ Key Features

### 👤 User Features
- **Authentication**: JWT-based secure login and registration
- **Flight Search**: Real-time search by city, airport, or date
- **Seat Selection**: Interactive seat map with add-ons
- **Booking Management**: Confirmation, payment, and history
- **Digital Tickets**: PDF generation with QR codes
- **Profile Management**: View and cancel bookings

### 🛫 Admin Features
- **Flight Management**: Add, edit, delete flights
- **Inventory Control**: Manage seat availability
- **Airport & Aircraft Management**: Comprehensive metadata control
- **Analytics**: Real-time booking statistics and reports
- **User Management**: Role-based access control

### 📦 Additional Features
- Payment gateway integration (Stripe/Razorpay)
- Email confirmations and notifications
- Responsive design (mobile-friendly)
- PDF ticket generation with QR codes
- Multi-role system (User/Admin)

## 🧰 Technology Stack

### Frontend
- **Framework**: Next.js 13+ (React with SSR)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **HTTP Client**: Axios
- **Form Handling**: React Hook Form + Zod validation
- **State Management**: React Context/Redux (if applicable)

### Backend
- **Framework**: Flask (Python)
- **Authentication**: Flask-JWT-Extended
- **Database ORM**: SQLAlchemy
- **Migrations**: Flask-Migrate
- **Email**: Flask-Mail
- **CORS**: Flask-CORS
- **Validation**: Marshmallow/Pydantic

### Database
- **Primary Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migration Tool**: Alembic (via Flask-Migrate)

## 🏗️ Architecture Overview

```
┌─────────────────┐    HTTP/REST API    ┌─────────────────┐    SQLAlchemy ORM    ┌─────────────────┐
│   Frontend      │ ◄─────────────────► │   Backend       │ ◄─────────────────► │   Database      │
│   (Next.js)     │                     │   (Flask)       │                     │   (PostgreSQL)  │
│                 │                     │                 │                     │                 │
│ • User Interface│                     │ • REST API      │                     │ • Users         │
│ • Authentication│                     │ • JWT Auth      │                     │ • Flights       │
│ • Flight Search │                     │ • Business Logic│                     │ • Bookings      │
│ • Booking Flow  │                     │ • Data Validation│                     │ • Payments      │
└─────────────────┘                     └─────────────────┘                     └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ and npm/yarn
- Python 3.8+
- PostgreSQL 13+
- Git

### 1. Clone Repository
```bash
git clone https://github.com/Abhishek2063/skyport.git
cd skyport
```

### 2. Backend Setup

#### Environment Setup
```bash
cd backend
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Environment Variables
Create `.env` file in backend directory:
```env
# Database
SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost:5432/skyport_db
SQLALCHEMY_TRACK_MODIFICATIONS=False

# JWT
JWT_SECRET_KEY=your-super-secret-jwt-key-here
JWT_ACCESS_TOKEN_EXPIRES=3600

# Email (Optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Payment Gateway (Optional)
STRIPE_SECRET_KEY=sk_test_...
RAZORPAY_KEY_ID=rzp_test_...
RAZORPAY_KEY_SECRET=...
```

#### Database Setup
```bash
# Initialize migration repository
flask db init

# Create initial migration
flask db migrate -m "Initial migration"

# Apply migrations
flask db upgrade
```

#### Run Backend Server
```bash
python run.py
```
Backend will be available at `http://localhost:5000`

### 3. Frontend Setup

#### Navigate to Frontend Directory
```bash
cd ../frontend
```

#### Install Dependencies
```bash
npm install
# or
yarn install
```

#### Environment Variables
Create `.env.local` file in frontend directory:
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:5000/api
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...
NEXT_PUBLIC_APP_NAME=SkyPort
```

#### Run Frontend Server
```bash
npm run dev
# or
yarn dev
```
Frontend will be available at `http://localhost:3000`

## 📊 Database Schema

### Core Tables
- **users**: User accounts and authentication
- **roles**: User role management
- **airports**: Airport information and codes
- **aircrafts**: Aircraft specifications
- **flights**: Flight schedules and pricing
- **bookings**: Reservation records
- **payments**: Transaction history

### Relationships
```
Role (1:M) User (1:M) Booking (M:1) Flight
                ↓           ↓
            Payment     Aircraft + Airports
```

## 🔐 Security Features

- **Authentication**: JWT-based stateless authentication
- **Authorization**: Role-based access control (RBAC)
- **Password Security**: bcrypt hashing
- **Input Validation**: Server-side validation with Marshmallow
- **CORS Protection**: Configured for cross-origin requests
- **SQL Injection Prevention**: SQLAlchemy ORM parameterized queries
- **HTTPS Ready**: SSL/TLS support for production

## 📁 Project Structure

```
skyport/
├── backend/
│   ├── app/
│   │   ├── __init__.py          # Application factory
│   │   ├── extensions.py        # Extension initialization
│   │   ├── config.py           # Configuration
│   │   ├── models/             # Database models
│   │   ├── routes/             # API routes
│   │   └── utils/              # Utility functions
│   ├── migrations/             # Database migrations
│   ├── requirements.txt        # Python dependencies
│   └── run.py                 # Application entry point
│
├── frontend/
│   ├── src/
│   │   ├── components/         # React components
│   │   ├── pages/             # Next.js pages
│   │   ├── hooks/             # Custom React hooks
│   │   ├── utils/             # Utility functions
│   │   ├── types/             # TypeScript type definitions
│   │   └── styles/            # CSS/Tailwind styles
│   ├── public/                # Static assets
│   ├── package.json           # Node.js dependencies
│   └── next.config.js         # Next.js configuration
│
└── README.md                  # This file
```

## 🔧 Development

### Backend Development
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run with auto-reload
export FLASK_ENV=development
python run.py

# Create new migration
flask db migrate -m "Description of changes"

# Apply migrations
flask db upgrade
```

### Frontend Development
```bash
# Start development server with hot reload
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Type checking
npm run type-check

# Linting
npm run lint
```

## 🧪 Testing

### Backend Testing
```bash
# Run unit tests
python -m pytest

# Run with coverage
python -m pytest --cov=app
```

### Frontend Testing
```bash
# Run Jest tests
npm test

# Run E2E tests (if configured)
npm run test:e2e
```

## 🚀 Deployment

### Backend Deployment (Production)
```bash
# Install production dependencies
pip install -r requirements.txt

# Set environment variables
export FLASK_ENV=production
export SQLALCHEMY_DATABASE_URI=postgresql://...

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

### Frontend Deployment
```bash
# Build for production
npm run build

# Start production server
npm start

# Or deploy to Vercel/Netlify
```

### Environment-Specific Configurations
- **Development**: Debug mode, detailed error messages
- **Production**: Optimized builds, error logging, SSL enforcement

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Use TypeScript for all frontend code
- Write unit tests for new features
- Update documentation as needed

## 📝 API Documentation

### Authentication Endpoints
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/refresh` - Token refresh
- `DELETE /api/auth/logout` - User logout

### Flight Endpoints
- `GET /api/flights/search` - Search flights
- `GET /api/flights/:id` - Get flight details
- `POST /api/flights` - Create flight (Admin)
- `PUT /api/flights/:id` - Update flight (Admin)

### Booking Endpoints
- `POST /api/bookings` - Create booking
- `GET /api/bookings` - Get user bookings
- `GET /api/bookings/:id` - Get booking details
- `DELETE /api/bookings/:id` - Cancel booking

## 🐛 Troubleshooting

### Common Issues

**Database Connection Error**
```bash
# Check PostgreSQL service
sudo service postgresql status

# Verify connection string
psql postgresql://username:password@localhost:5432/skyport_db
```

**Migration Issues**
```bash
# Reset migrations (development only)
flask db downgrade base
flask db upgrade

# Resolve conflicts
flask db merge -m "Merge migrations"
```

**Frontend Build Errors**
```bash
# Clear cache
npm run clean
rm -rf .next node_modules
npm install
```

## 🚀 Future Enhancements

- [ ] Mobile app development (React Native)
- [ ] Real-time flight tracking integration
- [ ] AI-based fare prediction
- [ ] Frequent flyer program
- [ ] Multi-language support
- [ ] Web check-in functionality
- [ ] Advanced analytics dashboard
- [ ] Integration with airline APIs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Abhishek Kumar**
- GitHub: [@Abhishek2063](https://github.com/Abhishek2063)
- Project Link: [https://github.com/Abhishek2063/skyport](https://github.com/Abhishek2063/skyport)

## 📞 Support

For support, email abhishek@example.com or create an issue in this repository.

---

⭐ **Star this repository if you find it helpful!**