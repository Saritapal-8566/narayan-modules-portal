from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests

from places_sync import get_google_maps_photos  # Make sure requests is imported if you're calling the API here

app = Flask(__name__)

# ====================================================================
# INSERT THE NEW CODE EXACTLY HERE (AFTER THE FLASK APP INITIALIZATION)
# ====================================================================

# 1. Fetch live review and uploaded photos from your Google Places helper function
# This returns an array of direct links like: ['https://lh3.googleusercontent.com/p/AF1Qip...', ...]
GOOGLE_PHOTOS = get_google_maps_photos(api_key="YOUR_GOOGLE_MAPS_API_KEY", place_id="YOUR_PLACE_ID")

# 2. Map them directly to your products array
# COMPANY_PRODUCTS = [
#     {
#         "id": 1,
#         "name": "VMC Job Work",
#         "category": "services",
#         "price": "Core RFQ",
#         # Uses the 1st photo from Google Uploads. If empty, uses a live online fallback.
#         "image_url": GOOGLE_PHOTOS[0] if len(GOOGLE_PHOTOS) > 0 else "https://images.unsplash.com/photo-1581092160607-ee22621dd758?q=80&w=600",
#         "description": "Precision heavy component machining using advanced vertical milling infrastructure.",
#         "specs": {"Process Type": "VMC Machining", "Capacity": "Heavy & Medium Components"}
#     },
#     {
#         "id": 2,
#         "name": "Mild Steel Linear Guideway Profile Rail",
#         "category": "components",
#         "price": "Custom Pricing",
#         # Uses the 2nd photo from Google Uploads.
#         "image_url": GOOGLE_PHOTOS[1] if len(GOOGLE_PHOTOS) > 1 else "https://images.unsplash.com/photo-1537462715879-360eeb61a0bc?q=80&w=600",
#         "description": "High-accuracy linear guideway units engineered for high-performance motion tracks.",
#         "specs": {"Size": "45 mm", "Block Type": "Square / Block", "Material": "Mild Steel"}
#     },
#     {
#         "id": 3,
#         "name": "CNC Metal Components",
#         "category": "components",
#         "price": "₹ 560 / Piece",
#         # Uses the 3rd photo from Google Uploads.
#         "image_url": GOOGLE_PHOTOS[2] if len(GOOGLE_PHOTOS) > 2 else "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?q=80&w=600",
#         "description": "High-precision turning components machined with ultra-tight tolerance thresholds.",
#         "specs": {"Material": "Mild Steel (MS)", "Process Type": "CNC Turning"}
#     },
#     {
#         "id": 4,
#         "name": "CAM Machining Job Work",
#         "category": "services",
#         "price": "Contact for Pricing",
#         # Uses the 4th photo from Google Uploads.
#         "image_url": GOOGLE_PHOTOS[3] if len(GOOGLE_PHOTOS) > 3 else "https://images.unsplash.com/photo-1563770660941-20978e870e26?q=80&w=600",
#         "description": "Advanced automated toolpath generation using state-of-the-art CAD/CAM software suites for complex die molds.",
#         "specs": {"Software": "Advanced CAM Software", "Capabilities": "Die Moulds"}
#     }
# ]

# app.py

# Replace your previous array setup with this explicitly mapped dictionary layout
# app.py

# app.py

