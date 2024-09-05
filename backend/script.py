from sqlalchemy.orm import Session, relationship
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Subcategory(Base):
    __tablename__ = 'subcategories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    subcategory = Column(String(length=50), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship("Category", back_populates="subcategories")


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(length=50), nullable=False)
    subcategories = relationship("Subcategory", order_by=Subcategory.id, back_populates="category")


# 创建数据库引擎（请根据实际数据库配置修改连接字符串）
engine = create_engine('mysql+pymysql://lizengsb:lizengsb@140.82.1.32:3306/butterpply-employer', echo=True)

# 创建一个新的会话
session = Session(bind=engine)

# 定义主类别
main_categories = [
    "Accounting & Consulting",
    "Admin Support",
    "AI Service",
    "Arts & Design",
    "Beauty & Wellness",
    "Data Science & Analytics",
    "Engineering & Architecture",
    "Finance & Legal",
    "Household and Support Services",
    "Information Technology",
    "Marketing & Sales",
    "Mobile, Web & Software Development",
    "Teaching & Education",
    "Translation",
    "Writing"
]

# 插入主类别到数据库
category_objects = {cat: Category(category=cat) for cat in main_categories}
session.add_all(category_objects.values())
session.commit()

# 子类别数据
subcategories_data = {
    "Accounting & Consulting": ["Accounting", "Bookkeeping", "Business Analysis & Strategy", "Career Coaching",
                                "Financial Analysis & Modelling", "Financial Management/CFO", "HR Administration",
                                "Instructional Design", "Management Consulting", "Personal Coaching",
                                "Recruiting & Talent Souring", "Training & Development", "Tax Preparation"],
    "Admin Support": ["Business Project Management", "Construction & Engineering Project Management", "Data Entry",
                      "Development & IT Project Management", "Digital Project Management", "Ecommerce Management",
                      "Executive Virtual Assistance", "General Research Service", "General Virtual Assistance",
                      "Healthcare Project Management", "Legal Virtual Assistance", "Manual Transcription",
                      "Medical Virtual Assistance", "Personal Virtual Assistance",
                      "Qualitative & Quantitative Research",
                      "Supply Chain & Logistics Project Management", "Web & Software Product Research"],
    "AI Service": ["AI Image Generation & Edit", "AI Speech & Audio Generation", "AI Video Generation & Editing",
                   "AI Content Writing & Editing", "AI Agent & Chatbot Development", "AI App Development",
                   "AI API Integration", "AI Model Development", "AI Ethics & Compliance",
                   "Data Analysis & Visualization",
                   "Data Annotation & Labeling", "Data Mining & Cleaning", "Knowledge Representation & Reasoning"],
    "Arts & Design": ["2D & 3D Animation", "AI Image Generation & Edit", "AI Speech & Audio Generation",
                      "AI Video Generation & Editing", "AR/VR Design", "Acting", "Art Direction",
                      "Audio Editing & Production",
                      "Brand Identity Design", "Cartoon & Comics", "Creative Direction", "Editorial Design",
                      "Fashion Design",
                      "Fine Art", "Game Art", "Graphic Design", "Illustration", "Image Editing & Production",
                      "Logo Design",
                      "Motion Graphics", "Music Performance", "Music Production", "NFT Art", "Packaging Design",
                      "Pattern Design", "Portraits & Caricatures", "Presentation Design", "Product & Industrial Design",
                      "Product Photography", "Singing", "Songwriting & Music Composition", "Video Editing & Production",
                      "Videography", "Visual Effects", "Voice Talent", "Web Design"],
    "Beauty & Wellness": ["Acupuncture", "Aromatherapy", "Beauty Treatments", "Body Treatments",
                          "Cupping Therapy", "Foot Therapy", "Hair Services", "Health Massage",
                          "Makeup Services", "Manicure", "Massage Therapies", "Meditation Sessions",
                          "Nail Art", "Nail Services", "Nutrition Counseling", "Skincare Treatments",
                          "Spa Services", "Therapy", "Wellness Coaching", "Yoga Classes"],
    "Data Science & Analytics": ["AI Data Annotation & Labeling", "Data Analytics", "Data Engineering",
                                 "Data Extraction", "Data Mining", "Data Processing", "Data Visualization",
                                 "Experimentation & Testing", "Generative AI Modeling",
                                 "Knowledge Representation", "Machine Learning & Deep Learning"],
    "Engineering & Architecture": ["3D Modeling & Rendering", "Architectural Design", "Biology",
                                   "Building Information Modeling", "CAD", "Chemical & Process Engineering",
                                   "Chemistry", "Civil Engineering", "Electrical Engineering",
                                   "Electronic Engineering", "Energy Engineering", "Interior Design",
                                   "Landscape Architecture", "Logistics & Supply Chain Management",
                                   "Mathematics", "Mechanical Engineering", "Physics", "STEM Tutoring",
                                   "Sourcing & Procurement", "Structural Engineering", "Trade Show Design"],
    "Finance & Legal": ["Banking Service", "Business & Corporate Law", "Immigration Law", "Intellectual Property Law",
                        "International Law", "Labor & Employment Law", "Legal Consulting", "Paralegal Services",
                        "Regulatory Law", "Securities & Finance Law", "Tax Law", "Tax Preparation"],
    "Household and Support Services": ["Appliance Repair Services", "Car Rental Service",
                                       "Carpet and Upholstery Cleaning", "Child Care",
                                       "Elderly Care Services", "Food Delivery Service", "Furniture Assembly Services",
                                       "Gardening and Lawn Care", "Grocery Shopping and Delivery",
                                       "Home Daycare Services",
                                       "Home Maintenance and Repair", "Home Organization Services",
                                       "Home Security Services",
                                       "House Sitting Services", "Housekeeping", "Laundry and Dry Cleaning Services",
                                       "Logistics & Express services", "Moving Service", "Nanny Services",
                                       "Pest Control Services",
                                       "Pet Care Services", "Pool Maintenance Services", "Private Chef Services",
                                       "Snow Removal Services", "Window Cleaning Services"],
    "Information Technology": ["Cybersecurity", "Database Administration", "IT Support", "Network Administration",
                               "Software Development", "Systems Analysis", "Web Development"],
    "Marketing & Sales": ["Advertising", "Brand Strategy", "Campaign Management", "Content Strategy",
                          "Email Marketing", "Lead Generation", "Marketing Automation", "Marketing Research",
                          "Marketing Strategy", "Product Reviews", "Public Relations", "SEO",
                          "Sales & Business Development", "Search Engine Marketing", "Social Media Marketing",
                          "Social Media Strategy", "Telemarketing"],
    "Mobile, Web & Software Development": ["AI Agent & Chatbot Development", "AI Integration", "AR/VR Development",
                                           "Automation Testing",
                                           "Back-End Development", "Blockchain & NFT Development", "CMS Development",
                                           "Coding Tutoring", "Crypto Coins & Tokens", "Crypto Wallet Development",
                                           "Database Development", "Desktop Software Development",
                                           "Ecommerce Website Development", "Emerging Tech", "Firmware Development",
                                           "Front-End Development", "Full Stack Development", "Manual Testing",
                                           "Mobile App Development", "Mobile Design", "Mobile Game Development",
                                           "Product Management", "Prototyping", "Scripting & Automation",
                                           "Scrum Leadership", "UX/UI Design", "Video Game Development", "Web Design"
                                           ],
    "Teaching & Education": ["Curriculum Development", "Language Tutoring", "Online Tutoring", "Special Education",
                             "Test Preparation"],
    "Translation": ["General Translation Services", "Language Localization", "Language Tutoring",
                    "Legal Document Translation", "Live Interpretation", "Medical Document Translation",
                    "Sign Language Interpretation", "Technical Document Translation"],
    "Writing": ["AI Content Writing", "Academic & Research Writing", "Ad & Email Copywriting",
                "Article & Blog Writing", "Business & Proposal Writing", "Copy Editing", "Creative Writing",
                "Editing & Proofreading", "Ghostwriting", "Grant Writing", "Legal Writing", "Marketing Copywriting",
                "Medical Writing", "Proofreading", "Resume & Cover Letter Writing", "Sales Copywriting",
                "Scriptwriting",
                "Technical Writing", "Web & UX Writing", "Writing Tutoring"]
}

# 插入子类别
for cat, subcats in subcategories_data.items():
    category = category_objects[cat]
    for subcat in subcats:
        new_subcategory = Subcategory(subcategory=subcat, category=category)
        session.add(new_subcategory)

session.commit()
session.close()


class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True, autoincrement=True)
    skill = Column(String(length=50), nullable=False)


skills_data = ['Python', 'JavaScript', 'SQL', 'Java', 'C++', 'HTML', 'CSS', 'React', 'Node.js', 'Django', 'Flask',
               'Ruby on Rails', 'Swift', 'Kotlin', 'Go', 'TypeScript', 'Angular', 'Vue.js', 'PHP', 'Perl']

for skill in skills_data:
    new_skill = Skills(skill=skill)
    session.add(new_skill)


session.commit()
session.close()