COMPANY_PRODUCTS = [
    {
        "id": 1,
        "name": "VMC Job Work",
        "category": "services",
        "price": "₹ 550 / Hour",
        "image_url": "https://images.unsplash.com/photo-1581092160607-ee22621dd758?q=80&w=600",
        "description": "Expert high-precision VMC machining components tailored for automobile, mining, compressor, and agricultural equipment industrial frameworks.",
        "specs": {"Process Type": "VMC Milling Work", "Application": "Automotive, Heavy Machinery"}
    },
    {
        "id": 2,
        "name": "Mild Steel Linear Guideway Profile Rail",
        "category": "components",
        "price": "₹ 2,500 / Piece",
        "image_url": "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?q=80&w=600",
        "description": "High-accuracy linear movement guideway rail profiles optimized for smooth machine sliding components.",
        "specs": {"Size": "45 mm", "Block Type": "Square / Block", "Material": "Mild Steel (MS)", "Rail Length": "1000 mm (1 mtr)"}
    },
    {
        "id": 3,
        "name": "10mm Stainless Steel Piston Rod",
        "category": "components",
        "price": "₹ 200 / Piece",
        "image_url": "/static/images/piston_rod.jpg",
        "description": "Premium anti-corrosive solid stainless steel linear shaft piston rods engineered for structural longevity under mechanical fatigue.",
        "specs": {"Rod Diameter": "10 mm", "Rod Length": "300 mm", "Material": "Stainless Steel (SS)"}
    },
    {
        "id": 4,
        "name": "CAM Machining Job Work",
        "category": "services",
        "price": "Get Latest Price",
        "image_url": "https://images.unsplash.com/photo-1563770660941-20978e870e26?q=80&w=600",
        "description": "Computer-aided manufacturing operations utilizing advanced software to compute automatable toolpaths for die moulds, custom gears, and complex profiling.",
        "specs": {"Software Capabilities": "CAM, Die Moulds Machining", "Operations": "Gear Cutting, Custom Milling"}
    },
    {
        "id": 5,
        "name": "CNC Metal Component",
        "category": "components",
        "price": "₹ 560 / Piece",
        "image_url": "https://images.unsplash.com/photo-1616401784845-180882ba9ba8?q=80&w=600",
        "description": "High-tolerance precision components generated via automated numerical control turning setups.",
        "specs": {"Material": "Mild Steel (MS)", "Process Type": "CNC Turning", "Tolerance": "±0.005 mm"}
    },
    {
        "id": 6,
        "name": "Stainless Steel Shaft",
        "category": "components",
        "price": "₹ 370 / Piece",
        "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=600",
        "description": "Solid polished steel power-transmission shafting components engineered to survive aggressive operations.",
        "specs": {"Steel Grade": "SS304", "Shaft Diameter": "10 mm", "Shaft Length": "500 mm", "Surface Finish": "Polished"}
    },
    {
        "id": 7,
        "name": "Mild Steel Bushes",
        "category": "components",
        "price": "₹ 500 / Piece",
        "image_url": "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?q=80&w=600",
        "description": "Polished high-tensile plain cylindrical bush bearings designed for heavy automotive suspension or assembly fittings.",
        "specs": {"Material Grade": "MS IS2062", "Inner Diameter": "8 mm", "Outer Diameter": "15 mm", "Length": "25 mm"}
    },
    {
        "id": 8,
        "name": "Aluminum Pneumatic Manifold Block",
        "category": "components",
        "price": "₹ 320 / Piece",
        "image_url": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=600",
        "description": "Anodized aluminum subplate hydraulic manifold fluid system distribution blocks rated for intense operational pressures.",
        "specs": {"Material": "Aluminium", "Working Pressure": "160 bar", "Number Of Ports": "4 Ports", "Port Size": "G 1/4"}
    }
]
# Dynamic product database structure extracted from IndiaMART
# COMPANY_PRODUCTS = [
#     {
#         "id": 1,
#         "name": "VMC Job Work",
#         "category": "services",
#         "price": "₹ 550 / Hour",
#         "description": "Precision machining components utilizing advanced VMC setups. Applicable for automotive, mining, compressors, and agricultural machinery.",
#         "specs": {"Process Type": "VMC Machining", "Capacity": "Heavy & Medium Components"}
#     },
#     {
#         "id": 2,
#         "name": "Mild Steel Linear Guideway Profile Rail",
#         "category": "components",
#         "price": "₹ 2,500 / Piece",
#         "description": "High-accuracy linear guideway rails engineered for industrial linear motion applications.",
#         "specs": {"Size": "45 mm", "Block Type": "Square / Block", "Material": "Mild Steel"}
#     },
#     {
#         "id": 3,
#         "name": "CNC Metal Components",
#         "category": "components",
#         "price": "₹ 560 / Piece",
#         "description": "High-precision turning components machined with ultra-tight tolerance thresholds.",
#         "specs": {"Material": "Mild Steel (MS)", "Process Type": "CNC Turning", "Tolerance": "±0.005 mm"}
#     },
#     {
#         "id": 4,
#         "name": "CAM Machining Job Work",
#         "category": "services",
#         "price": "Contact for Pricing",
#         "description": "Advanced automated toolpath generation using state-of-the-art CAD/CAM software suites for complex die molds.",
#         "specs": {"Software": "Advanced CAM Software", "Capabilities": "Die Moulds & Gear Cutting"}
#     }
# ]

@app.route('/')
def home():
    featured = [p for p in COMPANY_PRODUCTS if p['id'] in [1, 2, 3]]
    return render_template('index.html', products=featured)

@app.route('/catalog')
def catalog():
    # Optional category filter parameter via request query
    category_filter = request.args.get('category')
    if category_filter:
        filtered_list = [p for p in COMPANY_PRODUCTS if p['category'] == category_filter]
    else:
        filtered_list = COMPANY_PRODUCTS
    return render_template('catalog.html', products=filtered_list, current_category=category_filter)

@app.route('/submit-inquiry', methods=['POST'])
def submit_inquiry():
    try:
        data = request.get_json() if request.is_json else request.form
        
        # Capture form parameters
        customer_name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        product_interest = data.get('product')
        message = data.get('message')
        
        # Processing Logic: Insert into DB, trigger a webhook, or send an automated email alert
        print(f"New Leads Generated from {customer_name} ({phone}) for {product_interest}")
        
        if request.is_json:
            return jsonify({"status": "success", "message": "Inquiry successfully submitted to Narayan Moulds."}), 200
        return redirect(url_for('home', success="true"))
        
    except Exception as e:
        if request.is_json:
            return jsonify({"status": "error", "message": str(e)}), 500
        return "An internal execution error occurred.", 500

if __name__ == '__main__':
    app.run(debug=True,port =5001)